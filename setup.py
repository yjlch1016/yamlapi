from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = [
    'requests==2.22.0',
    'ddt==1.2.1',
    'PyMySQL==0.9.3',
    'BeautifulReport==0.0.9',
    'demjson==2.2.4',
    'loguru==0.4.0',
    'PyYAML==5.1.2',
    'pytest==5.0.1',
    'pytest-html==2.0.1',
    'allure-pytest==2.8.6',
    'pytest-rerunfailures==8.0',
    'Click==7.0',
]

setup(
    name='yamlapi',
    version='1.0.1',
    description='honeybee（蜜蜂）接口测试框架',
    author='yangjianliang',
    author_email='526861348@qq.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yjlch1016/yamlapi',
    license="MIT License",
    py_modules=['yaml_api'],
    install_requires=requires,
    keywords='Interface test framework',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        yamlapi=yaml_api:start_project
    ''',
    python_requires='>=3.5',
)
