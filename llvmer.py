import sys
import os
import subprocess
from tqdm import tqdm

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <root directory> <additional compiler flags>")
    exit(1)

CC = "clang -S -emit-llvm"

total_count, c_files_count, failure_count = 0, 0, 0
args = sys.argv[2:]
visited_dirs = set()
for subdir, dirs, files in tqdm(list(os.walk(sys.argv[1]))):
    # in case of links:
    if subdir in visited_dirs:
        raise Exception("This shouldn't happen")
    else:
        visited_dirs.add(subdir)
    # update counts and select source files
    total_count += len(files)
    files = list(filter(lambda file: file.endswith(".c"), files))
    c_files_count += len(files)
    # iterate over files for compilation
    for file in files:
        filepath = os.path.join(subdir, file)
        dst_path = f"{filepath.removesuffix('.c')}.ll"
        print(f"----- {CC} {' '.join(args)} {filepath} -o {dst_path} -----")
        res = subprocess.run(f"{CC} {' '.join(args)} {filepath} -o {dst_path}", stderr=subprocess.PIPE, shell=True)
        if len(res.stderr) > 0:
            print(res.stderr)
        if res.returncode != 0:
            print("!!!FAILURE!!!")
            failure_count += 1
print(f"Summary:\n\tTotal files number: {total_count} (in {len(visited_dirs)} directories)\n\tC source files detected: {c_files_count}\n\tErrors detected: {failure_count}\n\tResult: {'SUCCESS' if failure_count == 0 else 'FAILURE'}")