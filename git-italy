#!/usr/bin/env python3

import subprocess
import sys

# Italian gesture meme in ASCII
ITALIAN_GESTURE = """
        \\
         \\
          🤌
"""

COMMANDS = {
    "pizza": "push",
    "pasta": "pull",
    "carbonara": "checkout",
    "mamma-mia": "--help",
}

def main():
    args = sys.argv[1:]
    if not args:
        print(f"{ITALIAN_GESTURE}\nUsage: git-italy <command> [options]")
        return

    command = args[0]
    translated_command = COMMANDS.get(command, command)

    if translated_command == "--help":
        print(f"{ITALIAN_GESTURE}\nUse these commands:")
        for italian, git_command in COMMANDS.items():
            print(f"  git {italian} -> git {git_command}")
        return

    # Execute the Git command with the translated arguments
    subprocess.run(["git", translated_command] + args[1:])

if __name__ == "__main__":
    main()
