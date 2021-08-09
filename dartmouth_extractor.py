import os
import shutil

# Path to dartmouth dataset
origin = "Path\\to\\dataset_folder"
# Path to where you want to move the photos to
destination = "Path\\to\\destination_folder"

# Walks through every directory within the origin path
for (dirpath, dirnames, filenames) in os.walk(origin):
    for filename in filenames:
        # Checks if the file is a photo 
        if filename.endswith('.jpg') or filename.endswith('.JPG'): 
            print('Moving ' + os.sep.join([dirpath, filename]))
            # Moves the file
            shutil.move(os.sep.join([dirpath, filename]), destination)

print("Extraction Complete")