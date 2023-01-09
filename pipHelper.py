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
                print(
                    f'\033[92m{p} is already installed, skipping installation.\033[0m')

        if isinstance(package, list):  # if package is a list, install all packages in the list
            for p in package:
                inst(p)

    except Exception as e:
        print(
            f'\033[31mAn error {e} occurred while installing {package}.\033[0m')


def instVer(package, version):
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
                instVer(package, version)
                return
            p = package.replace(" ", "")
            print(
                f'\033[35mChecking status of {p} version {version} using pip...\033[0m')
            output = subprocess.run("pip3 show " + p, shell=True)
            if output.returncode != 0:
                subprocess.run("pip3 install " + p +
                               "==" + version, shell=True)
            else:
                print(
                    f'\033[92m{p} is already installed, skipping installation.\033[0m')

        if isinstance(package, list):
            for p, v in zip(package, version):
                instVer(p, v)

    except Exception as e:
        print(
            f'\033[31mAn error {e} occurred while installing {package}.\033[0m')


def uninst(package):
    """
    Uninstall package(s).
    """
    try:
        if isinstance(package, str):
            if "," in package:
                package = package.split(",")
                uninst(package)
                return
            p = package.replace(" ", "")
            print(f'\033[35mUninstalling {p}...\033[0m')
            subprocess.run("pip3 uninstall -y " + p, shell=True)
        else:
            print(f'\033[35mPackage not found.\033[0m')

        if isinstance(package, list):
            for p in package:
                uninst(p)

    except Exception as e:
        print(
            f'\033[31mAn error {e} occurred while uninstalling {package}.\033[0m')


def uninstAll():
    print("\033[35mFetching all packages installed using pip...\033[0m")
    subprocess.run("pip3 freeze > all_packages.txt", shell=True)
    with open("all_packages.txt", "r") as f:
        packages = f.read().splitlines()
        # packages = [p.split("==")[0] for p in packages]
        print(packages)
        for p in packages:
            uninst(p)
        print("\033[35mAll packages uninstalled.\033[0m")