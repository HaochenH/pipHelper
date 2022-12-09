import inst_package
# install a single package
inst_package.inst("numpy")
# install multiple packages
inst_package.inst("numpy, requests, pandas")
# or
inst_package.inst(["numpy", "requests", "pandas"])
# install a specific version of a package
inst_package.inst_version("numpy", "1.19.2")
inst_package.inst_version(["numpy", "requests", "pandas"], ["1.19.2", "2.28.1", "1.2.3"])
inst_package.inst_version("numpy, requests, pandas", "1.19.2, 2.28.1, 1.2.3")