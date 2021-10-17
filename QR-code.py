import pyqrcode
from pyqrcode import *
import png

input_url = input("Put the url which will be then QR-coded : ")

url = pyqrcode.create(input_url)

file_name = input("Write the file name (not to add any extentions EG - .png) : ")
final_file_name = f"{file_name}.png"

print("Done!")

url.png(final_file_name, scale = 6)