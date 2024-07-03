import os
import subprocess
import shutil

yarn_path = shutil.which('yarn')

os.chdir(os.path.join('..', '..', 'shrillecho-nextjs'))

cmd = [yarn_path, "run", "dev"]
print(cmd)
subprocess.run(cmd, check=True)