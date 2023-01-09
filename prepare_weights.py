import os
from pathlib import Path

PATHS_FILE = 'weight-filepaths-coco.txt'
# WEIGHTS_FOLDER = 'detector_weights'
WEIGHTS_FOLDER = 'detector_weights_coco'

GPU_SERVER_ROOT = 'winciorek@10.44.60.20:'

full_paths = []

with open(PATHS_FILE, 'r') as file:
    full_paths = list([line.replace('\n', '') for line in file.readlines() if line not in  ["\n", ""]])


for path in full_paths:
    path_splitted = path.split('/')
    model = path_splitted[4]
    # epochs = path_splitted[7]
    if 'coco' in WEIGHTS_FOLDER:
        if len(path_splitted) > 6:
            name = path_splitted[4]
            filename = path_splitted[6]
        else:
            name = path_splitted[4]
            filename = path_splitted[5]
    elif len(path_splitted) > 8:
        name = path_splitted[7]
        filename = path_splitted[9]
    else:
        name = path_splitted[6]
        filename = path_splitted[7]
    # print(path.split('/'))

    ### SCP - copy weights
    dest_dir = Path(WEIGHTS_FOLDER, model, name)
    os.makedirs(dest_dir, exist_ok=True)
    os.system('scp %s%s %s/%s' % (GPU_SERVER_ROOT, path, dest_dir, filename))

    ### Create config file

    ### Create eval .sh file
