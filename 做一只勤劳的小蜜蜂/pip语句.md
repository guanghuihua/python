# 关于pip 来安装包的一些常见操作   

[网址]( https://blog.csdn.net/peiwang245/article/details/98317863)

1. 查看pip  
（1）直接在cmd窗口中输入`pip`命令，会显示pip所有的参数使用方法；  
（2）输入pip提示Did not provide a command，则有两种可能，  
第一是没有配置环境变量，  
第二就是其他应用程序也存在pip的环境变量  

2. where pip  
这个命令不是pip的命令啊，用这个命令主要是如果上一步，环境变量配置没问题，  
就是第二种啦，这时候就可以用where pip来查询啦,如果有两个pip，所以直接输入pip系统无法识别是其中某个。怎么可以快速解决呢？输入pip.exe即可，当然也可以去到pip.exe的路径下，输入pip也行  

3. pip版本  
用`pip -V`可以查看版本，是大写的V：  
pip版本升级命令：`pip install --upgrade pip`
升级命令用的不多，一般如果是python自带的pip版本，可能会比较低，使用pip安装第三方库就会出现报错，但是报错的最后会给出这个升级命令，还是比较贴心的。  

4. pip list查看已经安装的第三方库  

 `pip list --outdated`可以查看有新版本的第三方库，可显示现在安装的版本，以及最新的版本  

5. pip安装第三方库 
    
命令：`pip install  库名`    

pip安装会拉取最新版本安装，想安装任意版本则可加上版本号  
命令：`pip install 库名=版本号`  

1. 查看安装  
`pip show 库名`  

2. 卸载第三方库  
`pip uninstall 库名`  

3. 卸载Pip  
`python -m pip uninstall pip`  
