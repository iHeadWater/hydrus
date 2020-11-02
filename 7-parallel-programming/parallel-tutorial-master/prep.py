import datetime
import os
from glob import glob
import pandas as pd
try:
    import ujson as json
except ImportError:
    import json

import dask
import dask.dataframe as dd
import dask.multiprocessing
import os
import sys

here = os.path.dirname(__file__)
os.makedirs(os.path.join(here, 'data', 'minute'), exist_ok=True)

stocks = ['afl', 'bwa',
          'hal', 'hp', 'hpq', 'ibm', 'jbl', 'jpm', 'luv', 'pcg',
          'usb'] # 'aig', 'al', 'avy' 貌似没有数据了

def write_stock(symbol):
    dirname = os.path.join(here, 'data', 'minute', symbol)
    today = datetime.datetime.now().date()
    year = datetime.timedelta(days=365)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        df = dd.demo.daily_stock(symbol, today - year, today, freq='30s',
                                 data_source='yahoo')
        names = [str(ts.date()) for ts in df.divisions]
        df.to_csv(os.path.join(dirname, '*.csv'), name_function=names.__getitem__)
        print("Finished CSV: %s" % symbol)

for symbol in stocks:
    write_stock(symbol)


def convert_to_json(d):
    filenames = sorted(glob(os.path.join(d, '*')))[-365:]
    outfn = d.replace('minute', 'json') + '.json'
    if os.path.exists(outfn):
        return
    with open(outfn, 'w') as f:
        for fn in filenames:
            df = pd.read_csv(fn)
            for rec in df.to_dict(orient='records'):
                json.dump(rec, f)
                f.write('\n')
    print("Finished JSON: %s" % d.split(os.path.sep)[-1])


js = os.path.join(here, 'data', 'json')
if not os.path.exists(js):
    os.mkdir(js)

directories = sorted(glob(os.path.join(here, 'data', 'minute', '*')))
values = [dask.delayed(convert_to_json)(d) for d in directories]
dask.compute(values)
