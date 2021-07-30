from tkinter import filedialog
from tkinter import Tk
import os
import shutil

Tk().withdraw()

def choose_file():
    filename = filedialog.askopenfilename(
            title="Choose a file",
            filetypes=(("All Files", "*.*"),
                        ("Text files", "*.txt"))
            )
    return filename

def choose_directory():
    dirname = filedialog.askdirectory(title="Choose directory.")
    return dirname

def rename_file(from_file, to_file):
    ext = os.path.splitext(from_file)[-1]
    dirname = os.path.dirname(from_file)
    new_file = os.path.join(dirname, to_file+ext)
    os.rename(from_file, new_file)

def main():
    print("Enter one of the following options to continue:")
    print("1 - Open a file")
    print("2 - Copy a file")
    print("3 - Delete a file")
    print("4 - Rename a file")
    print("5 - Move a file")
    print("6 - Make a folder")
    print("7 - Remove a folder")
    print("8 - List all files in directory")

    options = [i for i in range(1, 9)]
    choice = ""
    while choice not in options:
        choice = int(input("Enter your choice (1-8):> "))

    if choice == 1:
        file = choose_file()
        os.startfile(file)

    if choice == 2:
        to_copy = choose_file()
        to_location = choose_directory()
        shutil.copy(to_copy, to_location)

    if choice == 3:
        file = choose_file()
        os.remove(file)

    if choice == 4:
        file = choose_file()
        new_name = input("Enter new name:> ")
        rename_file(file, new_name)

    if choice == 5:
        file = choose_file()
        to_location = choose_directory()
        shutil.move(file, to_location)

    if choice == 6:
        folder = choose_directory()
        name = input("Enter folder name:> ")
        folder_name = folder + "/" + name
        os.mkdir(folder_name)

    if choice == 7:
        folder = choose_directory()
        shutil.rmtree(folder)

    if choice == 8:
        folder = choose_directory()
        items = os.listdir(folder)
        print("These are the folder(s) or file(s) in this directory")
        for item in items:
            print(item)

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)

        cont = input("Enter q to quit:")
        if cont == "q":
            break
