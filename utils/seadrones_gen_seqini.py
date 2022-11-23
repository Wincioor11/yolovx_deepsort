
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
    img_ = [img_ for img_ in images if img_['source']['folder_name'] == folder][0]
    ini = """[Sequence]
name=%s
imDir=img
frameRate=30
seqLength=%d
imWidth=%d
imHeight=%d
imExt=.png
""" % (img_['source']['folder_name'], len(imageslist), img_['width'], img_['height'])
    
    with open(Path(dataset_val_path, folder, 'seqinfo.ini'), 'w') as file:
        file.write(ini)

