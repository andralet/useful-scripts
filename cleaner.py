import sys
import os
import subprocess
from tqdm import tqdm

if len(sys.argv) < 2 or 3 < len(sys.argv):
    print(f"Usage: {sys.argv[0]} <root directory> <suffix to search for (default - .ll)>\n")
    exit(1)

target = ".ll" if len(sys.argv) < 3 else sys.argv[2]

total_count, found_files_count = 0, 0
visited_dirs = set()
remove_files = set()
for subdir, dirs, files in tqdm(list(os.walk(sys.argv[1]))):
    # in case of links:
    if subdir in visited_dirs:
        raise Exception("This shouldn't happen")
    else:
        visited_dirs.add(subdir)
    # update counts and select needed files
    total_count += len(files)
    files = list(filter(lambda file: file.endswith(target), files))
    found_files_count += len(files)
    # iterate over files for removal
    for file in files:
        remove_files.add(os.path.join(subdir, file))
print(remove_files)
print(f"You're about to remove the previous {found_files_count} of {total_count} (found in {len(visited_dirs)} directories)")
print(f"If you really want it, enter 'yes' (case insensitive) to continue")
ans = input()
if ans.lower() == "yes":
    for file in tqdm(remove_files):
        os.unlink(file)
    print("Done")
else:
    print("Aborted")