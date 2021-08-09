# Dartmouth-Extraction-Scripts
Python scripts for extracting images and creating CSV's of the Dartmouth dataset

The completely extracted dataset is in the humanoid robots drive under the Grand Combined Dataset folder

## Manual Fixes for Script Bugs

### Extractor Script
- The 40 Males folder contains duplicates for Mac OS so make sure to remove that or else the script will run into problems.
- The original dataset folder also contains some duplicate edited images named like "left 1.jpg" that needs to be removed manually.
- The script prints out which directory it gets stuck at so finding manually where the files are that need to be deleted should be simple

### CSV Generator Script
- The Dartmouth dataset uses different emotion labels such as "HappyTeeth" that we do not include in our model.
- There were a small amount of images that were not labeled with an emotion
