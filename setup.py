from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = [
    'requests>=2.23.0',
    'ddt>=1.4.1',
    'PyMySQL>=0.9.3',
    'DBUtils>=1.3',
    'psycopg2-binary>=2.8.5',
    'pymongo>=3.11.0',
    'redis>=3.2.1',
    'influxdb>=5.3.1',
    'BeautifulReport>=0.1.2',
    'demjson>=2.2.4',
    'loguru>=0.5.0',
    'PyYAML>=5.3.1',
    'ruamel.yaml>=0.16.10',
    'pytest>=5.4.2',
    'pytest-html>=2.1.1',
    'allure-pytest>=2.8.16',
    'pytest-reportlog>=0.1.1',
    'pytest-assume>=2.2.1',
    'pytest-rerunfailures>=9.0',
    'pytest-instafail>=0.4.2',
    'pytest-sugar>=0.9.3',
    'pytest-timeout>=1.3.4',
    'pytest-parallel>=0.1.0',
    'tablib>=2.0.0',
    'openpyxl>=3.0.3',
    'MarkupPy>=1.14',
    'Click>=7.0',
]

setup(
    name='yamlapi',
    version='1.3.6',
    description='yamlapi接口测试框架',
    author='yangjianliang',
    author_email='526861348@qq.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yjlch1016/yamlapi',
    license="MIT License",
    packages=['yamlapi'],
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=requires,
    keywords='Interface test framework',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'yamlapi=yamlapi.yaml_api:cli',
        ],
    },
    python_requires='>=3.5',
)
