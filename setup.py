try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='reddit',
    version='1.1.2',
    author='Timothy Mellor',
    author_email='timothy.mellor+pip@gmail.com',
    maintainer='Bryce Boe',
    maintainer_email='bbzbryce+pip@gmail.com',
    url='https://github.com/mellort/reddit_api',
    description='A wrapper for the Reddit API',
    long_description=('Please see the `documentation on github '
                      '<https://github.com/mellort/reddit_api>`_.'),
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2 :: Only',
                 'Topic :: Utilities'],
    license='GPLv3',
    keywords=['api', 'reddit'],
    packages=['reddit'],
    package_data={'reddit': ['*.cfg']})
