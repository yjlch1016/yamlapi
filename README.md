# yamlapi  
yamlapi接口测试框架  
支持unittest与pytest两种运行模式  
yamlapi即为yaml文件+api测试的缩写  
可看作是一个脚手架工具  
可快速生成项目的各个目录与文件  
只需维护一份或者多份yaml文件即可  

# 安装  
pip install yamlapi  

# 查看参数信息  
yamlapi -h（或yamlapi --help）  

# 查看版本号  
yamlapi -v（或yamlapi --v）  

# 安装最新版  
pip install -U yamlapi  

# 创建项目  
yamlapi --p=项目名称  
例如在某个路径下执行命令：  
yamlapi --p=demo_project  

# 卸载  
pip uninstall yamlapi  

# 运行  
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
