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

import subprocess

def git_operations():
    # 1. Print git status
    print("\n=== Git Status ===")
    status_result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(status_result.stdout)
    if status_result.stderr:
        print("STDERR:", status_result.stderr)

    # 2. List planned commands and ask for confirmation
    commands = [
        ["git", "add", "-A"],
        ["git", "commit", "-m", "update files"],
        ["git", "push"]
    ]

    print("\n=== Planned Commands ===")
    for cmd in commands:
        print(" ".join(cmd))

    confirmation = input("\nProceed? (y/n): ").strip().lower()
    if confirmation != "y":
        print("Aborted.")
        return

    # 3. Execute and print results for each command
    for cmd in commands:
        print(f"\n=== Executing: {' '.join(cmd)} ===")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.stdout:
            print("STDOUT:", result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        if result.returncode != 0:
            print(f"Command failed with exit code {result.returncode}")
            break

# Call the function
git_operations()