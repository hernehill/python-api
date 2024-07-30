name = 'sg_api'

version = '3.6.1.hh.1.0.0'

authors = [
    'Autodesk',
]

description = '''Flow, AKA shotgrid, AKA Shotgun Python API'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']

requires = [
]

private_build_requires = [
]

variants = [
]

def commands():
    env.REZ_SG_API_ROOT = '{root}'
    env.PYTHONPATH.append('{root}')

build_command = 'rez python {root}/rez_build.py'

uuid = 'repository.python-api'
