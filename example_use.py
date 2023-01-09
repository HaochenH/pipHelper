import instPackage
# install a single package
instPackage.inst("numpy")
# install multiple packages
instPackage.inst("numpy, requests, pandas")
# or
instPackage.inst(["numpy", "requests", "pandas"])
# install a specific version of a package
instPackage.instVer("numpy", "1.19.2")
instPackage.instVer(["numpy", "requests", "pandas"], ["1.19.2", "2.28.1", "1.2.3"])
instPackage.instVer("numpy, requests, pandas", "1.19.2, 2.28.1, 1.2.3")