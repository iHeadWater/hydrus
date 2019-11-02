"""代码来自博客https://machinelearningmastery.com/how-to-develop-lstm-models-for-multi-step-time-series-forecasting-of
-household-power-consumption/ """
import numpy as np
import pandas as pd


# fill missing values with a value at the same time one day ago
def fill_missing(values):
    one_day = 60 * 24
    for row in range(values.shape[0]):
        for col in range(values.shape[1]):
            if np.isnan(values[row, col]):
                values[row, col] = values[row - one_day, col]


# load all data
dataset = pd.read_csv('../data/household_power_consumption.txt', sep=';', header=0, low_memory=False,
                      infer_datetime_format=True, parse_dates={'datetime': [0, 1]}, index_col=['datetime'])

# mark all missing values
dataset.replace('?', np.nan, inplace=True)
# make dataset numeric
dataset = dataset.astype('float32')
# fill missing
fill_missing(dataset.values)

# add a column for for the remainder of sub metering
values = dataset.values
dataset['sub_metering_4'] = (values[:, 0] * 1000 / 60) - (values[:, 4] + values[:, 5] + values[:, 6])

# save updated dataset
dataset.to_csv('../data/household_power_consumption.csv')

# resample minute data to total for each day
# load the new file
dataset = pd.read_csv('../data/household_power_consumption.csv', header=0, infer_datetime_format=True, parse_dates=['datetime'],
                      index_col=['datetime'])
# resample data to daily
daily_groups = dataset.resample('D')
daily_data = daily_groups.sum()
# summarize
print(daily_data.shape)
print(daily_data.head())
# save
daily_data.to_csv('../data/household_power_consumption_days.csv')
