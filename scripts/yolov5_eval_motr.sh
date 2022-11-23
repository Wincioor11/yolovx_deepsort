python yolovx_deepsort_eval.py \
--config_detection ./configs/yolov5l.yaml \
--config_deepsort ./configs/deep_sort.yaml \
--detect_model yolov5 \
--frame_interval 1 \
--display_width 800 \
--display_height 600 \
--save_path ./eval_results/yolov5/motr

python yolovx_deepsort_eval.py --config_detection ./configs/yolov5l.yaml --config_deepsort ./configs/deep_sort.yaml --detect_model yolov5 --frame_interval 1 --display_width 800 --display_height 600 --save_path ./eval_results/yolov5/motr


python TrackEval/scripts/run_mot_challenge.py \
--BENCHMARK MOT17 \
--SPLIT_TO_EVAL train \
--METRICS HOTA CLEAR Identity VACE \
--USE_PARALLEL False \
--NUM_PARALLEL_CORES 1 \
--GT_FOLDER ./data/dataset/MOT17/images/ \
--TRACKER_FOLDER ./eval_results/ \
--TRACKERS_TO_EVAL yolov7 \
--SEQMAP_FOLDER ./data/dataset/seqmaps/


python scripts/run_mot_challenge.py --BENCHMARK MOT17 --SPLIT_TO_EVAL train --TRACKERS_TO_EVAL MPNTrack --METRICS HOTA CLEAR Identity VACE --USE_PARALLEL False --NUM_PARALLEL_CORES 1  

python TrackEval/scripts/run_mot_challenge.py --BENCHMARK MOT17 --SEQMAP_FOLDER ./data/dataset/seqmaps/ --SPLIT_TO_EVAL train --METRICS HOTA CLEAR Identity VACE --USE_PARALLEL False --NUM_PARALLEL_CORES 1 --GT_FOLDER ./data/dataset/MOT17/images/ --TRACKER_FOLDER ./eval_results/ --TRACKERS_TO_EVAL yolov7

python TrackEval/scripts/run_seadrones.py --BENCHMARK seadrones --SEQMAP_FOLDER ./data/dataset/seqmaps/ --SPLIT_TO_EVAL train --METRICS HOTA CLEAR Identity VACE --USE_PARALLEL False --NUM_PARALLEL_CORES 1 --GT_FOLDER G:\\Datasets\\sea_drones_mot\\val_ --TRACKERS_FOLDER ./eval_results/seadrones --TRACKERS_TO_EVAL yolov7
