from ctypes import resize
from PIL import Image

def resize_image(size1, size2):

    input_open = input('Name for picture you wanna change the size: ') #search for name with input from user
    image = Image.open(input_open)

    print(f"Current size : {image.size}")

    resize_image = image.resize((size1, size2))

    input_save = input("Fill name for image you saved: ") # input user for saved picture
    input_fototype = input("Write type of new picture: ") # input fomrat for picture

    resize_image.save(input_save+str(size1)+'.'+input_fototype)

    print(f"Changed Size become: {resize_image.size}")


size1 = int(input('Input width of new picture: '))
size2 = int(input('Input length of new picture: '))

resize_image(size1, size2)
