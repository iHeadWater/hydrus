# 如何发布自己的python工具

之前要使用别人的python包时，使用conda或者pip就能轻松的安装好，不需要从源码开始，很方便。然后写自己的python包时直接调用它们就行了，对于自己构建的python模块，也是直接调用就行。但是，如果你想要让自己的程序让程序之外整个系统上都能随意使用时，当你想让别人也能轻松地使用你的module时，这就不足够了。前者通常要求我们向module增加一个setup.py文件，后者则需要我们将程序打包发送到PyPI（这样别人就能pip安装了）。

这里以[realpython 的 reader](https://realpython.com/pypi-publish-python-package/#a-small-python-package)为例，主要参考[How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/#using-the-real-python-reader)，记录下具体执行程序发布时的要点。

## 1. 布局项目

本节将描述一个小的Python包，我们将用它作为一个例子，可以发布到PyPI上。 

这个包叫做 reader（已经从[GitHub仓库](https://github.com/realpython/reader)上下载下来并放到本文件夹下了），是一个可以用来下载和阅读 Real Python 文章的应用程序。

首先，看一下目录结构。该软件包在一个被命名为reader的目录中。

```File system
reader/
│
├── reader/
│   ├── config.txt
│   ├── feed.py
│   ├── __init__.py
│   ├── __main__.py
│   └── viewer.py
│
├── tests/
│   ├── test_feed.py
│   └── test_viewer.py
│
├── MANIFEST.in
├── README.md
└── setup.py
```

该软件包的源代码和一个配置文件都在一个reader子目录中。在tests子目录下有一些测试文件。

reader 是一个非常基本的 [web feed](https://en.wikipedia.org/wiki/Web_feed) 阅读器，可以从 [Real Python feed](https://realpython.com/contact/#rss-atom-feed) 下载最新的 Real Python 文章。

简单补充下调用包的不同方式：当项目越来越复杂时，一个挑战是向用户传达如何使用我们的项目。由于包由四个不同的源代码文件（reader/reader文件夹下）组成，用户如何知道要调用哪个文件来运行阅读器呢？

python解释器程序有一个-m选项，允许我们指定一个模块名称而不是文件名称。例如，如果有一个叫做hello.py的脚本，下面两个命令是等价的。

```Shell
$ python hello.py
Hi there!

$ python -m hello
Hi there!
```

后者的一个好处是，它允许我们调用Python中内置的模块。一个例子是调用 antigravity（命令行输入下面的命令，会弹出一个网页）：

```Shell
python -m antigravity
```

使用-m的另一个好处是，它既适用于包，也适用于模块。

由于 reader 是一个包，这个名字只指一个目录。Python 是如何决定在这个目录中运行哪段代码的呢？答案是它会寻找一个名为 \_\_main\_\_.py 的文件。如果这样的文件存在，它就被执行。如果 \_\_main\_\_.py 不存在，就会打印出一条错误信息。比如命令行执行下面的语句就会报错，因为数学标准库没有定义一个 \_\_main\_\_.py 文件。


```Shell
python -m math
```

如果我们正在创建一个应该被执行的包，那就包含一个 \_\_main\_\_.py 文件。稍后介绍如何为包创建入口点，这些入口点将像普通的程序一样行事。

## 2. 准备包

现在我们已经有了一个想发布的包。在将软件包上传到PyPI之前，哪些步骤是必要的？

### 起名字

第一步，也可能是最难的一步，是为包起一个好名字。PyPI上的所有软件包都需要有独特的名字。PyPI上已经有超过150,000个软件包，最喜欢的名字很可能已经被占用了。

所以可能需要集思广益，做一些研究来找到完美的名字。使用[PyPI搜索](https://pypi.org/search/)来检查一个名字是否已经被占用。

为了使reader包在PyPI上更容易找到，realpython给它起了一个更具描述性的名字，叫realpython-reader。同样的名字将被用于使用pip来安装该包。

尽管使用realpython-reader作为PyPI的名称，但当它被导入时，该包仍被称为reader。也就是说，可以在PyPI上和导入时为包使用不同的名字。然而，如果使用相同的名字或非常相似的名字，那么对用户来说就会更容易。

### 配置软件包

接下来就是配置软件包。

setup.py文件是pip会在给定文件夹中寻找的文件。它使用能用来执行打包的setuptools工具。它其中内容包括包的名称，包的简短描述以及作者的信息，还有python版本等。

setup.py文件应该放在软件包的顶部文件夹中。reader的setup.py看起来像这样。

```Python
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="realpython-reader",
    version="1.0.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Real Python",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
```

这里只介绍setuptools中的一些可用选项。[setuotppls文档](https://setuptools.pypa.io/en/latest/setuptools.html#basic-use)中对所有的细节都做了很好的说明。

在调用setup()时，以下参数是100%必要的。

- name：软件包的名称，它将出现在PyPI上。
- version：软件包的当前版本
- packages：包含源代码的包和子包。

后面会讨论更多关于版本的问题。

packages参数接收一个软件包的列表。在我们的例子中，只有一个包：reader。

还需要指定任何子包。在更复杂的项目中，可能有许多包需要列出。为了简化这项工作，setuptools包括find_packages()，它能很好地发现所有的子包。可以在reader项目中使用 find_packages() ，如下所示。

```Python
from setuptools import find_packages, setup

setup(
    ...
    packages=find_packages(exclude=("tests",)),
    ...
)
```

虽然只需要名字、版本和软件包，但如果添加一些更多的信息，软件包在PyPI上会变得更容易找到。请看一下PyPI上的[realpython-reader页面](https://pypi.org/project/realpython-reader/)，并将其与上面的setup.py进行比较。所有的信息都来自 setup.py 和 README.md。

setup()的最后两个参数值得特别一提。

- install_requires 用于列出软件包对第三方库的任何依赖性。reader依赖于feedparser和html2text，所以它们应该被列在这里。
- entry_points用于创建调用软件包中某个函数的脚本。在我们的例子中，创建了一个新的脚本realpython，在 reader/\_\_main\_\_.py 文件中调用 main()。

关于更多典型的setup.py文件的例子，请看 GitHub 上 Kenneth Reitz 的 [setup.py 仓库](https://github.com/kennethreitz/setup.py)。

### 写好文档

在向世界发布软件包之前，应该添加一些文档。文档可以小到一个简单的README文件，也可以大到一个完整的网页，包括教程、实例库和API参考。

至少，应该在项目中包含一个README文件。一个好的README应该快速描述项目，以及告诉用户如何安装和使用软件包。通常情况下，要把README作为setup()的long_description参数。这将在PyPI上显示README。

传统上，PyPI使用reStructuredText来编写软件包文档。不过自2018年3月以来，Markdown也被支持。

在PyPI之外，Markdown比reStructuredText得到更广泛的支持。如果不需要reStructuredText的任何特殊功能，最好将README保持在Markdown格式。注意，应该使用setup()参数long_description_content_type来告诉PyPI正在使用哪种格式。有效值是text/markdown、text/x-rst和text/lain。

对于更大的项目，可能想提供更多的文档，而不是装在一个文件里。在这种情况下，可以使用GitHub或Read the Docs这样的网站，并使用url参数链接到文档。在上面的setup.py例子中，url被用来链接到读者的GitHub仓库。

### 版本管理

软件包需要有一个版本，而PyPI只允许对一个软件包的特定版本进行一次上传。换句话说，如果想在PyPI上更新软件包，需要先增加版本号。这是一件好事，因为它保证了可重复性：两个拥有相同版本软件包的系统应该表现相同。

有许多不同的方案可以用于版本号。对于Python项目，[PEP 440](https://www.python.org/dev/peps/pep-0440/)给出了一些建议。然而，为了灵活起见，该PEP很复杂。对于一个简单的项目，坚持使用一个简单的版本管理方案较好。

[语义版本管理](https://semver.org/)是一个可以使用的好的默认方案。版本号是由三个数字组成的，例如0.1.2。这些组件被称为MAJOR、MINOR和PATCH，并且对于何时增加每个组件有简单的规则。

- 当做不兼容的API修改时，增加MAJOR版本。
- 当以向后兼容的方式增加功能时，增加 MINOR 版本。
- 当进行向后兼容的错误修复时，增加 PATCH 版本。

可能需要在项目中不同文件中指定版本。在 reader 项目中，我们在 setup.py 和 reader/\_\_init\_\_.py 中都指定了版本。为了确保版本号保持一致，可以使用一个叫做[Bumpversion](https://pypi.org/project/bumpversion/)的工具。

### 添加文件到软件包

有时，包中会有一些不是源代码文件的文件。例如，数据文件、二进制文件、文档，以及我们在这个项目中的配置文件。

为了告诉 setup() 包含这些文件，可以使用清单文件。对于许多项目，不需要担心清单，因为 setup() 创建的清单包括所有代码文件和 README 文件。

如果需要更改清单，可以创建一个清单模板，其名称必须为 MANIFEST.in。该文件规定了应包括和排除的内容的规则，例如：

```Text
include reader/*.txt
```

这个例子将包括reader目录下的所有.txt文件，这实际上就是配置文件。关于可用规则的列表，请参见[文档](https://docs.python.org/distutils/commandref.html#creating-a-source-distribution-the-sdist-command)。

除了创建MANIFEST.in之外，还需要告诉setup()来复制这些非代码文件。这可以通过将include_package_data参数设置为True来完成:

```Python
setup(
    ...
    include_package_data=True,
    ...
)
```

include_package_data参数控制在软件包安装时是否复制非代码文件。

## 3. 发布到PyPI

软件包终于准备好与电脑外的世界见面了！

如果你在PyPI上还没有一个账户，现在是时候创建一个了：在[PyPI](https://pypi.org/account/register/)上注册你的账户。与此同时，你也应该在[TestPyPI](https://test.pypi.org/manage/projects/)上注册一个账户。TestPyPI非常有用，因为你可以尝试发布软件包的所有步骤，如果你搞砸了，没有任何后果。

要上传软件包到PyPI，将使用一个叫Twine的工具。你可以像往常一样用Pip安装 Twine。本repo下我们使用conda安装了： conda install -c conda-forge twine

### 构建包

PyPI上的软件包不是以普通的源代码形式发布的。相反，它们被包装成发行包。分发包最常见的格式是源代码档案和Python轮子（下一节有介绍）。

一个源码档案由你的源码和任何支持文件组成，被包装成一个tar文件。同样地，一个轮子基本上是一个包含你的代码的 zip 档案。与源码归档不同的是，轮子包括任何可以使用的扩展。

要为软件包创建一个源文件和一个轮子，可以运行以下命令。

```Shell
cd 7-python-project/3-python-package/reader
python setup.py sdist bdist_wheel
```

这将在新创建的dist目录下创建两个文件，一个源文件和一个轮子。

```File system
reader/
│
└── dist/
    ├── realpython_reader-1.0.0-py3-none-any.whl
    └── realpython-reader-1.0.0.tar.gz
```

注意：在Windows上，源存档默认为一个.zip文件。你可以用 --format 命令行选项来选择源存档的格式。

可能想知道setup.py如何知道如何处理sdist和bdist_wheel参数。如果回顾一下 setup.py 是如何实现的，没有提到 sdist、bdist_wheel 或任何其他命令行参数。

所有的命令行参数都在上游的distutils标准库中实现。你可以通过添加 --help-commands 选项列出所有可用的参数。

```Shell
python setup.py --help-commands
```

如果想了解某个特定命令的信息，可以运行比如python setup.py sdist --help。

### 测试包

首先，应该检查新建立的发行包是否包含期望的文件。在Linux和macOS上，应该能够列出tar源存档的内容：tar tzf realpython-reader-1.0.0.tar.gz

在 Windows 上，可以使用 [7-zip](https://www.7-zip.org/) 这样的工具来查看相应的 zip 文件。

应该看到所有的源代码都被列出来了，还有一些新创建的文件，这些文件包含了在setup.py中提供的信息。特别是，要确保所有的子包和支持文件都包括在内。

也可以像解压缩文件一样解开轮子内部看看。如果源文件包含期望的文件，轮子也应该是好的。

新版本的Twine（1.12.0及以上）也可以检查软件包描述是否能在PyPI上正常呈现。可以对在dist中创建的文件运行twine检查。

```Shell
twine check dist/*
```

虽然它不会抓住你可能遇到的所有问题，但它会让你知道你是否使用了错误的内容类型。

### 上传包

现在你已经准备好将你的软件包上传到PyPI。为此，将再次使用Twine工具，告诉它上传你所构建的发行包。首先，应该上传到TestPyPI，以确保一切按预期进行。

```Shell
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Twine会要求你提供你的用户名和密码。

注意：如果按照教程以reader包为例，命令可能会失败，提示你不允许上传到realpython-reader项目。

你可以把setup.py中的名字改成唯一的，比如test-your-username。然后再次构建项目，将新构建的文件上传到TestPyPI。

如果上传成功，你可以迅速前往TestPyPI，向下滚动，看看你的项目正自豪地显示在新发布的版本中 点击你的包，确保一切看起来都很好。

如果你一直在使用reader包，那么本教程到此结束! 虽然你可以尽情地玩TestPyPI，但你不应该为了测试而把假包上传到PyPI。

然而，如果你有自己的软件包要发布，那么这一刻终于到来了！你可以在PyPI上发布自己的软件包。随着所有准备工作的完成，这最后一步很短。

```Shell
twine upload dist/*
```

根据要求提供你的用户名和密码就行了。

前往PyPI并查找你的软件包。你可以通过搜索、查看你的项目页面，或者直接进入你的项目的URL：pypi.org/project/your-package-name/，找到它。

恭喜你! 你的软件包已经在PyPI上发布了!

### pip安装包

花点时间沐浴在PyPI网页的蓝色光芒中，（当然）可以向你的朋友们炫耀一下。

然后再打开一个终端，可以用pip来安装它。
