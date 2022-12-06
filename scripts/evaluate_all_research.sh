#!/bin/bash
for detector in yolov5m yolov5x yolov7 yolov7x yolor-csp
do
    python yolovx_deepsort_eval.py \
    --config_detection ./configs/$detector.yaml \
    --config_deepsort ./configs/deep_sort.yaml \
    --detect_model $detector \
    --frame_interval 1 \
    --display_width 800 \
    --display_height 600 \
    --save_path ./eval_results/MOT17/$detector
done