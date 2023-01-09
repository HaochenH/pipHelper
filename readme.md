# instPackage
### Install package(s) inside a python script
[![License](https://img.shields.io/badge/license-GPL-3)](https://www.gnu.org/licenses/gpl-3.0.html) 
[![Python](https://img.shields.io/badge/python-3)](https://www.python.org/downloads/)
[![Pip](https://img.shields.io/badge/pip-3)](https://pypi.org/project/pip/)

<img width="908" alt="image" src="https://user-images.githubusercontent.com/101531662/211398288-f9a987a2-effd-49ae-92af-d64e4de23d9d.png">

You must [have pip installed](https://pip.pypa.io/en/stable/installation/) to use this module. 

instPackage install one or more Python packages sequentially using the `pip` command. The function accepts a single parameter called p_name, which can be either a string or a list of strings containing the name(s) of the package(s) to be installed.

Supported formats:

```python
import instPackage
# install one or more packages
instPackage.inst("numpy")
instPackage.inst(["numpy", "requests", "pandas"])
instPackage.inst("numpy, requests, pandas")
```
```python
# install a specific version
instPackage.instVer("numpy", "1.19.2")
instPackage.instVer(["numpy", "requests", "pandas"], ["1.19.2", "2.28.1", "1.2.3"])
instPackage.instVer("numpy, requests, pandas", "1.19.2, 2.28.1, 1.2.3")
```

The `instPackage()` function first checks the type of the package name parameter using the isinstance() function. If package is a string, the function checks if the string contains a comma character. If it does, the string is split into a list of strings using the split() method, and then the function is called recursively with the list of strings as the argument.

> It can be used in python programs which need dependencies that are not installed by default. I wrote it for my personal interest because I wanted to run a script on a new environment without the need to manually install any dependencies.
