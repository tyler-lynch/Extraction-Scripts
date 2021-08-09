import os
import shutil
import pandas as pd

base_dir = os.path.dirname(__file__)
emotion_path = "C:\\Users\\tyler\\OneDrive\\Desktop\\CK+\\Emotion_labels"
image_path = "C:\\Users\\tyler\\OneDrive\\Desktop\\CK+\\cohn-kanade-images"

picture_list = [] # List for pictures with emotion labels

### CREATING CSV ###

# Grab every emotion label
data_list = []
for (dirpath, dirnames, filenames) in os.walk(emotion_path):
    for filename in filenames:

        # Grabs the emotion files
        if filename.endswith('.txt'): 
            with open(os.sep.join([dirpath, filename]), 'r') as file:
                data = int(file.read().replace('\n', '').strip()[0]) # Converts the txt file to an integer

                file_ID = filename[:-12] + '.png' # Get rid of emotion extention and add image extention

                # Assigns appropriate emotion
                if data == 0:
                    emotion = 'neutral'
                    picture_list.append(file_ID)   
                if data == 1:
                    emotion = 'angry'
                    picture_list.append(file_ID)
                if data == 2:
                    # This emotion label is contempt, which we are not using in our model.
                    break
                if data == 3:
                    emotion = 'disgust'
                    picture_list.append(file_ID)
                if data == 4:
                    emotion = 'fear'
                    picture_list.append(file_ID)
                if data == 5:
                    emotion = 'happy'
                    picture_list.append(file_ID)
                if data == 6:
                    emotion = 'sad'
                    picture_list.append(file_ID)
                if data == 7:
                    emotion = 'surprise'
                    picture_list.append(file_ID)

            
            print('Adding ' + file_ID)
            data_list.append([file_ID, emotion])
                
# Creates dataframe
df = pd.DataFrame(data_list, columns=['file_ID', 'Emotion'])

# Export to csv
df.to_csv('ck_plus.csv')

shutil.move(os.sep.join([base_dir, 'ck_plus.csv']), os.sep.join([base_dir, 'CK+']))

print('CSV Complete')

## Moving images into CK+ folder ##

data_list = []
for (dirpath, dirnames, filenames) in os.walk(image_path):
    for filename in filenames:
        if filename in picture_list:
            shutil.copy(os.sep.join([dirpath, filename]), os.sep.join([base_dir, 'CK+']))

print("Extraction Complete")