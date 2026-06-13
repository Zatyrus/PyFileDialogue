## dependencies
import os
import tkinter as tk
from tkinter import filedialog
from typing import List, Tuple, Union

__all__ = [
    "call_directory",
    "call_subdirectories",
    "call_file",
    "call_multiple_files",
    "call_save_as_file",
]


# method implementations
def call_directory(title: str = "Please select a directory") -> str:
    """Open a file dialog to select a directory.

    Args:
        title (str, optional): Select a title for the dialog. Defaults to "Please select a directory".

    Returns:
        str: The path of the selected directory.
    """
    root = tk.Tk()
    root.withdraw()
    root.call("wm", "attributes", ".", "-topmost", True)
    DIR_path = filedialog.askdirectory(title=title)
    return DIR_path


def call_subdirectories(
    title: str = "Please select a directory to scan",
) -> List[str]:
    """Open a file dialog to select a directory and return a list of all subdirectories within it.

    Args:
        title (str, optional): Select a title for the dialog. Defaults to "Please select a directory to scan".

    Returns:
        List[str]: A list of paths for the selected subdirectories.
    """
    directory = call_directory(title=title)
    return [f.path for f in os.scandir(directory) if f.is_dir()]


def call_file(
    title: str = "Please select a file",
    filetypes: List[Tuple[str, str]] = [("All files", "*")],
) -> str:
    """Open a file dialog to select a file.

    Args:
        title (str, optional): Select a title for the dialog. Defaults to "Please select a file".
        filetypes (List[Tuple[str, str]], optional): A list of tuples specifying the file types to display. Defaults to [("All files", "*")].

    Returns:
        str: The path of the selected file.
    """
    root = tk.Tk()
    root.withdraw()
    root.call("wm", "attributes", ".", "-topmost", True)
    FILE_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    return FILE_path


def call_multiple_files(
    title: str = "Please select a number of files",
    filetypes: List[Tuple[str, str]] = [("All files", "*")],
) -> Union[Tuple[str, ...], str]:
    """Open a file dialog to select multiple files.

    Args:
        title (str, optional): Select a title for the dialog. Defaults to "Please select a number of files".
        filetypes (List[Tuple[str, str]], optional): A list of tuples specifying the file types to display. Defaults to [("All files", "*")].

    Returns:
        Union[Tuple[str, ...], str]: A tuple of paths for the selected files, or a single path if only one file is selected.
    """
    root = tk.Tk()
    root.withdraw()
    root.call("wm", "attributes", ".", "-topmost", True)
    FILE_path = filedialog.askopenfilenames(title=title, filetypes=filetypes)
    return FILE_path


def call_save_as_file(
    defaultextension: str = "*",
    title: str = "Save as...",
    confirmoverwrite: bool = True,
    filetypes: Union[List, None] = None,
    initialfile: Union[str, None] = None,
) -> str:
    """Open a file dialog to select a file path for saving.

    Args:
        defaultextension (str, optional): Select the filetype to default to. Defaults to "*".
        title (str, optional): Select a title for the dialog. Defaults to "Save as...".
        confirmoverwrite (bool, optional): Confirm overwrite if the file already exists. Defaults to True.
        filetypes (Union[List, None], optional): A list of tuples specifying the file types to display. Defaults to None.
        initialfile (Union[str, None], optional): The initial filename to display. Defaults to None.

    Returns:
        str: The path of the selected file.
    """
    root = tk.Tk()
    root.withdraw()
    root.call("wm", "attributes", ".", "-topmost", True)
    FILE_path = filedialog.asksaveasfilename(
        defaultextension=defaultextension,
        title=title,
        confirmoverwrite=confirmoverwrite,
        initialfile=initialfile if initialfile is not None else "",
        filetypes=filetypes
        if filetypes is not None
        else [
            ("Text files", "*.txt"),
            ("Json files", "*.json"),
            ("CSV files", "*.csv"),
            ("Npy files", "*.npy"),
            ("Pkl files", "*.pkl"),
            ("png files", "*.png"),
            ("jpg files", "*.jpg"),
            ("jpeg files", "*.jpeg"),
            ("svg files", "*.svg"),
            ("pdf files", "*.pdf"),
            ("All files", "*"),
        ],
    )
    return FILE_path
