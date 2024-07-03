import os
import subprocess
import shutil

yarn_path = shutil.which('yarn')

os.chdir(os.path.join('..', '..', 'shrillecho-gateway'))

if os.name == 'nt':
    yarn_path += '.cmd'

cmd = [yarn_path, "start:dev"]

subprocess.run(cmd, check=True)