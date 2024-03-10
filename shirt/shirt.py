import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')

    # Open shirt
    shirtfile = Image.open('shirt.png')

    # Get the size of the shirt
    size = shirtfile.size

    # Resize photo image to fit shirt
    photo = ImageOps.fit(imagefile, size)

    # Past shirt in photo
    photo.paste(shirtfile, shirtfile)

    # Criate output image
    photo.save(sys.argv[2])


def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.argv('Too many command-line arguments')
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if check_extension(file1[1]) == False:
        sys.exit('Invalid imput')
    if check_extension(file2[1]) == False:
        sys.exit('Invalid output')

    if file1[1].lower() != file2[1].lower():
        sys.exit('Input and output have different extensions')


def check_extension(file):
    if file in ['.jpg', '.jpeg', '.png']:
        return True
    return False

main()