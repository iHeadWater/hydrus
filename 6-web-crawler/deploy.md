# angular+flask+pytorch in Heroku

主要是记录下angular+flask+pytorch的组织过程。

## flask+pytorch

主要参考了：[DEPLOYING PYTORCH IN PYTHON VIA A REST API WITH FLASK](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html)

接下来会使用Flask部署一个pytorch model，并提供一个REST API。如果需要高性能部署，需要进一步了解[torchscript](https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html)，这里暂时就不说了。

首先定义API endpoints，请求和返回类型。API位置点在 /predict ，它接受一个HTTP POST请求，该请求有一个file参数，该参数包含image。对应的响应会是一个JSON文件，包含预测结果的，如下所示：

```JSON
{"class_id": "n02124075", "class_name": "Egyptian_cat"}
```

具体实践的代码可以见：[PyTorch Flask API](https://github.com/avinassh/pytorch-flask-api)。关于Flask简单内容可以参考本repo第一章节python基础。注意Flask是一个微型框架，自身没有提供数据库管理，表单验证，cookie处理等功能，很多功能需要通过扩展才能实现。更多内容可以见官网：[Flask](https://palletsprojects.com/p/flask/).

直接下载下来上面那个repo试验下即可。

## Flask by Example

这部分主要参考了：[Flask by Example](https://realpython.com/flask-by-example-part-1-project-setup/)

这是一个系列博客，讲述了跟flask相关的一系列内容，这是一个全栈式的教程。

### Part One: Project Setup

首先创建项目。然后部署到Heruko上。

#### 创建项目

因为我已经尝试过使用conda来配置虚拟环境的操作，发现并不好用，所以这里暂时先使用pip对应的虚拟环境配置工具virtualenv了，一般情况下pip也够用了。并且貌似google cloud的示例文档也是使用的virtualenv。为了方便，就用它了。如果已经安装了anaconda，应该有virtualenv了，没有的话：

```Shell
pip install virtualenv
```

然后接下来构建项目：

```Shell
mkdir flask-by-example && cd flask-by-example
git init
virtualenv --no-site-packages env --python=python3.7
conda create --name flask python=3.7
source env/bin/activate
touch app.py .gitignore README.md requirements.txt
```

更新ignore文件：

```.ignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# C extensions
*.so

# Distribution / packaging
.Python
env/
bin/
build/
develop-eggs/
dist/
eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.cache
nosetests.xml
coverage.xml

# Translations
*.mo

# Mr Developer
.mr.developer.cfg
.project
.pydevproject

# Rope
.ropeproject

# Django stuff:
*.log
*.pot

# Sphinx documentation
docs/_build/

*.DS_Store
```

然后安装Flask。

```Shell
pip install Flask
pip freeze > requirements.txt
```

修改app.py文件：

```Python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
```

然后运行：

```Shell
python app.py
```

访问  http://localhost:5000/  应该可以看到hello world了。

接下来设置 Heroku 环境，来将应用部署到云端。先了解下Heroku。

#### Heroku

首先在 [Heroku 网站](https://devcenter.heroku.com/articles/getting-started-with-python)上注册账号。然后下载安装Heroku的[Toolbelt](https://toolbelt.heroku.com/)，根据官方提示，直接执行以下命令即可：

```Shell
sudo snap install --classic heroku
```

然后在terminal，执行下面命令登录到 Heroku

```Shell
heroku login
```

按任意键会弹出网页，chrome浏览器自动记住密码了，点击登录即可登录成功。

接下来让我们首先按照 [Heroku 官网的指导](https://devcenter.heroku.com/articles/getting-started-with-python)来使用下这个工具，这样才方便后面的操作。现在安装Postgres。

Ubuntu下直接安装

```Shell
sudo apt-get install postgresql
```

检查安装位置：
`
```Shell
which psql
```

一般是在/usr/bin/psql位置下。

接下来先按照官方教程来部署一个程序。在一个新文件夹下打开terminal，执行：

```Shell
git clone https://github.com/heroku/python-getting-started.git
cd python-getting-started
```

现在就有课一个git repo，包含了一个简单的应用，一个runtime.txt文件，指定了python3.7.3，还有一个requirements.txt文件指定了python依赖包。

现在部署app，在刚才的根目录下执行：

```Shell
heroku create
```

现在heroku为这个app生成了一个随机的名字。现在可以将这个app部署到云端了。

执行：

```Shell
git push heroku master
```

等待片刻，app就构建完成了。现在保证有一个app的实例运行：

```Shell
heroku ps:scale web=1
```

现在就可以通过根据这个app的名称生成的URL来访问这个app了。现在在开发的机器上，比较方便的做法：

```Shell
heroku open
```

这个网站是可以在任意一台电脑上打开的。

使用如下内容可以查看日志：

```Shell
heroku logs --tail
```

这个日志内容是所有heroku上运行的app的输出流的整合。按Control+C可以结束日志。

接下来是 [Procfile](https://devcenter.heroku.com/articles/procfile)，这是一个在app根目录下的text文件，来显示地说明启动app时，执行什么代码。比如：

```Text
web: gunicorn gettingstarted.wsgi --log-file -
```

这里声明了一个进程类型 web，以及运行它需要的命令。web非常重要，它声明了进程类型会联系到 Heroku 的 HTTP routing 栈，部署之后，它可以接受到网络访问。

现在app是运行在dyno上的，所有Heroku的应用都运行在叫dynos的轻量级linux 容器里。把它当做一个而运行Procfile中命令的容器即可。输入以下命令可以检查现在的dynos数：

```Shell
heroku ps
```

默认地应用会部署在一个免费的dyno上。免费的自然有些限制。可以升级到付费的，可见：[heruko pricing](https://www.heroku.com/pricing)。如果升级到付费版，可以你很容易的将app移动到付费版下，这块等用到了再回来看：https://devcenter.heroku.com/articles/getting-started-with-python#scale-the-app

接下来看看app依赖的配置。官网指导的方式是使用 requirements.txt ，在根目录下创建该文件，可以说明python的依赖。当app部署时，Heroku会读取这个文件，并使用pip install -r 来安装合适的python依赖。如果需要代码本地运行，可以执行：

```Shell
pip install -r requirements.txt
```

也可以在本地启动该程序，这个实例用到了Django，需要先运行：

```Shell
python manage.py collectstatic
```

回答yes即可。然后用heroku local启动本地：

```Shell
heroku local web
```

如果想要删除现在的app，可以参考：[如何删除heroku多余部署的app](http://majunnan.logdown.com/posts/1243187-how-to-remove-extra-deployment-heroku-app)

另外，完全“停止”您的应用程序，参考：[如何在Heroku上停止应用程序？](https://stackoom.com/question/BnO1/%E5%A6%82%E4%BD%95%E5%9C%A8Heroku%E4%B8%8A%E5%81%9C%E6%AD%A2%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F)，可以将Web dynos缩小到零：

```Shell
heroku ps:scale web=0
```

#### 本地项目实践

接下来回到本项目，创建一个 Procfile 文件。这是为 Heroku 准备的。Heroku apps 包括一个 Procfile 来指定app启动时想要执行的命令。项目根目录下执行：

```Shell
touch Procfile
```

把下面的内容加到刚创建的Procfile中

```Text
web: gunicorn app:app
```

确保将gunicorn加入到环境文件中，安装gunicorn：

```Shell
pip install gunicorn
pip freeze > requirements.txt
```

需要为 Heroku 指定 python 的版本以使 Heroku 使用正确的 [Python Runtime](https://devcenter.heroku.com/articles/python-runtimes)。为了指定 Python Runtime ，在app的根目录下创建一个 runtime.txt 文件。

```Shell
touch runtime.txt
```

然后增加以下内容：

```Text
python-3.7.4
```

因为virtualenv默认安装的3.7的版本就是3.7.4，所以指定这个版本。现在git commit 下。

```git
git add -A
git commit -m 'heroku'
```

现在先创建新的Heroku apps，一个用于生产环境，一个用于测试环境。

```Shell
heroku create locust2020-pro
heroku create locust2020-stage
```

现在新建远程分支指向，pro和stage到git远程，方便后面app提交。

```Shell
git remote add pro git@heroku.com:locust2020-pro.git
git remote add stage git@heroku.com:locust2020-stage.git
```

（取消本地远程分支指向可以使用：git remote remove pro）

现在可以push app到Heroku。现在本地只有一个master分支，远程的分支有stage和pro两个，分别对应heruko的两个库。

```Shell
git push stage master
git push pro master
```

提交可能会报错，根据：[Permission denied (publickey) when deploying heroku code. fatal: The remote end hung up unexpectedly](https://stackoverflow.com/questions/4269922/permission-denied-publickey-when-deploying-heroku-code-fatal-the-remote-end)，必须上传自己的public key给到Heroku，首先检查自己现在的key：

```Shell
heroku keys
```

如果结果显示没有SSH keys，那么需要创建：

```Shell
heroku keys:add
```

然后选择默认位置即可。接着执行下面语句上传自己的公钥给heroku

```Shell
heroku keys:add ~/.ssh/id_rsa.pub
```

现在已经上传给heroku 了，可以重新提交自己的代码了。

提交之后，应该可以看到网址出现：https://locust2020-pro.herokuapp.com/

点击看看会发生什么。没错，hello world就出现了。

#### Staging/Production 工作流

现在修改一点内容，然后只push到staging上。修改app.py内容如下：

```Python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
```

然后本地启动看看效果。

```Shell
python app.py
```

浏览器打开：http://localhost:5000/mike

现在可以将对staging的修改提交到远程。add，commit，push一波三连。

```Shell
git add -A
git commit -m 'staging'
git push stage master
```

可以看到推到远程之后，远程就会自动构建项目并且发布。访问：https://locust2020-stage.herokuapp.com/mike 
可以看到hello mike。不过用pro的远程就不行了。所以我们可以在stageing环境下build和测试 代码，而当我们非常满意现在的变化时，再把内容推送到production环境下。

```Shell
git push pro master
```

#### config 设置

为app设置不同的config 环境。因为local，staging和production的设置之间会有些不同。比如链接不同的数据库，有不同个的亚马逊云的keys的等。现在设置config file来处理不同的环境。

```Shell
touch config.py
```

有了config文件，创建一个config基类，其他config类会继承它。然后就在不同环境下导入自己需要的即可。config.py的内容如下：

```Python
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
```

现在先看看local设置。为了设置应用的环境变量，我们会使用一个工具：[autoenv](https://github.com/inishchith/autoenv)。该工具能设置每次进入文件夹时就执行的命令。现在先全局安装下它，执行：

```Shell
deactivate
pip install autoenv
touch .env
```

在刚刚创建的.env文件中，添加如下内容：

```Text
source env/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"
```

现在更新自己的.bashrc文件：

```Shell
echo "source `which activate.sh`" >> ~/.bashrc
source ~/.bashrc
```

现在回到上一层文件夹，再回来：

```Shell
cd ..
cd flask-by-example
```

可以看到autoenv会自动地执行命令问是否需要进入env环境。virtual environment 自动启动了，APP_SETTINGS变量也被声明了。

我们可以对Heroku做相似的设置。

```Shell
heroku config:set APP_SETTINGS=config.StagingConfig --remote stage
heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro
```

现在确保app.py使用了正确的环境设置：

```Python
import os
from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
```

现在commit病push到staging和production。

```Shell
git add -A
git commit -m 'app setting'
git push stage master
git push pro master
```

现在可以运行app，看看各个环境都是导入什么config settings的：

```Shell
python app.py
```
本地输出：config.DevelopmentConfig

```Shell
heroku run python app.py --app locust2020-stage
```
stage输出：Running python app.py on wordcount-stage... up, run.7699
config.StagingConfig

```Shell
heroku run python app.py --app locust2020-pro
```

pro输出：Running python app.py on wordcount-pro... up, run.8934
config.ProductionConfig

### Part2 ：Setting up Postgres, SQLAlchemy, and Alembic

这部分开始设置一个 Postgres 数据库来存储结果。也使用SQLAlchemy，一个ORM（Object Relational Mapper）。并使用Alembic来处理数据库迁移。目的是构建一个Flask app 能计算给定的文本的词频。Postgres 数据库这里暂时有点问题！！！！

#### 安装

在本地安装Postgres。如果前面执行了Heroku的示例，这里应该已经装了。

```Shell
psql --version
```

接下来启动postgres。简单补充一点postgre的内容，：

参考了[01-PostgreSQL的基本使用（Ubuntu18.04）](https://www.jianshu.com/p/db68a87fbb0e)：

```Shell
/etc/init.d/postgresql start
```

在服务端安装完成后，需要使用SupersetUser登录，超级用户默认为postgres。接下来要创建一个用户。

```Shell
#进入一个模板，这时候只用输入用户密码
sudo su postgres -c psql template1
#修改postgrse用户的密码，这里为了方便记忆，我用了和系统用户一样密码
ALTER USER postgres WITH PASSWORD ' <***password***> ';
```

接下来输入一下内容可以退出PostgreSQL提示符：

```psql
\q
```

这将使您回到postgres Linux命令提示符。回到最初状态的话，可以重启terminal，也可以执行：

```Shell
su owen
```

这样就回到base环境了。参考另一个文档：[如何在Ubuntu 18.04上安装和使用PostgreSQL](https://www.howtoing.com/how-to-install-and-use-postgresql-on-ubuntu-18-04)

使用以下命令可以在终端切换到服务器上的postgres帐户：

```Shell
sudo -i -u postgres
```

然后执行psql可以登录到PostgreSQL提示符中，从这里您可以立即与数据库管理系统进行交互。

```Shell
psql
\q
```

如果要创建一个用户角色，比如我是owen，创建一个owen的role。在切换到服务器上的postgres帐户的终端里：

```Shell
createuser --interactive
```

然后输入owen，然后敲y即可。

回到本项目。创建数据库，首先进入到postgre的环境：

```Shell
sudo -i -u postgres
psql
```

然后创建数据库：

```postgre
create database wordcount_dev;
```

然后回到项目根目录：

```Shell
cd
cd Documents/Code/flask-by-example
```

在env环境下安装Psycopg2，Flask-SQLAlchemy， Flask-Migrate

```Shell
pip install psycopg2
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install Flask-Script
pip freeze > requirements.txt
```

#### 更新配置

为了使用数据库，修改config.py文件，补充SQLALCHEMY_DATABASE_URI：

```Python
import os

class Config(object):
    ...
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
```

在终端增加DATABASE_URL变量：

```Shell
export DATABASE_URL="postgresql://localhost/wordcount_dev"
```

然后把这一行也放到.env文件里，这样下次进来env环境，该变量DATABASE_URL就会自动导入终端了。

现在修改app.py ：

```Python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
```

#### Data model

现在开始写 models.py 文件。

```Shell
touch models.py 
```

```Python
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
```

现在可以创建一个table来存储word counts的结果。首先导入app.py文件中创建的数据库链接，以及从SQLAlchemy’s PostgreSQL dialects的JSON。然后创建一个Result() 类来对应result表。

创建一个manage.py文件来管理数据库迁移。

```Shell
touch manage.py 
```

```Python
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
```

接下来初始化Alembic：

```Shell
python manage.py db init
```

运行完上述数据库初始化代码后，会有一个新建的migrations文件夹。这里有一些Alembic必须的设置来运行数据库迁移。里面有个versions文件文件，它里面用来放置迁移脚本。

现在通过下面命令来执行迁移命令：

```Shell
python manage.py db migrate
```