绝大多数标本馆都会使用 excel 表格作为存储、分享数据的媒介，也会使用文件夹存放或整理标本的照片。对于很多缺乏技术支持的标本馆，这些手段可能是管理标本数据唯一有效的方法；而对于一些大中型植物标本馆，这些形态也是数据生产过程中非常重要的中间形式。处理它们经常会耗费大量的人力资源，单纯的人工往往也很难达到理想的效果。标本馆助手（iHerbarium）就是为了解决这一问题而产生的。

iHerbarium 是一款 Windows 桌面小程序，主要基于 [ipybd 框架](https://github.com/leisux/ipybd)开发，能够辅助标本馆提高标本处理流程中诸如标签打印、格式转换、照片命名、数据清洗等工作的效率和品质。

### 一、照片条形码识别并命名

- 程序可以识别各种尺寸图片上的条形码内容，并以此命名图片文件名，条形码识别默认基于 zbar ，必要时可以自动切换为 pyzxing （需自行安装JDK支持），**首次使用识别功能时，需联网下载相关文件，否则无法正常使用**，为了保证结果能够达到预期，我们不建议植物标本上贴附多个条形码，对于一些质量不佳的照片，识别引导时可通过手动录入更大的切片像素提高条码的识别率。
- 同一个文件夹内如果同时存在与 jpg 同名的 DNG/nef 原片，程序会同时改写源文件的文件名；

### 二、照片提取

- 可以根据给定的 excel 文件名列表，从目标文件夹内（可嵌套）批量提取相应文件名的照片。
- 使用 DNG 保存的原片，程序可直接提取 DNG 中用于预览的 jpg 照片。

### 三、标签打印

- 生成标签：可以输出带有条形码的采集标签，也可以输出不带有条形码的普通采集标签，标签内容基于 excel 数据表生成，excel 格式可以按照压缩包内推荐的四种模板整理，也可以按照程序引导，将你私有的数据格式转换成符合标签输出要求的数据表格式。
- 复份扩增：标签输出能够按照一条数据生成多份复份标签（每份扩增 n 份或者按照 excel 内每条数据指定的复份数量进行扩增），如果存在标签扩增，程序最终会额外输出一份与最终标签一一对应的新数据表。
- 条码编排：每个标签上的条形码编号可以在 excel 内预先指定，也可以让程序按照一定的规则从某一起始编号按序编排（不重复），程序会以 Code128 将其转换成条形码。
- 使用教程：如果你对程序引导仍然感到陌生，请[请戳这里](https://mp.weixin.qq.com/s/h4G32OU6Sh8ko1t6_f87FA)查看细致的标签打印教程。
- 标签定制：若需要定制标签模板，可提交详细的 issue 或者 e-mail（xu_zhoufeng@126.com）。

### 四、数据表转换

- iherbarium 支持绝大多数二维 excel 数据表转化为 CVH、BioGrid、DarwinCore、标签打印规范的数据表，这在应对多种来源的数据表时非常有用。
- iHerbarium 的表格转换能力来自于 ipybd，有关数据表格式转换的引导操作，请见 [ipybd 标准字段名映射]([leisux/ipybd: Powerful Data Cleaner For Biodiversity (github.com)](https://github.com/leisux/ipybd#43-标准字段名映射引导))的介绍。
- 我们在文件中推荐了一种 Excel 收集各类植物标本采集数据的规范，它可以用于标本馆对外的数据规范要求，配合软件使用可大幅简化数据管理工作。

### 五、使用

- Windows 用户：iHerbarium 二进制包是由 Python 脚本经 Pyinstaller 编译输出，可直接下载 zip 文件解压后运行 iherbarium.exe 即可。
- 其他/DIY用户：可自行下载 source 文件夹，配置环境运行。

### 六、引用

如果你需要将其发表在文献中，你可以参考以下两种形式：

1. *徐洲锋. 标本馆助手, V2.0[CP]. 广州: 中国科学院华南植物园, 2023. https://github.com/leisux/iherbarium*

2. *Xu Zhoufeng(2022). iHerbarium(Version 1.9)[Software]. Guangzhou: South China Botanical Garden, CAS. https://github.com/leisux/iherbarium*

### 七、支持

开发和维护工具不易，如果认为这款软件值得你支持一下，可以使用微信扫描下面的 QR 码～

<img src="./support.png" width="300" />

