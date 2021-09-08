from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(
    name='yamlapi',
    version='1.4.1',
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
    install_requires=requirements,
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
