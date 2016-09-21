import os
import sys
import shutil


if __name__ == '__main__':
    package = 'eventboost'
    for path in sys.path:
        if os.path.isdir(path) and os.path.abspath(path) != os.getcwd():
            shutil.rmtree('{0}/{1}'.format(path, package))
            shutil.copytree(
                src='{0}/{1}'.format(os.getcwd(), package),
                dst='{0}/{1}'.format(path, package)
            )
            print('Package has been installed in {0}'.format(path))
            break
