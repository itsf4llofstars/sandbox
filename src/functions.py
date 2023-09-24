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
    except FileNotFoundError as fnfe:
        raise FileNotFoundError("File was not found") from fnfe


def delete_file(filename) -> None:
    """Delete a file. Requires import os

    Args:
        filename (None): path and filename of the file
    """
    try:
        os.remove(filename)
    except FileNotFoundError as fnfe:
        raise FileNotFoundError("File was not found") from fnfe


def main():
    delete_file(os.path.expanduser(os.path.join("~", "notes", "lorem_moved.txt")))


if __name__ == "__main__":
    main()
