python TrackEval/scripts/run_mot_challenge.py --BENCHMARK MOT17 --SEQMAP_FOLDER ./data/dataset/seqmaps/ --SPLIT_TO_EVAL train --METRICS HOTA CLEAR Identity VACE --USE_PARALLEL True --NUM_PARALLEL_CORES 5 --GT_FOLDER ./data/dataset/MOT17/images/ --TRACKERS_FOLDER ./eval_results/MOT17 --TRACKERS_TO_EVAL yolov5m yolov5x yolov7 yolov7x yolor-csp


python TrackEval/scripts/run_mot_challenge.py --BENCHMARK MOT17 --SEQMAP_FOLDER ./data/dataset/seqmaps/ --SPLIT_TO_EVAL train --METRICS HOTA CLEAR Identity VACE --USE_PARALLEL True --NUM_PARALLEL_CORES 1 --GT_FOLDER ./data/dataset/MOT17/images/ --TRACKERS_FOLDER   --TRACKERS_TO_EVAL yolor-csp
