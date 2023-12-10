import os
from PIL import Image


def get_png_files(file_path):
    _png_files = []

    for file in os.listdir(file_path):
        name, ext = os.path.splitext(file)
        if ext == ".png":
            _png_files.append(file)

    return _png_files


def convert_to_png(input_file):
    png_img = Image.open(input_file)
    name, ext = os.path.splitext(input_file)
    png_img.save(name + str(".jpg"))


def main():
    path = "."

    png_files = get_png_files(path)

    if not png_files:
        print("No PNG files detected.")
        return

    for png in png_files:
        convert_to_png(png)


if __name__ == "__main__":
    main()
