#!/usr/bin/python

from setuptools import setup
import sys

DESC = """SPF (Sender Policy Framework) implemented in Python."""
with open("README.md", "r") as fh:
    LONG_DESC = fh.read()

if sys.version_info[0] == 2:
    install_req = ['PyDNS', 'authres', 'ipaddr']
else:
    install_req = ['Py3DNS', 'authres']

setup(name='pyspf',
      version='2.0.14',
      description=DESC,
      long_description=LONG_DESC,
      long_description_content_type="text/markdown",
      author='Terence Way',
      author_email='terry@wayforward.net',
      maintainer="Stuart D. Gathman",
      maintainer_email="stuart@gathman.org",
      url='https://github.com/sdgathman/pyspf/',
      license='Python Software Foundation License',
      py_modules=['spf'],
      keywords = ['spf','email','forgery'],
      scripts = ['type99.py','spfquery.py'],
      include_package_data=True,
      zip_safe = False,
      install_requires=install_req,
      classifiers = [
	'Development Status :: 5 - Production/Stable',
	'Environment :: No Input/Output (Daemon)',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: Python Software Foundation License',
	'Natural Language :: English',
	'Operating System :: OS Independent',
	'Programming Language :: Python',
	'Programming Language :: Python :: 3',
	'Topic :: Communications :: Email :: Mail Transport Agents',
	'Topic :: Communications :: Email :: Filters',
	'Topic :: Internet :: Name Service (DNS)',
	'Topic :: Software Development :: Libraries :: Python Modules'
      ]
)

if sys.version_info < (2, 6):
    raise Exception("pyspf 2.0.6 and later requires at least python2.6.")
