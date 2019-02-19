from setuptools import setup, find_packages


setup(
    name='telega',
    version='1.0.2',
    packages=find_packages(),
    url='https://github.com/RusJr/telega',
    license='MIT',
    author='Rus Jr',
    author_email='binderrrr@gmail.com',
    keywords='telegram telega client tglib',
    description='Python Telegram TDLib sync client',
    package_data={
        'telega': ['td_lib/linux/libtdjson.so', ],
    },
    python_requires=">=3.5",
    install_requires=[]
)
