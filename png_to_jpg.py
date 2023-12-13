import os
import sys
from PIL import Image


def get_png_files(file_path):
    _png_files = []

    for file in os.listdir(file_path):
        name, ext = os.path.splitext(file)
        if ext == ".png":
            _png_files.append(file)

    return _png_files


def convert_to_png(file_path):
    if not os.path.isfile(file_path):
        print("Input is not a file.")
        return

    png_img = Image.open(file_path)
    name, ext = os.path.splitext(file_path)

    if ext != ".png":
        print("Not a PNG file.")
        return

    if png_img.mode in ("RGBA", "P"):
        png_img = png_img.convert("RGB")

    png_img.save(name + str(".jpg"))


def main():
    if len(sys.argv) == 1:
        print("Please enter file path and file name")
        return

    if os.path.isfile(sys.argv[1]):
        convert_to_png(sys.argv[1])
    else:
        png_files = get_png_files(sys.argv[1])

        for file in png_files:
            convert_to_png(sys.argv[1] + "\\" + file)


if __name__ == "__main__":
    main()
