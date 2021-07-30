import os
import sys
from PIL import Image

EXTENSIONS = ('.JPG', '.PNG', '.GIF')

def resize_image(name, width, height):
	img = Image.open(name)
	new_img = img.resize((width, height), Image.ANTIALIAS)
	new_img.save("Resized_"+img.filename)
	print("Image saved as: Resized_" + img.filename)

if len(sys.argv) == 4:
	try:
		img_name = sys.argv[1]
		width = int(sys.argv[2])
		height = int(sys.argv[3])
		if img_name == ".":
			for file in os.listdir():
				if os.path.splitext(file)[1].upper() in EXTENSIONS:
					resize_image(file, width, height)
		else:
			resize_image(img_name, width, height)
	except FileNotFoundError:
		print("File doesn't exist or isn't in this folder.")
	except ValueError:
		print("Invalid width and height provided.")
		print("Make sure no comma is added")
		print("python script.py <filename> <img-width> <img-height>")
	except OSError:
		print("Error resizing the file.")
	except Exception as e:
		print("Error resizing the file. Report to developer.")
else:
	print("Run the code in this format:")
	print("python script.py <filename> <img-width> <img-height>")
