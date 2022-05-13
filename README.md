绝大多数标本馆都会使用 excel 数据表格作为存储、分享数据的媒介，也会使用文件夹存放或整理标本的照片。对于很多缺乏技术支持的标本馆，这些手段可能是他们管理标本数据唯一有效的方法，而对于一些中大型植物标本馆，这些形式也是数据生产过程中非常重要的初始或中间形态。标本馆助手（iHerbarium）是专为标本馆开发的一款桌面小程序，它基于 [ipybd 框架](https://github.com/leisux/ipybd)，可以大幅提高标本处理流程中诸如标签打印、数据整理、数据转化等工作的效率和品质。


### 一、照片条形码识别并命名

- 可以识别图片内的条形码，并以此命名图片，识别默认基于 zbar ，也可自行安装 JDK8 后联合 pyzxing 扩大支持的编码类型；这一功能特别适合被用于已贴附条形码的植物标本照片进行自动命名。
- 使用 Nikon 拍摄的 nef 原片，和相应的 jpg 在同一文件见内，程序会同时以条形码命名 nef 文件；这对于使用 RAW 格式保存标本原片的标本馆非常有用。

### 二、照片提取

- 可以根据给定的 excel 文件名列表，从目标文件夹内（可嵌套）批量提取相应文件名的照片。

### 三、标签打印

- 生成标签：可以输出带有条形码的采集标签，也可以输出不带有条形码的普通采集标签，标签内容基于 excel 数据表生成，excel 格式可以按照压缩包内推荐的四种模板整理，也可以按照程序引导，将你私有的数据格式转换成符合标签输出要求的数据表格式。
- 复份扩增：标签输出能够按照一条数据生成多份复份标签（每份扩增 n 份或者按照 excel 内每条数据指定的复份数量进行扩增），如果存在标签扩增，程序最终会额外输出一份与最终标签一一对应的新数据表。
- 条码编排：每个标签上的条形码编号可以在 excel 内预先指定，也可以让程序按照一定的规则从某一起始编号按序编排（不重复），程序会以 Code128 将其转换成条形码。
- 使用教程：如果你对程序引导仍然感到陌生，请[请戳这里](https://mp.weixin.qq.com/s/h4G32OU6Sh8ko1t6_f87FA)查看细致的标签打印教程。
- 标签定制：若需要定制标签模板，可提交详细的 issue 或者 e-mail。
- 

### 四、数据表转换

- 基于 ipybd，iherbarium 支持绝大多数二维 excel 数据表转化为 CVH、Kingdonia、DarwinCore、标签打印规范的数据表，这在应对多种来源的数据表时非常有用。

### 五、使用

- Windows 用户：iHerbarium 二进制包是由 Python 脚本经 Pyinstaller 编译输出，因此可直接下载 Realse 版本，解压 zip 文件，后进入 iherbarium 文件夹，运行 iherbarium.exe 即可。
- 其他/DIY用户：可自行下载脚本，配置环境运行。

### 六、引用

如果你需要将其发表在文献中，请使用以下参考格式：

**中文：**
*徐洲锋. 标本馆助手, V1.9[CP]. 广州: 中国科学院华南植物园, 2022.https://github.com/leisux/iherbarium*

**English：**
*Xu Zhoufeng(2022). iHerbarium(Version 1.9)[Software]. Guangzhou: South China Botanical Garden, CAS. https://github.com/leisux/iherbarium*

### 七、支持

如果你觉得这款软件值得请一杯咖啡，请微信扫码：

<span style="text-align:center">
  <img src="https://tva1.sinaimg.cn/large/e6c9d24ely1h26txtps4uj20na0mq0v4.jpg" width="250"/>
</span>

