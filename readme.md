# pipHelper
### Install or remove package(s) inside a python script
[![License](https://img.shields.io/badge/license-GPL-3)](https://www.gnu.org/licenses/gpl-3.0.html) 
[![Python](https://img.shields.io/badge/python-3)](https://www.python.org/downloads/)
[![Pip](https://img.shields.io/badge/pip-3)](https://pypi.org/project/pip/)

You must have [pip](https://pip.pypa.io/en/stable/installation/) installed to use this module. 

pipHelper install or uninstall one or more Python packages sequentially using the `pip` command. The function accepts a single parameter called p_name, which can be either a string or a list of strings containing the name(s) of the package(s) to be installed.

pipHelper can also help you uninstall all packages. 


Supported formats:

```python
import pipHelper
# install one or more packages
pipHelper.inst("numpy")
pipHelper.inst(["numpy", "requests", "pandas"])
pipHelper.inst("numpy, requests, pandas")
```
```python
# install a specific version
pipHelper.instVer("numpy", "1.19.2")
pipHelper.instVer(["numpy", "requests", "pandas"], ["1.19.2", "2.28.1", "1.2.3"])
pipHelper.instVer("numpy, requests, pandas", "1.19.2, 2.28.1, 1.2.3")

# uninstall packages
pipHelper.uninst("numpy, requests")

# uninstall all packages
pipHelper.uninstAll()
```

The `inst()` function first checks the type of the package name parameter using the isinstance() function. If package is a string, the function checks if the string contains a comma character. If it does, the string is split into a list of strings using the split() method, and then the function is called recursively with the list of strings as the argument.

> t could be used to quickly build an environment if a python program needs dependencies.
