## dependencies
import os
import tkinter as tk
from tkinter import filedialog
from typing import List, Tuple, Union


## main class implementation
class PyDialogue:
    def __init__(self) -> "PyDialogue":
        """Initialize the PyDialogue class."""
        pass

    def askDIR(self, title: str = "Please select a directory") -> str:
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

    def askDIRS(self, title: str = "Please select a directory to scan") -> List[str]:
        """Open a file dialog to select a directory and return a list of all subdirectories within it.

        Args:
            title (str, optional): Select a title for the dialog. Defaults to "Please select a directory to scan".

        Returns:
            List[str]: A list of paths for the selected subdirectories.
        """
        directory = self.askDIR(title=title)
        return [f.path for f in os.scandir(directory) if f.is_dir()]

    def askFILE(
        self,
        title: str = "Please select a file",
        filetypes: List[Tuple[str]] = [("All files", "*")],
    ) -> str:
        """Open a file dialog to select a file.

        Args:
            title (str, optional): Select a title for the dialog. Defaults to "Please select a file".
            filetypes (List[Tuple[str]], optional): A list of tuples specifying the file types to display. Defaults to [("All files", "*")].

        Returns:
            str: The path of the selected file.
        """
        root = tk.Tk()
        root.withdraw()
        root.call("wm", "attributes", ".", "-topmost", True)
        FILE_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
        return FILE_path

    def askFILES(
        self,
        title: str = "Please select a number of files",
        filetypes: list = [("All files", "*")],
    ) -> List[str]:
        """Open a file dialog to select multiple files.

        Args:
            title (str, optional): Select a title for the dialog. Defaults to "Please select a number of files".
            filetypes (list, optional): A list of tuples specifying the file types to display. Defaults to [("All files", "*")].

        Returns:
            List[str]: A list of paths for the selected files.
        """
        root = tk.Tk()
        root.withdraw()
        root.call("wm", "attributes", ".", "-topmost", True)
        FILE_path = filedialog.askopenfilenames(title=title, filetypes=filetypes)
        return FILE_path

    def askSAVEASFILE(
        self,
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
