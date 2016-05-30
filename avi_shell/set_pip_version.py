import os
import yaml

if __name__ == '__main__':

    AVI_PIP_VERSION = '16.1'
    if os.path.exists("./VERSION"):
        with open("./VERSION", "r") as f:
            fs = yaml.load(f.read())
            AVI_PIP_VERSION = "%s.%s" % (fs["Version"], fs["build"])
    with open('pip_version.txt', 'wb') as fd:
        fd.write(AVI_PIP_VERSION)
    fd.close()