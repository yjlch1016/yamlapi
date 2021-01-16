# yamlapi  
yamlapi接口测试框架  

# QQ群  
529063263  

# 工程主页  
readthedocs：  
https://yamlapi-docs.readthedocs.io/zh_CN/latest/  
pypi：  
https://pypi.org/project/yamlapi/  
github：  
https://github.com/yjlch1016/yamlapi  

支持unittest与pytest两种运行模式  
yamlapi即为yaml文件+api测试的缩写  
可看作是一个脚手架工具  
可快速生成项目的各个目录与文件  
支持MySQL、PgSQL与MongoDB数据库的增删改查  
只需维护一份或者多份yaml文件即可  
（或者json文件）  

`pip install yamlapi`  
安装  

`yamlapi -h（或yamlapi --help）`  
查看参数信息  

`yamlapi -v（或yamlapi --version）`  
查看版本号  

`pip install -U yamlapi`  
安装最新版  

`yamlapi create --p=项目名称`  
创建项目  
例如在某个路径下执行命令：  
`yamlapi create --p=demo_project`  

`yamlapi run --c=环境缩写`  
运行项目  
例如在项目的根目录下面执行命令：  
`yamlapi run --c=test`  

`yamlapi clean`  
清理测试报告与日志目录下的所有文件  
类似于`mvn clean`    

`pip uninstall yamlapi`  
卸载  

***
# 一、思路         
1、采用requests+unittest+ddt+PyMySQL+DBUtils+psycopg2-binary+pymongo+BeautifulReport+demjson+loguru+
PyYAML+ruamel.yaml+pytest+pytest-html+allure-pytest+pytest-reportlog+pytest-assume+pytest-rerunfailures+pytest-instafail+pytest-sugar+pytest-timeout+pytest-parallel+tablib  
2、requests是发起HTTP请求的第三方库  
3、unittest是Python自带的单元测试工具  
4、ddt是数据驱动的第三方库  
5、PyMySQL是连接MySQL的第三方库  
6、DBUtils是数据库连接池的第三方库  
7、psycopg2-binary是连接PgSQL的第三方库  
8、pymongo是连接Mongo的第三方库  
9、BeautifulReport是生成html测试报告的第三方库  
10、demjson是解析非标格式json的第三方库  
11、loguru是记录日志的第三方库  
12、PyYAML与ruamel.yaml是读写yaml文件的第三方库  
13、pytest是单元测试的第三方库  
14、pytest-html是生成html测试报告的插件  
15、allure-pytest是生成allure测试报告的插件  
16、pytest-reportlog是替换--resultlog选项的插件  
17、pytest-assume是多重断言的插件  
18、pytest-rerunfailures是失败重跑的插件  
19、pytest-instafail是实时显示错误信息的插件  
20、pytest-sugar是显示进度的插件  
21、pytest-timeout是设置超时时间的插件  
22、pytest-parallel是多线程的插件  
23、tablib是导出多种格式数据的第三方库  

***
# 二、目录结构  
1、case是测试用例包  
2、report_log是测试报告和日志的目录  
3、resource是yaml文件的目录  
4、setting是工程的配置文件包  
5、tool是常用方法的封装包  
6、.dockerignore是在传递给docker引擎时需要忽略掉的文件  
7、.gitignore是.ignore插件需要排除的文件  
8、conftest.py是全局钩子文件  
9、Dockerfile是构建镜像的文件  
10、Jenkinsfile是Jenkins Pipeline文件  
11、pytest.ini是pytest的配置文件  
12、requirements.txt是第三方依赖库  

***
# 三、yaml、json文件说明  
yaml文件  
```yaml
- case_name: 用例名称
  step:
    - step_name: 步骤名称
      mysql:
        -
        -
        -
      pgsql:
        -
        -
        -
      mongo:
        -
        -
        -
      request_mode: POST
      api: /api/test
      file:
        -
        -
        -
      body:
        {"key_1":"value_1","key_2":"value_2"}
      headers:
        {"Content-Type":"application/json"}
      query_string:
        {"key_3":"value_3","key_4":"value_4"}
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
json文件  
```json
[
  {
    "case_name": "用例名称",
    "step": [
      {
        "step_name": "步骤名称",
        "mysql": [],
        "pgsql": [],
        "mongo": [],
        "request_mode": "POST",
        "api": "/api/test",
        "file": [],
        "body": "{\"key_1\":\"value_1\",\"key_2\":\"value_2\"}",
        "headers": "{'Content-Type': 'application/json'}",
        "query_string": "{'key_3':'value_3','key_4':'value_4'}",
        "expected_time": 3,
        "expected_code": 200,
        "expected_result": "{\"code\":1,\"message\":\"成功\"}",
        "regular": {
          "variable": [
            "name_1",
            "name_2"
          ],
          "expression": [
            "\"response_1\":\"(.+?)\"",
            "\"response_2\":\"(.+?)\""
          ]
        }
      }
    ]
  }
]
```
1、外层有2个字段，内层有16个字段  
命名和格式不可修改，顺序可以修改  

| 字段 | 中文名称 | 是否必填 | 格式 | 注解 |
| ---- | ---- | --- | ---- | ---- |
| case_name | 用例名称 | 是 | | |
| step | 步骤 | 是 | -列表格式 | 1条用例可以有1个或者N个步骤，全部的步骤通过，本条用例才算通过 |
| step_name | 步骤名称 | 是 | | |
| mysql | MySQL语句 | 否 | -列表格式 | 顺序不可修改 |
| pgsql | PgSQL语句 | 否 | -列表格式 | 顺序不可修改 |
| mongo | Mongo语句 | 否 | -列表格式 | 顺序不可修改 |
| request_mode | 请求方式 | 是 | | |
| api | 接口路径 | 是 | | |
| file | 文件 | 否 | -列表格式 | 顺序不可修改 |
| body | 请求体 | 否 | 缩进字典格式或者json格式 | |
| headers | 请求头 | 否 | 缩进字典格式或者json格式 | |
| query_string | 请求参数 | 否 | 缩进字典格式或者json格式 | |
| expected_time | 预期的响应时间 | 否 | | |
| expected_code | 预期的响应代码 | 是 | | |
| expected_result  | 预期的响应结果 | 是 | -列表格式、缩进字典格式或者json格式 | |
| regular | 正则 | 否 | 缩进字典格式 | |
| variable | 变量名 | 否 | -列表格式 | |
| expression | 表达式 | 否 | -列表格式 | |

2、mysql字段说明  
mysql： MySQL语句，-列表格式，顺序不可修改，选填  

| 位置 | 索引 | 作用 | 是否必填 | 格式 | 注解 |
| ---- | ---- | --- | --- | ---- | ---- |
| 第一行 | mysql[0] | 增删改 | 否 | 字符串 | 增、删、改语句 |
| 第二行 | mysql[1] | 查 | 否 | 字符串 | 查语句（动态传参） |
| 第三行 | mysql[2] | 查 | 否 | 字符串 | 查语句（数据库双重断言）|

第一行：mysql[0]  
第二行：mysql[1]  
第三行：mysql[2]  
第一行为增、删、改语句，第二行为查语句（动态传参），第三行为查语句（数据库双重断言）  
第一行是发起请求之前的动作，没有返回结果  
第二行是发起请求之前的动作，有返回结果，是为了动态传参  
第三行是发起请求之后的动作，有返回结果，但是不可用于动态传参，是为了断言实际的响应结果  
当不需要增删改查和双重断言时，可以不写mysql字段，或者三行都为空  
当只需要增删改时，第一行为增删改语句，第二行为空，第三行为空  
当只需要查时，第一行为空，第二行为查语句，第三行为空  
当只需要双重断言时，第一行为空，第二行为空，第三行为查语句  

3、pgsql字段说明  
pgsql： PgSQL语句，-列表格式，顺序不可修改，选填  

| 位置 | 索引 | 作用 | 是否必填 | 格式 | 注解 |
| ---- | ---- | --- | --- | ---- | ---- |
| 第一行 | pgsql[0] | 增删改 | 否 | 字符串 | 增、删、改语句 |
| 第二行 | pgsql[1] | 查 | 否 | 字符串 | 查语句（动态传参） |
| 第三行 | pgsql[2] | 查 | 否 | 字符串 | 查语句（数据库双重断言）|

第一行：pgsql[0]  
第二行：pgsql[1]  
第三行：pgsql[2]  
第一行为增、删、改语句，第二行为查语句（动态传参），第三行为查语句（数据库双重断言）  
第一行是发起请求之前的动作，没有返回结果  
第二行是发起请求之前的动作，有返回结果，是为了动态传参  
第三行是发起请求之后的动作，有返回结果，但是不可用于动态传参，是为了断言实际的响应结果  
当不需要增删改查和双重断言时，可以不写pgsql字段，或者三行都为空  
当只需要增删改时，第一行为增删改语句，第二行为空，第三行为空  
当只需要查时，第一行为空，第二行为查语句，第三行为空  
当只需要双重断言时，第一行为空，第二行为空，第三行为查语句  

4、mongo字段说明（参考mysql字段）  
mongo： Mongo语句，-列表格式，顺序不可修改，选填  

| 位置 | 索引 | 作用| 是否必填 | 格式 | 注解 |
| ---- | ---- | --- | --- | ---- | ---- |
| 第一行 | mongo[0]  | 增删改 | 否 | -列表格式 | 第一个元素为集合名，第二个元素为增删改，第三个元素为增删改参数 |
| 第二行 | mongo[1] | 查 | 否 | -列表格式 | 第一个元素为集合名，第二个元素为查参数 |
| 第三行 | mongo[2] | 查 | 否 | -列表格式 | 第一个元素为集合名，第二个元素为查参数 |
 
第一行：mongo[0]  
第二行：mongo[1]  
第三行：mongo[2]  
第一行为增、删、改，第二行为查（动态传参），第三行为查（数据库双重断言）  
第一行是发起请求之前的动作，没有返回结果  
第二行是发起请求之前的动作，有返回结果，是为了动态传参  
第三行是发起请求之后的动作，有返回结果，但是不可用于动态传参，是为了断言实际的响应结果  
当不需要增删改查和双重断言时，可以不写mongo字段，或者三行都为空  
当只需要增删改时，第一行为增、删、改，第二行为空，第三行为空  
当只需要查时，第一行为空，第二行为查，第三行为空  
当只需要双重断言时，第一行为空，第二行为空，第三行为查  

5、file字段说明  
file： 文件参数，-列表格式，顺序不可修改，选填  

| 位置 | 类型 | 是否必填 | 格式 | 注解 |
| ---- | --- | --- | ---- | ---- |
| 第一行 | 文件类型 | 否 | 字符串 | 例如：file |
| 第二行 | 文件名称 | 否 | 字符串 | 例如：demo_excel.xlsx |
| 第三行 | MIME类型 | 否 | 字符串 | 例如：application/octet-stream |

6、函数助手  

| 函数名称 | 写法 | 作用域| 数量限制 |
| ---- | ---- | --- | --- |
| 正则表达式提取的结果 | ${变量名}  | 全局 | 不限 |
| MySQL查询语句返回的结果 | {__SQL索引} | 本条用例 | 不限 |
| PgSQL查询语句返回的结果 | {__PGSQL索引} | 本条用例 | 不限 |
| Mongo查询语句返回的结果 | {__MONGO索引} | 本条用例 | 不限 |
| 随机数字 | {__RN位数} | 本条用例 | 不限 |
| 随机英文字母 | {__RL位数} | 本条用例 | 不限 |
| 随机手机号码 | {__MP} | 本条用例 | 不限 |
| 随机日期时间字符串 | {__RD开始年份,结束年份} | 本条用例 | 不限 |

正则表达式提取的结果用${变量名}匹配，一条用例里面可以有多个  
MySQL查询语句返回的结果，即第二行mysql[1]返回的结果，用{__SQL索引}匹配  
即{__SQL0}、{__SQL1}、{__SQL2}、{__SQL3}。。。。。。一条用例里面可以有多个  
PgSQL查询语句返回的结果，即第二行pgsql[1]返回的结果，用{__PGSQL索引}匹配  
即{__PGSQL0}、{__PGSQL1}、{__PGSQL2}、{__PGSQL3}。。。。。。一条用例里面可以有多个  
Mongo查询语句返回的结果，即第二行mongo[1]返回的结果，用{__MONGO索引}匹配  
即{__MONGO0}、{__MONGO1}、{__MONGO2}、{__MONGO3}。。。。。。一条用例里面可以有多个  
随机数字用{__RN位数}，如{__RN15}，一条用例里面可以有多个  
随机英文字母用{__RL位数}，如{__RL10}，一条用例里面可以有多个  
随机手机号码用{__MP}，一条用例里面可以有多个  
随机日期时间字符串用{__RD开始年份,结束年份}，如{__RD2019,2020}，一条用例里面可以有多个  
以上8种类型在一条用例里面可以混合使用  
${变量名}的作用域是全局的，其它7种的作用域仅限该条用例   

***
# 四、运行  
1、unittest模式：  
python+测试文件名+环境缩写  
`python case/demo_test.py dev`  
开发环境  
`python case/demo_test.py test`  
测试环境  
`python case/demo_test.py pre`  
预生产环境  
`python case/demo_test.py formal`  
生产环境  

2、pytest模式：  
pytest+--cmd=环境缩写  
`pytest --cmd=dev`  
开发环境  
`pytest --cmd=test`  
测试环境  
`pytest --cmd=pre`  
预生产环境  
`pytest --cmd=formal`  
生产环境  

3、yamlapi模式：  
yamlapi+run+--c=环境缩写  
`yamlapi run --c=dev`  
开发环境  
`yamlapi run --c=test`  
测试环境  
`yamlapi run --c=pre`  
预生产环境  
`yamlapi run --c=formal`  
生产环境  

4、运行结果：  
会在report_log目录下生成以下文件  
allure-report  
log年月日.log  
report.html  
report.xml  
test_case.csv  
test_case.html  
test_case.json  
test_case.xlsx  
test_case.yaml  

***
# 五、打包镜像  
`docker pull registry.cn-hangzhou.aliyuncs.com/yangjianliang/yamlapi:0.0.7`  
从阿里云镜像仓库拉取yamlapi镜像

`docker build -t demo_image .`  
docker build -t 镜像名称 .  
本地打包  
demo_image为镜像名称，随便取  

`docker run -e cmd="test" demo_image:latest`  
docker run -e cmd="环境缩写" 镜像名称:latest  
启动容器  
前台运行  
-e cmd="test"向启动命令动态传递参数，环境缩写为test  
