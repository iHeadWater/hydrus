# Angular

做一个展示土壤含水量预测的网页，为蝗灾贡献一点力量，所以这里简单记录一下制作过程。先简单学习下wuhan2020的项目，用了一个云服务，略麻烦，所以转到之前“系统开发初步教程”那一套下面去，花一两天时间快速整个网页出来。整个在ubuntu18.04下操作。

## 安装

需要安装的东西包括：nodejs，angularjs等，这些东西的关系可以参考：[Angular2、Ionic、TypeScript、es6的关系？](https://www.jianshu.com/p/27c026734b8d)，如果看不懂，就直接按照下面步骤做即可。

### 安装 nodejs 和 npm 

npm的安装可以参考：[About npm](https://docs.npmjs.com/about-npm/index.html)。

简单介绍下npm。npm是世界上个最大的软件注册中心，全球程序员用它分享package。npm包括三个不同的组成部分：

- the website：在网站上可以寻找自己想要的package
- the Command Line Interface (CLI)：CLI从terminal运行，是使用npm的接口
- the registry：registry是javascript软件的公共数据库

我们通常使用npm来安装各种软件。

使用npm的话，首先，快速注册一个账号。

然后，npm网站推荐使用 node version manager 安装，就按照推荐来做，因为npm官方不建议使用Node来安装，因为node的安装过程将npm安装在具有本地权限的目录中，这在全局运行npm包时可能导致权限错误。  另外，不用nvm的话，安装版本的控制不方便，版本不匹配的话后续的安装可能会失败。也就是说 node version manager 安装是用户级别的安装，方便用，另外版本好管理。

node version manager  在linux下有nvm和n两种，windows下也有nvm，并且nvm用的人更多一些，所以就使用nvm了。

根据[nvm github安装说明](https://github.com/nvm-sh/nvm#install--update-script)，直接执行下面语句即可，

```Shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash
```

如果没有curl，也可以使用wget，二选一即可：

```Shell
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash
```

执行后，重启terminal。可以使用下面语句确认安装成功：

```Shell
command -v nvm
```

输出nvm表示安装成功。注意which nvm是不能运行的，因为nvm不是一个可执行文件，而是一个sourced shell function。

接下来按照[nvm的指示](https://github.com/nvm-sh/nvm#usage)安装node。

```Shell
nvm install node # "node" is an alias for the latest version
```

第一个被安装的node会被当做默认的node使用。新的shells会以默认的node开始。

现在执行：

```Shell
node -v
npm -v
```

可以看到node和npm的版本。

补充：如果你使用了nodejs官方的安装方式，sudo安装了nodejs，想要卸载，可以用如下方式：

参考：[Ubuntu 卸载安装 node 和 npm](https://www.jianshu.com/p/a9212848a34f)：

```Shell
sudo apt-get remove --purge npm
sudo apt-get remove --purge nodejs
sudo apt-get remove --purge nodejs-legacy
sudo apt-get autoremove
```

如果你想卸载nvm，可以参考：[How to uninstall nvm? #298](https://github.com/nvm-sh/nvm/issues/298)

### 安装typescript

在安装angular之前，先安装typescript。根据：[Angular 2 TypeScript 环境配置](https://www.runoob.com/angularjs2/angularjs2-typescript-setup.html)的介绍，TypeScript 是一种由微软开发的自由和开源的编程语言，它是JavaScript的一个超集，扩展了JavaScript的语法。 官方推荐使用TypeScript 来创建 Angular 的应用。

根据typescript官网的提示，执行下面语句即可：

```Shell
npm install -g typescript
```

注意使用npm不要使用sudo，因为用nvm安装的node是一个用户版本的，不是global全局root级的。如果你用sudo安装了npm，用sudo npm就会把东西安装到root的范围下。（后面的安装同理，不要用sudo）

下面语句可以查看typescript版本：

```Shell
tsc --version
```

### 安装 angular

直接根据官网[Setting up the local environment and workspace](https://angular.io/guide/setup-local)来安装：

angular需要的版本是："node":">= 10.13.0","npm":">= 6.11.0","yarn":">= 1.13.0"

```Shell
npm install -g @angular/cli
```

下面语句可以查看自己的angular版本：

```Shell
ng --version
```

### 安装 vscode 

安装vscode比较简单，不赘述了，直接google。

## 开发

开发angular程序需要在Angular 的workspace 环境下开发。所以开发前，要新建一个workspace，比如项目名为 locust2020，terminal 下进入自己想要放置locust2020项目的文件夹，然后执行下面语句。

```Shell
ng new locust2020
```

命令执行过程中按回车默认即可。

最后ng new指令会创建一个新的workspace和一个简单的welcome app，现在来运行它。

```Shell
cd  locust2020
ng serve --open
```

现在可以看到这个欢迎页面了。下面就开始使用angular。可以参考中文文档：[Angular 文档](https://angular.cn/docs)。中文文档上点击任何一段，都会弹出原文。

### 快速上手

那从快速上手开始。官方的实例还给了一个在线的开发环境 [stackblitz](https://angular.cn/generated/live-examples/getting-started-v0/stackblitz.html)，可以使用这个开发环境熟悉下操作。接下来先按照官方文档执行一遍，了解下angular基本内容。

- 模板语法：
    - *ngFor：let product of products 就相当于 for product in products, *ngFor="let product of products; index as productId" 就相当于把productId指定为for i中的i
    - *ngIf；
    - 插值 {{}}；
    - 属性绑定 []，例子中绑定的是products.ts文件内的常量
    - 事件绑定 ()
- 组件：组件在用户界面（也就是 UI）中定义了一些责任区，让你能重用这些 UI 功能集。可以看到src文件夹下的app文件夹下，包括了三个组件，一个是app-root，也就是app开头的几个文件，另外两个就是两个文件夹product-list和top-bar对应的组件。可以看到一个组件包含三个部分，
    - 一个组件类（），它用来处理数据和功能。对应ts文件
    - 一个 HTML 模板，它决定了 UI。对应html文件
    - 组件专属的样式定义了外观和感觉。对应css文件
- 输入：app文件夹下的products.ts中定义了属性值。
- 输出：可以看到ts和html的对应修改是必须的。

### route

接下来了解下route。使用 Angular 路由器来用一些独立页面显示完整的产品详情，这些页面有自己的 URL。Angular 路由器能让你根据用户在应用中的位置向用户显示不同的组件和数据。当用户执行应用任务时，路由器可以从一个视图导航到另一个视图。比如：

- 在地址栏中输入一个 URL，导航到相应的页面。
- 点击页面上的链接，导航到新页面。
- 点击浏览器的后退和前进按钮，在浏览器的历史中前后导航。

app.module.js 就是在这时候发挥作用的。

### 管理数据

服务是 Angular 应用的重要组成部分。在 Angular 中，服务是一个类的实例，它可以借助 Angular 的依赖注入系统来让应用中的任何一个部件都能使用它。关于依赖注入可以看下：[浅谈控制反转与依赖注入](https://zhuanlan.zhihu.com/p/33492169)

服务可以让你在**应用的各个部件之间共享数据**。对于在线商店，购物车服务就是存放购物车的数据和方法的地方。

具体的，就是service.ts文件出现了。

在使用 Angular 的 HTTP 客户端之前，你必须先配置你的应用来使用 HttpClientModule。关于HttpClient 可以参考：[HttpClient](https://angular.cn/guide/http)。

大多数前端应用都需要通过 HTTP 协议与后端服务器通讯。现代浏览器支持使用两种不同的 API 发起 HTTP 请求：XMLHttpRequest 接口和 fetch() API。

Angular 的 HttpClientModule 中注册了在整个应用中使用 HttpClient 服务的单个实例所需的服务提供商。在app.module.ts文件的顶部从 @angular/common/http 包中导入 HttpClientModule 以及其它导入项。

### 表单

Angular 中的表单建立在标准 HTML 表单功能之上，以帮助你创建自定义表单控件和轻松的验证体验。Angular 响应式表单有两个部分：组件中那些用于存储和管理表单的对象，以及表单在模板中的可视化。