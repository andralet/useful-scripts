# useful-scripts
Some handy scripts used from time to time.

### Requirements
* llvmer.py and cleaner.py use tqdm python module (may be installed with `pip install tqdm`). If you don't want to install it, just remove tqdm reference from the code: it does nothing important there.

### llvmer.py
Runs clang -S -emit-llvm for each .c file in directory provided in the first command line argument and its subdirectories with additional options provided in the following arguments. If possible, creates resulting .ll file for each .c file processed. This tool has lots of output, so it's better to redirect it into a file. The overall statistic is given in the end.

Note that this tool may be pretty much slow because of waiting for each command completion and saving its output. Disabling the output and using some sort of [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) may be in order when logs are not important.

For logic modification see command building for subprocess.run in the code.

### cleaner.py
A straightforward way to remove all files in directory provided in the first command line argument and its subdirectories with suffix from the second command line argument, if given (.ll by default). Shows filenames and asks for confirmation, so it's relatively safe.

The code logic is the same as for llvmer.py script.