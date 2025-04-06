import subprocess

import sys

print("Add, Commit, Push")

print("Executing /""git status/"" ")
print("")

# Run the git status command
resultGitStatus = subprocess.run(["git", "status"], capture_output=True, text=True)

print("Executing /""git status/"" ")
print("")

print(resultGitStatus.stdout)
print("STDERR:")
print(resultGitStatus.stderr)

print("Executing /""git add --all/"" ")
print("")

# Run the git status command
resultGitAdd = subprocess.run(["git", "add", "--all"], capture_output=True, text=True)
print(resultGitAdd.stdout)
print("STDERR:")
print(resultGitAdd.stderr)

if len(sys.argv) !=3:
    message = sys.argv[2]
    print (message)
    message = "\"update files. \""

print("Executing \"commit -m\" ")
print("")

# Run the git status command
resultGitcommit = subprocess.run(["git", "commit", "-m", message ], capture_output=True, text=True)
print(resultGitcommit.stdout)
print("STDERR:")
print(resultGitcommit.stderr)

print("Executing /""git Push/"" ")
print("")

# Run the git status command
resultGitPush = subprocess.run(["git", "push"], capture_output=True, text=True)
print(resultGitPush.stdout)
print("STDERR:")
print(resultGitPush.stderr)

confirmation = input("\nAre you sure?: ").strip().lower()
    if confirmation != 'y' != 'yes':
        print("Redacted")
        return

    for cmd in commands:
        print(f"\nExecuting: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        if result.returncode != 0:
            print(f"Command failed with exit code {result.returncode}")
            break
