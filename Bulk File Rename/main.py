import os

basedir = input("Directory of Files:> ")
files = os.listdir(basedir)
to_name = input("New name:> ")

counter = 1

for file in files:
	present_filename = os.path.join(basedir, file)
	file_ext = os.path.splitext(present_filename)[1]
	if not os.path.exists(present_filename):
		continue
	to_filename = os.path.join(basedir, f'{counter}{file_ext}')
	print("Renamed from", present_filename)
	print("Renamed to", to_filename)
	os.rename(present_filename, to_filename)
	counter += 1
