python yolovx_deepsort_eval.py \
--config_detection ./configs/yolov7crowdhuman.yaml \
--config_deepsort ./configs/deep_sort.yaml \
--detect_model yolov7 \
--frame_interval 1 \
--display_width 800 \
--display_height 600 \
--save_path ./eval_results/yolov7/motr

python yolovx_deepsort_eval.py --config_detection ./configs/yolov7crowdhuman.yaml --config_deepsort ./configs/deep_sort.yaml --detect_model yolov7 --frame_interval 1 --display_width 800 --display_height 600 --save_path ./eval_results/yolov7/motr

python yolovx_deepsort_eval_seadrones.py --config_detection ./configs/yolov7seadrones.yaml --config_deepsort ./configs/deep_sort.yaml --ignore_display --detect_model yolov7 --save_path eval_results/seadrones/yolov7