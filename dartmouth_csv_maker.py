import csv
import os
import shutil
import pandas as pd
import re

origin = "Path\\to\\extracted_photos"

# Create dataframe
data = [] # List of lists to hold each row of data for the dataframe
for (dirpath, dirnames, filenames) in os.walk(origin):
    for filename in filenames:
        # Find gender
        if "M" in filename: 
            gender = 'M'
        if "F" in filename: 
            gender = 'F'

        # Finds age in file name
        age = re.findall('[0-9]+', filename)[1]

        # Finds emotion from filename
        emotion = re.findall('[A-z]+', filename)[2][4:]
        emotion = emotion.split('_')[0]

        # Creates data for the dataframe
        data.append([filename, age, emotion, gender])

# Creates dataframe
df = pd.DataFrame(data, columns=['file_ID', 'Age', 'Emotion', 'Gender'])

# Export to csv
df.to_csv('dartmouth_v2.csv')
