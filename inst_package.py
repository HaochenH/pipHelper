import subprocess

def inst(package):
    """
    Install package(s) inside a python script.
    Supported formats:
    inst("numpy")
    inst("numpy, requests, pandas")
    inst(["numpy", "requests", "pandas"])
    """
    try:
        if isinstance(package, str):  # if package is a string, install the package
            print(f'\033[35mInstalling {package}...')
            if "," in package:
                package = package.split(",")
                inst(package)
                return
            p = package.replace(" ", "")
            print(f'Checking status of {p} using pip...\033[0m')
            output = subprocess.run("pip3 show " + p, shell=True)
            if output.returncode != 0:
                subprocess.run("pip3 install " + p, shell=True)
            else:
                print(f'\033[92m{p} is already installed, skipping installation.\033[0m')

        if isinstance(package, list):  # if package is a list, install all packages in the list
            for p in package:
                inst(p)

    except Exception as e:
        print(f'\033[31mAn error {e} occurred while installing {package}.\033[0m')

def inst_version(package, version):
    """
    Install a specific version of a package(s)
    Accept: ["numpy", "requests", "pandas"], ["1.19.2", "2.28.1", "1.2.3"]
    or: "numpy, requests, pandas", "1.19.2, 2.28.1, 1.2.3"
    or: "numpy", "1.19.2"
    """
    try:
        if isinstance(package, str):
            if "," in package:
                package = package.split(",")
                version = version.split(",")
                inst_version(package, version)
                return
            p = package.replace(" ", "")
            print(f'\033[35mInstalling {p} version {version}...')
            print(f'Checking status of {p} using pip...\033[0m')
            output = subprocess.run("pip3 show " + p, shell=True)
            if output.returncode != 0:
                subprocess.run("pip3 install " + p + "==" + version, shell=True)
            else:
                print(f'{p} is already installed, skipping installation.\n')

        if isinstance(package, list):
            for p, v in zip(package, version):
                inst_version(p, v)
        
    except Exception as e:
        print(f'\033[31mAn error {e} occurred while installing {package}.\033[0m')