import os
import sys
from PIL import Image
import piexif


def get_exif(file_path):
    if not os.path.isfile(file_path):
        print("Input is not a file.")
        return

    img = Image.open(file_path)

    # Check if there is EXIF in the file
    if "exif" not in img.info:
        print("No EXIF detected.")
        return

    exif_dict = piexif.load(img.info['exif'])

    name, ext = os.path.splitext(file_path)
    exif_file = open(name + ".exif", "w")
    exif_file.write(str(exif_dict))
    exif_file.close()


def main():
    if len(sys.argv) == 1:
        print("Please enter file path and file name")
        return

    get_exif(sys.argv[1])


if __name__ == "__main__":
    main()
