from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup (
    name = "pyRedunda",
    packages = ["pyRedunda"],
    version = "1.1.0",
    description = "A python library for using Redunda.",
    author = "Ashish Ahuja",
    author_email = "ashish.ahuja@sobotics.org",
    url = "https://github.com/SOBotics/Redunda-lib-Python",
)
