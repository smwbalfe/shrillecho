import sys
import os

def update_environment_variables(env_file_paths, target_env):
    for env_file_path in env_file_paths:
        # Resolve the relative path to absolute path
        abs_env_file_path = os.path.abspath(env_file_path)
        
        ### Read the content of the .env file
        with open(abs_env_file_path, "r") as file:
            lines = file.readlines()

        # Update the ENVIRONMENT and NEXT_PUBLIC_ENV lines
        with open(abs_env_file_path, "w") as file:
            for line in lines:
                if line.startswith("ENVIRONMENT="):
                    file.write(f'ENVIRONMENT="{target_env}"\n')
                elif line.startswith("NEXT_PUBLIC_ENV="):
                    file.write(f'NEXT_PUBLIC_ENV={target_env}\n')
                else:
                    file.write(line)

if __name__ == "__main__":
    # Check if an environment argument is provided
    if len(sys.argv) != 2:
        print("Usage: python update_env_vars.py <env>")
        sys.exit(1)

    # The environment to set ('dev' or 'prod')
    target_env = sys.argv[1]

    # Validate the environment argument
    if target_env not in ["dev", "prod"]:
        print("Error: <env> must be 'dev' or 'prod'")
        sys.exit(1)

    # Relative paths to the .env files
    env_paths = [
        r".\shrillecho-nextjs\.env.local",
        r".\shrillecho-fastapi\.env",
    ]
    
    # Update the environment variables
    update_environment_variables(env_paths, target_env)
