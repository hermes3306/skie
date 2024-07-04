import os

def list_folders_and_files(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"Directory: {dirpath}")
        for filename in filenames:
            print(f"File: {os.path.join(dirpath, filename)}")

usb_directory = '/'  # Replace this with your USB stick directory
list_folders_and_files(usb_directory)
