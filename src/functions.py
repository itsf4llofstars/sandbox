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


def move_file(filename, destination) -> None:
    """Delete a file. Requires import os

    Args:
        filename: The path and name of the orig file
        destination: The path and name of the dest file
    """
    try:
        if os.path.exists(destination):
            print("This file exists at the destination")
        else:
            os.replace(filename, destination)
    except FileNotFoundError:
        raise FileNotFoundError("File was not found")


def main():
    move_from = os.path.expanduser(os.path.join("~", "ed", "lorem.txt"))
    move_to = os.path.expanduser(os.path.join("~", "notes", "lorem_moved.txt"))

    move_file(move_from, move_to)


if __name__ == "__main__":
    main()
