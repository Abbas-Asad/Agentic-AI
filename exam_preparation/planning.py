import agents
import os
from rich import print

# Get the path to the agents module
agents_path = os.path.dirname(agents.__file__)
print(f"Agents module path: {agents_path}")

# List only files (not folders) from agents directory
file_count = 0
for item in os.listdir(agents_path):
    item_path = os.path.join(agents_path, item)
    if os.path.isfile(item_path):  # Only files, not folders
        file_count += 1
        print(f"{file_count}. {item}")

print(f"\nTotal files found: {file_count}")