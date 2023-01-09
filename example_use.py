import pipHelper
# install multiple packages
pipHelper.inst("numpy, requests")
# install a specific version of a package
pipHelper.instVer("numpy, requests", "1.19.2, 2.28.1")
pipHelper.uninst("numpy, requests")
# pipHelper.uninstAll()