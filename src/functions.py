"""
Name: functions.py
Author: itsf4llofstars
Desc: Copying files
"""
import os
import shutil


def copy_file(filename, destination, copy_type=None) -> None:
    """Copy a file
    copyfile() -> Contents (destination filename needed)
    copy() -> copyfile() + permissions
    copy2() -> copy() + metadata

    Args:
        filename: The path and filename to be copied from
        destination: The path and filename to be copied to
    """
    if copy_type is None:
        shutil.copyfile(filename, destination)
    elif int(copy_type) == 1:
        shutil.copy(filename, destination)
    elif int(copy_type) == 2:
        shutil.copy2(filename, destination)


def main():
    files_name = "lorem.txt"
    files_dest = "lorem_copy.txt"

    name = os.path.expanduser(os.path.join("~", "notes", files_name))
    dest = os.path.expanduser(os.path.join("~", "ed"))

    copy_file(name, dest, 2)


if __name__ == "__main__":
    main()
