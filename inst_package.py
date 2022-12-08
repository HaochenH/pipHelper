import subprocess

def inst_package(p_name):
    """
    Install package(s) inside a python script.
    Supported formats:
    inst_package("numpy, requests, pandas")
    inst_package(["numpy", "requests", "pandas"])
    """

    if isinstance(p_name, str):  # if p_name is a string, install the package
        print(f'\033[35mInstalling {p_name}...')
        if "," in p_name:
            p_name = p_name.split(",")
            inst_package(p_name)
            return
        p = p_name.replace(" ", "")
        print(f'Checking status of {p} using pip...\033[0m')
        output = subprocess.run("pip3 show " + p, shell=True)
        if output.returncode != 0:
            subprocess.run("pip3 install " + p, shell=True)
        else:
            print(f'{p} is already installed, skipping installation.\n')

    if isinstance(p_name, list):  # if p_name is a list, install all packages in the list
        for p in p_name:
            inst_package(p)