import os
import pdb

dataset_name = 'E:/Academic/CS4203 - Research and Development Project/DataSet/Jester/20BN-JESTER/Train'  # Adjusted to your dataset folder name

# Load and process the category labels
with open('labels.csv') as f:
    lines = f.readlines()
categories = []
for line in lines:
    line = line.rstrip()
    categories.append(line)
categories = sorted(categories)
with open('category.txt', 'w') as f:
    f.write('\n'.join(categories))

# Create a dictionary mapping categories to indices
dict_categories = {}
for i, category in enumerate(categories):
    dict_categories[category] = i

# Define input and output files
# files_input = ['Validation.csv', 'Train.csv']
# files_output = ['val_videofolder.txt', 'trainn_videofolder.txt']
files_input = ['Train.csv']
files_output = ['train_videofolder.txt']

for (filename_input, filename_output) in zip(files_input, files_output):
    with open(filename_input) as f:
        lines = f.readlines()
    folders = []
    idx_categories = []
    for line in lines:
        line = line.strip()
        
        # Skip header or empty lines
        if not line or 'video_id' in line:
            continue
            
        items = line.split(',')  # Assuming CSV is comma-separated
        folders.append(items[0])
        idx_categories.append(dict_categories[items[1]])  # Use dict to map label to index

    output = []
    for i in range(len(folders)):
        curFolder = folders[i]
        curIDX = idx_categories[i]
        
        # Counting the number of frames in each video folder
        dir_files = os.listdir(os.path.join(dataset_name, curFolder))
        output.append('%s %d %d' % (curFolder, len(dir_files), curIDX))
        
        print('%d/%d' % (i + 1, len(folders)))
        
    with open(filename_output, 'w') as f:
        f.write('\n'.join(output))
