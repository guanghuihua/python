# 超文本标记语言

## 什么是超文本标记语言

Hyper Text Makeup Language  ->HTML
它包括一系列标签．通过这些标签可以将网络上的文档格式统一，使分散的Internet资源连接为一个逻辑整体  
使用HTML，将所需要表达的信息按某种规则写成HTML文件，
通过专用的浏览器来识别，并将这些HTML文件“翻译”成可以识别的信息，即现在所见到的网页
浏览器<-->服务器

### 什么是http协议（超文本传输协议）

超文本传输协议（Hypertext Transfer Protocol，HTTP）是一个简单的请求-响应协议，它通常运行在TCP之上。它指定了客户端可能发送给服务器什么样的消息以及得到什么样的响应。  
HTTP协议是Hyper Text Transfer Protocol（超文本传输协议）的缩写,是用于从**万维网（WWW:World Wide Web ）服务器**传输**超文本**到**本地浏览器**的传送协议。
HTTP是一个基于TCP/IP通信协议来传递数据（HTML 文件, 图片文件, 查询结果等）。
浏览器显示的内容都有 `HTML`、`XML`、`GIF`、`Flash` 等，浏览器是通过 MIME Type 区分它们，决定用什么内容什么形式来显示。  
注释：MIME Type 是该资源的媒体类型，MIME Type 不是个人指定的，是经过互联网（IETF）组织协商，以 RFC（是一系列以编号排定的文件，几乎所有的互联网标准都有收录在其中） 的形式作为建议的标准发布在网上的，大多数的 Web 服务器和用户代理都会支持这个规范   
**媒体类型通常通过 HTTP 协议，由 Web 服务器告知浏览器的，更准确地说，是通过 Content-Type 来表示的。例如：Content-Type：text/HTML。**  

### http工作原理

HTTP协议工作于客户端-服务端架构上。  
浏览器作为**HTTP客户端**通过**URL**向**HTTP服务端**即**WEB服务器**发送所有请求。  
Web服务器有：Apache服务器，IIS服务器（Internet Information Services）等。  
 
典型的HTTP事务处理有如下的过程：
（1）客户与服务器建立连接；
（2）客户向服务器提出请求；
（3）服务器接受请求，并根据请求返回相应的文件作为应答；
（4）客户与服务器关闭连接。

### http通信协议流程

Web Browser  <--> HTTP server <--> CGI program <--> Database


## 记录一下在vscode上面html的环境配置

首先创建一个`.html`文件
可以快捷创建,首先使用一个英文`!`然后出现选项之后回车即可，
实际上出现问题，没有办法进行快捷创建，如何改进，
在vscode中选择右下角，有一个`Select Language Mode`来选择语言，换成html即可快捷创建  
又出现问题，不知道怎么让html文件直接在浏览器中显示，解决办法是
在vscode中`ctrl+shift+p`快捷键，进入命令面板，然后找到`live sever`点击，即可看到右下角出现`Go Live`点击即可使用浏览器查看你编辑的html文件

