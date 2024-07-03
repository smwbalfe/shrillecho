import subprocess
import os
import sys

def run_command(command):
    try:
        result = subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error: {e}")
        sys.exit(1)

# Change directory to the required path
project_dir = os.path.join('..', '..', 'shrillecho-fastapi')
# print(os.path.abspath(project_dir))
# exit(1)
# os.chdir(project_dir)

# Check if the virtual environment already exists
venv_dir = os.path.join(project_dir, '.venv')
if not os.path.exists(venv_dir):
    # Create a virtual environment
    run_command([sys.executable, '-m', 'venv', venv_dir])
else:
    print("Virtual environment already exists.")

# Path to the Python executable in the virtual environment
venv_python = os.path.join(venv_dir, 'Scripts', 'python.exe') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'python')

# Upgrade pip and install required packages
requirements_path = os.path.abspath(os.path.join(project_dir, 'requirements.txt'))
shrillecho_py_path = os.path.abspath(os.path.join('..', '..', 'shrillecho-py'))
run_command([venv_python, '-m', 'pip', 'install', '--upgrade', 'pip'])
run_command([venv_python, '-m', 'pip', 'install', '-r', requirements_path, 'uvicorn', '-e', shrillecho_py_path])

os.chdir(project_dir)
# Start the uvicorn server
subprocess.Popen([
    venv_python, '-m', 'uvicorn', 'server:app', '--proxy-headers', '--host', 'localhost', '--port', '8001', '--reload'
])
