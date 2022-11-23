
from contextlib import nullcontext
import json
import os
from pathlib import Path


dataset_val_path = R'G:\Datasets\sea_drones_mot\val_\val'
annotation_val_path = R'G:\Datasets\sea_drones_mot\annotations\instances_val_objects_in_water.json'

images = []
annotations = []
with open(annotation_val_path) as ann_file:
    ann = json.load(ann_file)
    images = ann['images']
    annotations = ann['annotations']



for img in images:
    folder = img['source']['folder_name']
    img_name = img['file_name'] 
    if not os.path.isdir(Path(dataset_val_path, folder, 'img')):
        os.makedirs(Path(dataset_val_path, folder, 'img')) 
        os.makedirs(Path(dataset_val_path, folder, 'det')) 
    os.rename(Path(dataset_val_path, img_name), Path(dataset_val_path, folder, 'img', img_name))
    