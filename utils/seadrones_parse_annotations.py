
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
    folder_imageslist_map[folder] = os.listdir(Path(dataset_val_path, folder, 'img'))
    id = int([img for img in images if img['source']['folder_name'] == folder][-1]['video_id'])
    folder_annotations_map[folder] = [ann for ann in annotations if int(ann['video_id']) == id]

# for folder in folders:
#     imgs = [img for img in images if img['source']['folder_name'] == folder]
#     vids = [img['video_id'] for img in imgs]
#     print(set(vids))

# print(folder_imageslist_map)

for folder, img_list in folder_imageslist_map.items():
    print(folder)
    if not os.path.isdir(Path(dataset_val_path, folder, 'gt')):
        os.makedirs(Path(dataset_val_path, folder, 'gt')) 

    ann_list = folder_annotations_map[folder]
    
    track_ids = set([ann['track_id'] for ann in ann_list])
    tracks_map = {}
    for idx, tid in enumerate(sorted(track_ids)):
        tracks_map[tid] = idx + 1

    # if folder == 'DJI_0001':
    #     print(["%d : %d" % (annl['image_id'] , annl['track_id']) for annl in ann_list])
    #     10/0
    with open(Path(dataset_val_path, folder, 'gt', 'gt.txt'), 'w') as gt_fie:
        for idx, img_fname in enumerate(img_list):
            # print(img_fname)
            anns = [ann for ann in ann_list if int(ann['image_id']) == int(img_fname.split('.')[0])]
            for ann in anns:

                try:
                    frame = idx + 1
                    id = tracks_map[ann['track_id']] # tutaj shift musi byc
                    bb_left = ann['bbox'][0]
                    bb_top = ann['bbox'][1]
                    bb_width = ann['bbox'][2]
                    bb_height = ann['bbox'][3]
                    conf = 0
                    class_id = ann['category_id']
                    visibility = 1
                    gt_fie.write("%d, %d, %d, %d, %d, %d, %d, %d, %d\n" % (frame, id, bb_left, bb_top, bb_width, bb_height, conf, class_id, visibility))
                except:
                    print('FAILURE: ',folder, ' ', id, ' ', frame)
                    continue

        
        


    