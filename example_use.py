import inst_package
# install a single package
inst_package.inst("numpy")
# install multiple packages
inst_package.inst("numpy, requests, pandas")
# or
inst_package.inst(["numpy", "requests", "pandas"])