import os
import shutil
import pandas as pd

base_dir = os.path.dirname(__file__)
emotion_path = r"C:\Users\tyler\OneDrive\Desktop\Fer2013"

emotion_list = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

data_list = []
for (dirpath, dirnames, filenames) in os.walk(emotion_path):
    for dirname in dirnames:
        if dirname in emotion_list:
            for file in os.listdir(os.sep.join([dirpath, dirname])):
                data_list.append([file, dirname])

df = pd.DataFrame(data_list, columns=['file_ID', 'Emotion'])

# Export to csv
df.to_csv('fer2013.csv')
