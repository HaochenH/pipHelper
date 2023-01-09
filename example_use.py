import pipHelper
# install a single package
pipHelper.inst("numpy")
# install multiple packages
pipHelper.inst("numpy, requests, pandas")
# or
pipHelper.inst(["numpy", "requests", "pandas"])
# install a specific version of a package
pipHelper.instVer("numpy", "1.19.2")
pipHelper.instVer(["numpy", "requests", "pandas"], ["1.19.2", "2.28.1", "1.2.3"])
pipHelper.instVer("numpy, requests, pandas", "1.19.2, 2.28.1, 1.2.3")