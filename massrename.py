import argparse
import os
import re

def output_msg(msg):
    """
    Checks if the flag --show-output is present and outputs a debug message

    Parameters:
        msg : str
            The message to display
    """

    if args.show_output: print(msg)
    

def filter_files(unfiltered_files, check, part):
    """
    Uses a list of filenames and filters them using the arguments processed by argsparse. 
    Files that don't match the check don't get append to the filtered list, and an output_msg() is shown.

    Parameters:
        unfiltered_files : list
            A list of unfiltered filenames 
        check : str
            If this string is in a filename, it is appended to filtered
        part : int
            Part of the whole filename to check (0=filename, 1=file ext)

    Returns: 
        filtered_files : list
            A list of filtered filenames
        unfiltered_files : list
            In the case where check doesn't exist (=None), it will just return the unfiltered_files
    """

    if check != None:
        filtered_files = [] # Stores filtered files

        output_msg("Filelist (unfiltered): {}".format(unfiltered_files))

        for i in unfiltered_files: # Filtering
            if all(text not in os.path.splitext(i)[part] for text in check[0]):     # If one of the items in check[0] isn't in the filename/extension, filter
                output_msg( "Filtered {} (doesn't include {})".format(i, check) )
                continue
            filtered_files.append(i)
            
        output_msg("Filelist (filtered): {}".format(filtered_files))

        return filtered_files
    return unfiltered_files # If the check doesn't exist, then return the unfiltered files list 


def file_sort_key(file):
    """
    Given a directory with...
    "test1.txt, test2.txt, test10.txt"
    The os.listdir() will return... 
    "test1.txt, test10.txt, test2.txt"
    To make %n work, we need it to return the files in a logical/natural form.
    We use this key to achieve that, while also using the sorted() function.

    Parameters: 
        unsorted_files : list
            A list of unsorted files
    """

    key = re.split(r'(\d+)', file)
    key[1::2] = map(int, key[1::2])
    return key


def rename_files(name, files):
    """
    Changes the name of the files given.

    Parameters:
        name : str
            A string following the name syntax (see name arguments in README.md)
        files : list
            A list of filenames
    """

    new_names = [] # List of new names that match the files parameter

    # Checking for {n} in the name
    if "{n}" not in name:
        name = name + "{n}"

    # Calculating names
    for i in range(len(files)):
        rename = name.format(n=i+1)

        if args.overwrite_ext == False:
            rename = rename + os.path.splitext(files[i])[1]

        new_names.append(rename)

    # Checking new names with user
    print("Old name\tNew name")
    print("--------\t--------")
    for i in range(len(files)):
        print(files[i], "\t", new_names[i])

    if input("Are the filenames correct? (y/N) ").upper() == "Y":
        for i in range(len(files)):
            # Renaming
            os.rename(files[i], new_names[i])
            output_msg("Renamed {} to {}".format(files[i], new_names[i]))
    else:
        output_msg("Input not Y or y, aborting.")



# Processing arguments

parser = argparse.ArgumentParser(description="Command line mass renaming tool")

# Filter arguments
parser.add_argument("name", type=str, help="The name you want to rename the files to")
parser.add_argument("-f", "--filetype", action="append", nargs="+", type=str, help="Filters to files that use the extentions specified")
parser.add_argument("-i", "--includes", action="append", nargs="+", type=str, help="You should give this argument as a string, it does count file extensions (string)")

# Other arguments
parser.add_argument("--show-output", action="store_true", help="Flag for program output")
parser.add_argument("--overwrite-ext", action="store_true", help="Overwrites the built-in feature to automatically add extensions, allowing you to change the extension in the name parameter")

args = parser.parse_args()



# Main

files = os.listdir(os.getcwd())                 # All files in working directory

files = filter_files(files, args.filetype, 1)   # Filtering based on extension
files = filter_files(files, args.includes, 0)   # Filtering based on filename

files = sorted(files, key=file_sort_key)        # Sorting the files into human/natural order

rename_files(args.name, files)


