import pipHelper
# install one or more packages
pipHelper.inst("numpy")
pipHelper.inst(["numpy", "requests", "pandas"])
pipHelper.inst("numpy, requests, pandas")

# install a specific version
pipHelper.instVer("numpy", "1.19.2")
pipHelper.instVer(["numpy", "requests", "pandas"], ["1.19.2", "2.28.1", "1.2.3"])
pipHelper.instVer("numpy, requests, pandas", "1.19.2, 2.28.1, 1.2.3")

# uninstall packages
pipHelper.uninst("numpy, requests")

# uninstall all packages
# pipHelper.uninstAll()