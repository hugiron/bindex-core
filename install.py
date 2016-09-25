import os
import sys
import shutil


def install_dependencies():
    dependencies = ['requests', 'bs4', 'mongoengine', 'pika', 'pandas']
    for dp in dependencies:
        os.system('pip install {0}'.format(dp))
        print('{0} installed from pip'.format(dp))


def remove_cache(path):
    cache = '{0}/__pycache__'.format(path)
    if os.path.exists(cache):
        shutil.rmtree(cache)
    for folder in os.listdir(path):
        next_path = '{0}/{1}'.format(path, folder)
        if os.path.isdir(next_path):
            remove_cache(next_path)


def install_package():
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

if __name__ == '__main__':
    install_dependencies()
    remove_cache('.')
    print('All cache has been removed...')
    install_package()
