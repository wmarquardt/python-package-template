from setuptools import setup, find_packages
from python_package_template.version import version

setup(
    name='python-package-template',
    version=version,
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Just another python package template',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],
    install_requires=[],
    url='https://github.com/wmarquardt/python-package-template',
    author='William Marquardt',
    author_email='williammqt@gmail.com'
)
