
from contextlib import nullcontext
import json
from logging import warn
import os
from pathlib import Path


dataset_val_path = R'G:\Datasets\sea_drones_mot\val_\val'
annotation_val_path = R'G:\Datasets\sea_drones_mot\annotations\instances_val_objects_in_water.json'
oldfilenames_path = R'G:\Datasets\sea_drones_mot\val_\old_filenames.txt'


# <frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <class>, <visibility>

images = []
annotations = []
vid_folder_map = {}
folder_imageslist_map = {}
folder_annotations_map = {}

with open(annotation_val_path) as ann_file:
    ann = json.load(ann_file)
    images = ann['images']
    annotations = ann['annotations']

folders = os.listdir(dataset_val_path)

for folder in folders:
    imageslist= os.listdir(Path(dataset_val_path, folder, 'img'))

    i = 1
    for file in imageslist:
        os.rename( Path(dataset_val_path, folder, 'img', file), Path(dataset_val_path, folder, 'img', "%s.png" % str(i).zfill(6)))
        i+=1