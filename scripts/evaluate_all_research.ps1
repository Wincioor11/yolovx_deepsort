
# warmup
cmd.exe /c "conda activate yolovxdeepsort & python yolovx_deepsort_eval.py --config_detection ./configs/yolov5l.yaml --config_deepsort ./configs/deep_sort.yaml --detect_model yolov5 --frame_interval 1 --display_width 800 --display_height 600 --save_path ./eval_results/warmup"

# evaluation
# $detectors = "yolov5m", "yolov5x", "yolov7", "yolov7x", "yolor-csp"
$detectors = "yolor-csp"
foreach ($detector in $detectors)
{
cmd.exe /c "conda activate yolovxdeepsort & python yolovx_deepsort_eval.py --config_detection ./configs/research/$detector.yaml --config_deepsort ./configs/deep_sort.yaml --detect_model $detector --frame_interval 1 --display_width 800 --display_height 600 --save_path ./eval_results/MOT17/$detector"
}