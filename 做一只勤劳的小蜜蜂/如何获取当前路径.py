import os  #导入os模块
#方法一
os.getcwd()
#方法二
os.path.abspath("-")
# >>> 'D:\\Github\\Python-code\\-'
os.path.abspath(",")
# >>> 'D:\\Github\\Python-code\\,'
os.path.abspath()
# >>> TypeError: abspath() missing 1 required positional argument: 'path'
#----------------------------------------------------------------
# 由上面可知，使用os.path.abspath()必须传入参数，使用os.getcwd()更方便