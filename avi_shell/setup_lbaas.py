from setuptools import setup, find_packages
import os

# added avi pip version
AVI_PIP_VERSION = '16.1'
if os.path.isfile('pip_version.txt'):
   with open('./pip_version.txt', 'r') as fd:
      AVI_PIP_VERSION = fd.read()
AVI_PIP_VERSION = AVI_PIP_VERSION.strip()

setup(name='avi_lbaas',
    author = 'Avi Networks',
    author_email = 'support@avinetworks.com',
    version=AVI_PIP_VERSION,
    description='Command line interface to view and configure Avi Software',
    url='http://www.avinetworks.com',
    py_modules=['avi_lbaas'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'avi_lbaas = avi_lbaas:main',
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
        'Babel==2.1.1',
        'cmd2==0.6.8',
        'debtcollector==1.1.0',
        'funcsigs==0.4',
        'iso8601==0.1.11',
        'monotonic==0.5',
        'msgpack-python==0.4.6',
        'netaddr==0.7.18',
        'netifaces==0.10.4',
        'oslo.config==3.2.0',
        'oslo.i18n==3.1.0',
        'oslo.serialization==2.2.0',
        'oslo.utils==3.3.0',
        'pbr==1.8.1',
        'prettytable==0.7.2',
        'python-keystoneclient==1.8.1',
        'pytz==2015.7',
        'requests==2.9.1',
        'requests-toolbelt==0.5.1',
        'six==1.10.0',
        'stevedore==1.10.0',
        'urllib3==1.14',
        'virtualenv==13.1.2',
        'wheel==0.26.0',
        'wrapt==1.10.6',
        'commentjson'
    ]

)
