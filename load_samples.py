import numpy as np
import inspect
import os
ev_dir  = os.path.dirname(inspect.getfile(inspect.currentframe()))

ev_params = ['mchirp', 'eta', 's1z', 's2z', 'RA', 'DEC',
             'psi', 'iota', 'vphi', 'tc', 'DL']
events = [
    'GW151216',
    
    'GW170121', 'GW170202', 'GW170304', 'GW170425', 'GW170727', 'GW170403', 
    
    'GW150914', 'GW151226', 'GW170104', 'GW170608', 'GW170729',
    'GW170809', 'GW170814', 'GW170818', 'GW170823', 'GW151012',
    
    'GW170817A',
]

def load_samples(events=events, ev_dir=ev_dir):
    ev_samples_dic = {}
    for ev in events:
        ev_samples_dic[ev] = dict(zip(ev_params, np.load(f'{ev_dir}/{ev}.npy').T))
    return ev_samples_dic

t_gps = {
'GW151216': 1134293073.164,
'GW170121': 1169069154.565,
'GW170202': 1170079035.715,
'GW170304': 1172680691.356,
'GW170425': 1177134832.178,
'GW170727': 1185152688.019,
'GW170403': 1175295989.221,
'GW150914': 1126259462.411,
'GW151226': 1135136350.585,
'GW170104': 1167559936.582,
'GW170608': 1180922494.5,
'GW170729': 1185389807.311,
'GW170809': 1186302519.740,
'GW170814': 1186741861.519,
'GW170818': 1187058327.075,
'GW170823': 1187529256.500,
'GW151012': 1128678900.428,
'GW170817A': 186974184.716,
}