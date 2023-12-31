# Documentation

If files are destroyed copies of their contents should be placed here. Notes and
documentation on files/scripts can also be created here.

## Contents

1. Copy File
2. Move File
3. Delete File

### Copy File

```python3
def copy_file(filename, destination, copy_type=None) -> None:
    """Copy a file. Requires import shutil

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
```

### Move File

Can be used to move a folder by omitting filename data.

```python3
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
```

### Delete File

```python3
def delete_file(filename) -> None:
    """Delete a file. Requires import os

    Args:
        filename (None): path and filename of the file
    """
    try:
        os.remove(filename)
    except FileNotFoundError as fnfe:
        raise FileNotFoundError("File was not found") from fnfe
```
