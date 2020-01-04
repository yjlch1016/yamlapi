from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='yamlapi',
    version='1.0.0',
    description='Interface test framework',
    author='yangjianliang',
    author_email='526861348@qq.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yjlch1016/yamlapi',
    py_modules=['yaml_api'],
    install_requires=[
        'Click', 'requests', 'ddt', 'PyMySQL', 'BeautifulReport',
        'demjson', 'loguru', 'PyYAML', 'pytest', 'pytest-html',
        'allure-pytest', 'pytest-rerunfailures'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        yamlapi=yaml_api:start_project
    ''',
    python_requires='>=3.5.0',
)
