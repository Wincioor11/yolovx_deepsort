import os
import os.path as osp
import logging
import argparse
from pathlib import Path

from utils.log import get_logger
from deepsort import VideoTracker
from utils.parser import get_config

import motmetrics as mm
mm.lap.default_solver = 'lap'

def mkdir_if_missing(dir):
    os.makedirs(dir, exist_ok=True)

def main(data_root='', seqs=('',), args=""):
    logger = get_logger()
    logger.setLevel(logging.INFO)
    # data_type = 'mot'
    # result_root = os.path.join(Path(data_root), "train", "mot_results", args.detect_model)
    # mkdir_if_missing(result_root)

    cfg = get_config()
    cfg.merge_from_file(args.config_detection)
    cfg.merge_from_file(args.config_deepsort)
    cfg.DETECT_MODEL = args.detect_model
    cfg.USE_FASTREID = args.fastreid
    cfg.SEQ_IDX = 0
    # run tracking
    accs = []
    for seq in seqs:
        logger.info('[{}] start seq: {}'.format(cfg.SEQ_IDX, seq))
        # result_filename = os.path.join(result_root, '{}.txt'.format(seq))
        video_path = data_root+"/train/"+seq+"/img1/%06d.jpg"
        # video_path = data_root+"/"+seq+"/seqinfo.ini"
        with VideoTracker(cfg, args, video_path) as vdo_trk:
            vdo_trk.run()
        cfg.SEQ_IDX +=1

        # # eval
        # logger.info('Evaluate seq: {}'.format(seq))
        # evaluator = Evaluator()
        # evaluator.run("MOT17", data_root, result_root, args.save_path,
        # "train", "/utils/MOTChallengeEvalKit/seqmaps")

    logger.info('Finished! Now you can run the TrackEval to evaluate the results using known metrics :)')

    # eval
    logger.info('Evaluate...')
    # evaluator = Evaluator()
    # evaluator.run("MOT17", data_root, args.save_path, args.save_path,
    # "train", ".\\utils\\MOTChallengeEvalKit\\seqmaps")

    # # get summary
    # metrics = mm.metrics.motchallenge_metrics
    # mh = mm.metrics.create()
    # summary = Evaluator.get_summary(accs, seqs, metrics)
    # strsummary = mm.io.render_summary(
    #     summary,
    #     formatters=mh.formatters,
    #     namemap=mm.io.motchallenge_metric_names
    # )
    # print(strsummary)
    # Evaluator.save_summary(summary, os.path.join(result_root, 'summary_global.xlsx'))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_detection", type=str, default="./configs/yolov3.yaml")
    parser.add_argument("--config_deepsort", type=str, default="./configs/deep_sort.yaml")
    parser.add_argument("--ignore_display", dest="display", action="store_false", default=False)
    parser.add_argument("--detect_model", type=str, default="yolov3")
    parser.add_argument("--fastreid", action="store_true")
    parser.add_argument("--frame_interval", type=int, default=1)
    parser.add_argument("--display_width", type=int, default=800)
    parser.add_argument("--display_height", type=int, default=600)
    parser.add_argument("--save_path", type=str, default="./demo")
    parser.add_argument("--cpu", dest="use_cuda", action="store_false", default=True)
    parser.add_argument("--camera", action="store", dest="cam", type=int, default="-1")
    parser.add_argument("--speed_measure", action="store_true")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    # seqs_str = '''MOT17-01-DPM
    #             MOT17-01-FRCNN
    #             MOT17-01-SDP
    #             MOT17-03-DPM
    #             MOT17-03-FRCNN
    #             MOT17-03-SDP
    #             MOT17-06-DPM
    #             MOT17-06-FRCNN
    #             MOT17-06-SDP
    #             MOT17-07-DPM
    #             MOT17-07-FRCNN
    #             MOT17-07-SDP
    #             MOT17-08-DPM
    #             MOT17-08-FRCNN
    #             MOT17-08-SDP
    #             MOT17-12-DPM
    #             MOT17-12-FRCNN
    #             MOT17-12-SDP
    #             MOT17-14-DPM
    #             MOT17-14-FRCNN
    #             MOT17-14-SDP
    #             '''        
    seqs_str = '''MOT17-02-DPM
                MOT17-02-FRCNN
                MOT17-02-SDP
                MOT17-04-DPM
                MOT17-04-FRCNN
                MOT17-04-SDP
                MOT17-05-DPM
                MOT17-05-FRCNN
                MOT17-05-SDP
                MOT17-09-DPM
                MOT17-09-FRCNN
                MOT17-09-SDP
                MOT17-10-DPM
                MOT17-10-FRCNN
                MOT17-10-SDP
                MOT17-11-DPM
                MOT17-11-FRCNN
                MOT17-11-SDP
                MOT17-13-DPM
                MOT17-13-FRCNN
                MOT17-13-SDP
                '''   
    data_root = 'data/dataset/MOT17/images/'
    # data_root = 'data/dataset/MOT17/images/'

    seqs = [seq.strip() for seq in seqs_str.split()]

    main(data_root=data_root,
         seqs=seqs,
         args=args)