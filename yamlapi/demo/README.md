# yamlapi  
yamlapi接口测试框架  

支持unittest与pytest两种运行模式  
yamlapi即为yaml文件+api测试的缩写  
可看作是一个脚手架工具  
可快速生成项目的各个目录与文件  
只需维护一份或者多份yaml文件即可  

`pip install yamlapi`  
安装  

`yamlapi -h（或yamlapi --help）`  
查看参数信息  

`yamlapi -v（或yamlapi --version）`  
查看版本号  

`pip install -U yamlapi`  
安装最新版  

`yamlapi --p=项目名称`  
创建项目  
例如在某个路径下执行命令：  
`yamlapi --p=demo_project`  

`pip uninstall yamlapi`  
卸载  


# 一、思路         
1、采用requests+unittest+ddt+PyMySQL+DBUtils+BeautifulReport+demjson+loguru+PyYAML+ruamel.yaml+pytest+pytest-html+allure-pytest+pytest-reportlog+pytest-rerunfailures+pytest-sugar+pytest-timeout+pytest-parallel  
2、requests是发起HTTP请求的第三方库  
3、unittest是Python自带的单元测试工具  
4、ddt是数据驱动的第三方库  
5、PyMySQL是连接MySQL的第三方库  
6、DBUtils是数据库连接池的第三方库  
7、BeautifulReport是生成html测试报告的第三方库  
8、demjson是解析非标格式json的第三方库  
9、loguru是记录日志的第三方库  
10、PyYAML与ruamel.yaml是读写yaml文件的第三方库  
11、pytest是单元测试的第三方库  
12、pytest-html是生成html测试报告的插件  
13、allure-pytest是生成allure测试报告的插件  
14、pytest-reportlog是替换--resultlog选项的插件  
15、pytest-rerunfailures是失败重跑的插件  
16、pytest-sugar是显示进度的插件  
17、pytest-timeout是设置超时时间的插件  
18、pytest-parallel是多线程的插件   


# 二、目录结构    
1、case是测试用例包              
2、report_log是测试报告和日志的目录       
3、resource是yaml文件的目录      
4、setting是工程的配置文件包            
5、tool是常用方法的封装包  
6、.gitignore是.ignore插件需要排除的文件  
7、conftest.py是全局钩子文件  
8、Jenkinsfile是Jenkins Pipeline文件  
9、pytest.ini是pytest的配置文件  
10、requirements.txt是第三方依赖库  


# 三、yaml文件说明  
```yaml
- case_name: 用例名称
  step:
    - step_name: 步骤名称
      mysql:
        -
        -
        -
      request_mode: POST
      api: /api/test
      body:
        {"key_1":"value_1","key_2":"value_2"}
      headers:
        {"Content-Type":"application/json"}
      expected_time: 3
      expected_code: 200
      expected_result:
        {"code":1,"message":"成功"}
      regular:
        variable:
          - name_1
          - name_2
        expression:
          - '"response_1":"(.+?)"'
          - '"response_2":"(.+?)"'
```
1、外层有2个字段，内层有13个字段  
命名和格式不可修改，顺序可以修改  

| 字段 | 中文名称 | 是否必填 | 格式 | 注解 |
| ---- | ---- | --- | ---- | ---- |
| case_name | 用例名称 | 是 | | |
| step | 步骤 | 是 | -列表格式 | 1条用例可以有1个或者N个步骤，全部的步骤通过，本条用例才算通过 |
| step_name | 步骤名称 | 是 | | |
| mysql | MySQL语句 | 否 | -列表格式| 顺序不可修改 |
| request_mode | 请求方式 | 是 | | |
| api | 接口路径 | 是 | | |
| body | 请求体 | 否 | 缩进字典格式或者json格式 | |
| headers | 请求头 | 否 | 缩进字典格式或者json格式 | |
| query_string | 请求参数 | 否 | 缩进字典格式或者json格式 | |
| expected_time | 预期的响应时间 | 否 | | |
| expected_code | 预期的响应代码 | 是 | | |
| expected_result  | 预期的响应结果 | 是 | -列表格式、缩进字典格式或者json格式 | |
| regular | 正则 | 否 | 缩进字典格式 | |
| variable | 变量名 | 否 | -列表格式 | |
| expression | 表达式 | 否 | -列表格式 | |

mysql： MySQL语句，-列表格式，顺序不可修改，选填  
第一行：mysql[0]  
第二行：mysql[1]  
第三行：mysql[2]  
第一行为增、删、改语句，第二行为查语句，第三行为查语句（数据库双重断言）  
第一行是发起请求之前的动作，没有返回结果  
第二行是发起请求之前的动作，有返回结果，是为了动态传参  
第三行是发起请求之后的动作，有返回结果，但是不可用于动态传参，是为了断言实际的响应结果  
当不需要增删改查和双重断言时，可以不写mysql字段，或者三行都为空  
当只需要增删改时，第一行为增删改语句，第二行为空，第三行为空  
当只需要查时，第一行为空，第二行为查语句，第三行为空  
当只需要双重断言时，第一行为空，第二行为空，第三行为查语句 

2、参数化  
正则表达式提取的结果用${变量名}匹配，一条用例里面可以有多个  
MySQL查询语句返回的结果，即第二行mysql[1]返回的结果，用{__SQL索引}匹配  
即{__SQL0}、{__SQL1}、{__SQL2}、{__SQL3}。。。。。。一条用例里面可以有多个  
随机数字用{__RN位数}，一条用例里面可以有多个  
随机英文字母用{__RL位数}，一条用例里面可以有多个  
随机手机号码用{__MP}，一条用例里面可以有多个  
以上5种类型在一条用例里面可以混合使用  
${变量名}的作用域是全局的，其它4种的作用域仅限该条用例  


# 四、运行  
1、unittest模式：  
python+测试文件名+环境缩写  
python case/demo_test.py dev  
python case/demo_test.py test  
python case/demo_test.py pre  
python case/demo_test.py formal  
2、pytest模式：  
pytest+--cmd=环境缩写  
pytest --cmd=dev  
pytest --cmd=test  
pytest --cmd=pre  
pytest --cmd=formal  


# 五、从阿里云镜像仓库拉取镜像  
`docker pull registry.cn-hangzhou.aliyuncs.com/yangjianliang/yamlapi:[镜像版本号]`  
