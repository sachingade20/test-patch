from setuptools import setup, find_packages
import os

# added avi pip version
AVI_PIP_VERSION = '16.1'
if os.path.isfile('pip_version.txt'):
   with open('./pip_version.txt', 'r') as fd:
      AVI_PIP_VERSION = fd.read()
AVI_PIP_VERSION = AVI_PIP_VERSION.strip()

setup(name='avi_shell',
    author = 'Avi Networks',
    author_email = 'support@avinetworks.com',
    version=AVI_PIP_VERSION,
    description='Command line interface to view and configure Avi Software',
    url='http://www.avinetworks.com',
    py_modules=['avi_shell'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'avi_shell = avi_shell:main',
            ],
        },
    packages=find_packages(),
    include_package_data = True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Customers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'cmd2==0.6.8',
        'iso8601==0.1.11',
        'prettytable==0.7.2',
        'pytz==2015.7',
        'requests==2.20.0',
        'requests-toolbelt==0.5.1',
        'urllib3==1.14',
        'virtualenv==13.1.2',
        'wheel==0.26.0',
        'wrapt==1.10.6',
        'commentjson'
    ]

)
