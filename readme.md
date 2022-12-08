# inst_package
### Install package(s) inside a python script
[![Python](https://img.shields.io/badge/python-3)](https://www.python.org/downloads/)

Supported formats: 

```python
inst("numpy") 
inst("numpy, requests, pandas") 
inst(["numpy", "requests", "pandas"])
```

inst_package install one or more Python packages sequentially using the `pip` command. The function accepts a single parameter called p_name, which can be either a string or a list of strings containing the name(s) of the package(s) to be installed.

```python
import inst_package
inst_package.inst("numpy")
inst_package.inst(["numpy", "requests", "pandas"])
```

The `inst_package()` function first checks the type of the p_name parameter using the isinstance() function. If p_name is a string, the function checks if the string contains a comma character. If it does, the string is split into a list of strings using the split() method, and then the function is called recursively with the list of strings as the argument.

> It can be used in python programs which need dependencies that are not installed by default. I wrote it for my personal interest because I wanted to run a script on a new environment without the need to manually install any dependencies.