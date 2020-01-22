# honeybee   
（蜜蜂）接口测试框架  


# 一、思路         
1、采用requests+unittest+ddt+PyMySQL+BeautifulReport+demjson+loguru+PyYAML+pytest+pytest-html+allure-pytest+pytest-rerunfailures+pytest-sugar+pytest-timeout  
2、requests是发起HTTP请求的第三方库  
3、unittest是Python自带的单元测试工具  
4、ddt是数据驱动的第三方库  
5、PyMySQL是连接MySQL的第三方库  
6、BeautifulReport是生成html测试报告的第三方库  
7、demjson是解析json的第三方库  
8、loguru是记录日志的第三方库  
9、PyYAML是读写yaml文件的第三方库  
10、pytest是单元测试的第三方库  
11、pytest-html是生成html测试报告的插件  
12、allure-pytest是生成allure测试报告的插件  
13、pytest-rerunfailures是失败重跑的插件   
14、pytest-sugar是显示进度的插件  
15、pytest-timeout是设置超时时间的插件  


# 二、目录结构    
1、case是测试用例包              
2、log是日志目录         
3、report是测试报告的目录       
4、resource是yaml文件的目录      
5、setting是工程的配置文件包            
6、tool是常用方法的封装包         


# 三、yaml文件说明  
1、字段（命名和格式不可修改，顺序可以修改）  
case_name: 用例名称   
mysql: MySQL查询语句   
request_mode: 请求方式  
api: 接口    
data: 请求体，缩进字典格式或者json格式     
headers: 请求头，缩进字典格式或者json格式    
query_string: 请求参数，缩进字典格式或者json格式    
expected_code: 预期的响应代码    
expected_result: 预期的响应结果，-列表格式     
regular: 正则，缩进字典格式  
>>variable:变量名，-列表格式  
>>expression:表达式，-列表格式  

2、参数化  
正则表达式提取的结果用${变量名}表示，一条用例里面可以有多个    
MySQL返回的结果用{__SQL}表示，一条用例里面可以有多个   
随机数字用{__RN位数}，一条用例里面可以有多个   
随机英文字母用{__RL位数}，一条用例里面可以有多个  
以上4种类型在一条用例里面可以混合使用  
${变量名}的作用域是全局的，其它3种的作用域仅限该条用例  
