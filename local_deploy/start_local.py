import subprocess
import sys

def run_in_new_terminal(command):
    if sys.platform == "win32":
        subprocess.run(f"start cmd /c {command}", shell=True)
    elif sys.platform == "linux":
        subprocess.run(f"xterm -e {command}", shell=True)
    elif sys.platform == "darwin":
        subprocess.run(f"osascript -e 'tell application \"Terminal\" to do script \"{command}\"'", shell=True)


# # Stop, remove, and run Docker commands
# commands = [
#     ['docker', 'stop', 'redis'],
#     ['docker', 'rm', 'redis'],
#     ['docker', 'run', '--name', 'redis', '-p', '6379:6379', '-d', 'redis']
# ]

# # Execute Docker commands
# for cmd in commands:
#     try:
#         subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         print(f"Command {' '.join(cmd)} executed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error executing {' '.join(cmd)}:", e.stderr)

# Commands to run Python scripts in new terminal windows
python_scripts = [
    "python start_web.py",
    "python start_server.py",
]

# Execute Python scripts in new terminals
for script in python_scripts:
    run_in_new_terminal(script)
