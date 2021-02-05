FROM registry.cn-hangzhou.aliyuncs.com/yangjianliang/yamlapi:0.0.8
# 基础镜像

MAINTAINER yangjianliang <526861348@qq.com>
# 作者

COPY . /apitest/
# 拷贝代码

ENV cmd test
# 设置环境变量：被测环境的缩写

WORKDIR /apitest/
# 设置工作目录

ENTRYPOINT pytest --cmd=$cmd
# 运行测试工程
