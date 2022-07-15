# from pylabel import importer
from __future__ import annotations
from email.mime import image
from genericpath import isdir
from itertools import groupby
import json
from os import mkdir

dataset_path = 'G:\Datasets\sea_drones_see_detection\\'

annotations_train_path = '%sannotations\\instances_train.json' % dataset_path
annotations_test_path = '%sannotations\\instances_val.json' % dataset_path

labels_path = '%slabels' % dataset_path
labels_train_path = '%s\\train' % labels_path
labels_test_path = '%s\\val' % labels_path

classes_path = '%sclasses.txt' % dataset_path




# https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data

COCO_FORMAT = '{class_id} {x_center} {y_center} {width} {height}\n'

groupby_image_id = lambda obj : obj['image_id']
groupby_id = lambda obj : obj['id']

json2coco = lambda annotation, image : COCO_FORMAT.format(
        class_id=int(annotation['category_id'])-1, 
        # x_center=float(annotation['bbox'][0])/float(image['width']), 
        x_center=(float(annotation['bbox'][0]) + float(annotation['bbox'][2])/2.0 )/float(image['width']), 
        # y_center=float(annotation['bbox'][1])/float(image['height']), 
        y_center=(float(annotation['bbox'][1]) + float(annotation['bbox'][3])/2.0 )/float(image['height']), 
        width=float(annotation['bbox'][2])/float(image['width']), 
        height=float(annotation['bbox'][3])/float(image['height']) 
    )

def parse_sea_drones_to_coco_labels(json, output_labels_dir):
    annotations = list(json['annotations'])
    images = {} 
    for img, details in groupby(json['images'], groupby_id):
        images[img] = list(details)[0]

    for image_id, annotations_ in groupby(annotations, groupby_image_id):
        with open('%s\\%d.txt' % (output_labels_dir, image_id), 'w') as im_file:
            im_file.writelines([ json2coco(dict(annotation), images[image_id]) for annotation in list(annotations_) ])

def parse_classes(json, output_file):
    categories = json['categories']
    categories = sorted(categories, key=id)
    with open(output_file, 'w') as file:
        file.writelines([ item['name'] + '\n' for item in categories ])


def main():
    if not isdir(labels_path):
        mkdir(labels_path)
        mkdir(labels_train_path)
        mkdir(labels_test_path)

    for annotations, labels in [(annotations_train_path,labels_train_path), (annotations_test_path,labels_test_path)]:
        with open(annotations, 'r') as ann_file:
            parse_sea_drones_to_coco_labels(json.load(ann_file), labels)

    with open(annotations_train_path, 'r') as ann_file:
        parse_classes(json.load(ann_file), classes_path)

if __name__ == '__main__':
    main()