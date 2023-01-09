
# warmup
cmd.exe /c "conda activate yolovxdeepsort & python yolovx_deepsort_eval.py --config_detection ./configs/yolov5l.yaml --config_deepsort ./configs/deep_sort.yaml --detect_model yolov5 --frame_interval 1 --display_width 800 --display_height 600 --save_path ./eval_results/warmup --benchmark warmup"

# evaluation
$detectors_left_mot17 = "yolox-s", "yolox-x" #mot17 for yolox
$detectors_coco = "yolov5m", "yolov5x", "yolov7", "yolov7x", "yolor-csp", "yolox-s", "yolox-x"
$detectors_mot15 = "yolov5m", "yolov5x", "yolov7", "yolov7x", "yolor-csp", "yolox-s", "yolox-x"
# $detectors = "yolov5m", "yolov5x", "yolov7", "yolov7x", "yolor-csp"
# $detectors = "yolor-csp"
foreach ($detector in $detectors_left_mot17)
{
cmd.exe /c "conda activate yolovxdeepsort & python yolovx_deepsort_eval.py --config_detection ./configs/research/$detector.yaml --config_deepsort ./configs/deep_sort.yaml --detect_model $detector --frame_interval 1 --display_width 800 --display_height 600 --save_path ./eval_results/MOT17/$detector --benchmark MOT17"
}

foreach ($detector in $detectors_mot15)
{
cmd.exe /c "conda activate yolovxdeepsort & python yolovx_deepsort_eval.py --config_detection ./configs/research/$detector.yaml --config_deepsort ./configs/deep_sort.yaml --detect_model $detector --frame_interval 1 --display_width 800 --display_height 600 --save_path ./eval_results/MOT15/$detector --benchmark MOT15"
}

foreach ($detector in $detectors_coco)
{
cmd.exe /c "conda activate yolovxdeepsort & python yolovx_deepsort_eval.py --config_detection ./configs/coco/$detector.yaml --config_deepsort ./configs/deep_sort.yaml --detect_model $detector --frame_interval 1 --display_width 800 --display_height 600 --save_path ./eval_results/coco/MOT17/$detector --benchmark MOT17"
}

foreach ($detector in $detectors_coco)
{
cmd.exe /c "conda activate yolovxdeepsort & python yolovx_deepsort_eval.py --config_detection ./configs/coco/$detector.yaml --config_deepsort ./configs/deep_sort.yaml --detect_model $detector --frame_interval 1 --display_width 800 --display_height 600 --save_path ./eval_results/coco/MOT15/$detector --benchmark MOT15"
}