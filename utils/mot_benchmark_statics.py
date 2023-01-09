

MOT17_test_seqs = '''MOT17-01-DPM
            MOT17-01-FRCNN
            MOT17-01-SDP
            MOT17-03-DPM
            MOT17-03-FRCNN
            MOT17-03-SDP
            MOT17-06-DPM
            MOT17-06-FRCNN
            MOT17-06-SDP
            MOT17-07-DPM
            MOT17-07-FRCNN
            MOT17-07-SDP
            MOT17-08-DPM
            MOT17-08-FRCNN
            MOT17-08-SDP
            MOT17-12-DPM
            MOT17-12-FRCNN
            MOT17-12-SDP
            MOT17-14-DPM
            MOT17-14-FRCNN
            MOT17-14-SDP
            '''        
MOT17_train_seqs = '''MOT17-02-DPM
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
MOT17_data_root = 'data/dataset/MOT17/images/'

MOT15_train_seqs = '''ADL-Rundle-6
ADL-Rundle-8
ETH-Bahnhof
ETH-Pedcross2
ETH-Sunnyday
KITTI-13
KITTI-17
PETS09-S2L1
TUD-Campus
TUD-Stadtmitte
Venice-2
'''

MOT15_test_seqs = '''ADL-Rundle-1
ADL-Rundle-3
AVG-TownCentre
ETH-Crossing
ETH-Jelmoli
ETH-Linthescher
KITTI-16
KITTI-19
PETS09-S2L2
TUD-Crossing
Venice-1
'''

MOT15_data_root = 'data/dataset/MOT15/'

MOT20_train_seqs = '''MOT20-01
MOT20-02
MOT20-03
MOT20-05
'''

MOT20_test_seqs = '''MOT20-04
MOT20-06
MOT20-07
MOT20-08
'''

MOT20_data_root = 'data/dataset/MOT20/'

warmup_seqs = '''ADL-Rundle-6
ADL-Rundle-8
'''
warmup_data_root = 'data/dataset/MOT15/'


def get_train_seqs(benchmark):
    if benchmark is 'MOT15':
        return MOT15_train_seqs
    elif benchmark is 'MOT17':
        return MOT17_train_seqs
    elif benchmark is 'MOT20':
        return MOT20_train_seqs
    elif benchmark is 'warmup':
        return warmup_seqs
    else: 
        return ''

def get_test_seqs(benchmark):
    if benchmark is 'MOT15':
        return MOT15_test_seqs
    elif benchmark is 'MOT17':
        return MOT17_test_seqs
    elif benchmark is 'MOT20':
        return MOT20_test_seqs
    elif benchmark is 'warmup':
        return warmup_seqs
    else: 
        return ''

def get_data_root(benchmark):
    if benchmark is 'MOT15':
        return MOT15_data_root
    elif benchmark is 'MOT17':
        return MOT17_data_root
    elif benchmark is 'MOT20':
        return MOT20_data_root
    elif benchmark is 'warmup':
        return warmup_data_root
    else: 
        return ''