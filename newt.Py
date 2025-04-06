#Used Deepseek AI for assistance in simplfiying and fixing errors in code

import subprocess

import sys

def operat():
    
    print("Add, Commit, Push\n")
    

    print("git status:")
    resultGitStatus = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(resultGitStatus.stdout)
    if resultGitStatus.stderr:
        print("STDERR:")
        print(resultGitStatus.stderr)
    
    commands = [
        ["git", "add", "--all"],
        ["git", "commit", "-m", "update files"],
        ["git", "push"]
    ]
    
    print("\nQueued commands:")
    for cmd in commands:
        print(" ".join(cmd))
    
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