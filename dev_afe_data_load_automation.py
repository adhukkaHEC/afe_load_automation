# Import packages and make sure git is installed
import os
import subprocess
import time 
subprocess.run(["python", "-m", "pip", "install", "GitPython"])
from git import Repo
os.environ['APP_ENV'] = "DEV"   # APP_ENV set to DEV since this automation is for development environment

# Define github credentials
github_username = "adhukkaHEC"
github_token = "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"
repo_url = "https://" + github_username + ":" + github_token + "@github.com/Hilcorp-Reserves/reserves-afe-loader.git"

# Define destination file path for repo folder as well as virutal environment. This will need to be updated depending 
# on the location you would like to host the process
repo_folder = "D:\\Users\\al10810\\Desktop\\reserves-afe-loader"
# Path to the virtual environment (DO NOT CHANGE)
venv_folder = repo_folder + "\\proc_venv"

# Clone or update the repository depending on if the folder for the AFE load process already exists
if os.path.exists(repo_folder):
    repo = Repo(repo_folder)    
else:
    repo = Repo.clone_from(repo_url, repo_folder)

# Checkout Develope branch
repo.git.checkout("develop")

# Set working directory to the repo folder
os.chdir(repo_folder)

# Create execution script to run main.py using python executable in virtual environment
python_executable = os.path.join(venv_folder, "Scripts", "python.exe")
main_py_file = os.path.join(repo_folder, "src", "main.py")

# Deploy execution in terminal
subprocess.run([python_executable, main_py_file])

