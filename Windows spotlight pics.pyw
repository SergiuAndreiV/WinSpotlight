from shutil import copytree
import os
import sys


# user of the current session
user_profile = os.environ.get("USERPROFILE")

# path to the windows spotlight pics
image_location = user_profile + r"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"

destination_folder = user_profile + r"\Desktop\Windows spotlight pics"

# original lengt of the path
dest_fold_len = len(destination_folder)


def copy_raw_pics():
	# copy pics from win folder to Desktop
	copytree(image_location, destination_folder)


def rename():
	inc = 0
	for filename in os.listdir(destination_folder):
		inc += 1
		stri = str(inc)
		full_name = os.path.join(destination_folder, filename)

		# ignore small photos
		if os.path.getsize(full_name) > 99000:
			# print(os.path.getsize(full_name))
			try:
				output = os.rename(full_name, destination_folder + "\win_spot_" + stri + ".jpg")	
			except FileNotFoundError:
				print(filename)
		else:
			os.remove(full_name)


inc = 0	


def create_new_folder(destPath):
	global inc, destination_folder
	if os.path.exists(destPath):
		inc += 1

		# slice original folder name.
		origName = destination_folder[:dest_fold_len]

		# increment by 1 the original folder name
		destination_folder = origName + " " + str(inc)

		# recursive call till folder name dose not exists
		create_new_folder(destination_folder)

	# copy to the new folder
	else:
		copy_raw_pics()
		rename()


create_new_folder(destination_folder)
print(destination_folder)

# copy_raw_pics()
# rename()
