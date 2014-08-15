# -*- coding: utf-8 -*-
#"""
#Created on Tue Jun 10 19:17:21 2014
#
#@author: julianarhee
#"""
# from image_processing import FindFeatures
#import os
#import matplotlib.pyplot as plt
#import cPickle as pkl
#import numpy as np
#import pandas as pd


# file importing stuff:
#import fnmatch
#import os.path
#import re 
#import itertools
#
#import uuid
#import time


from FeatureFinder import FeatureFinder
import cPickle as pkl
import os.path
import os
import uuid
import time
import numpy as np


class ImageAnalyzer:
    
    def __init__(self, path):
        
        self.folder_key = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time())) + '_' + 'analyzed'
        self.nchuk= 0
        self.chunks_per_dir = 3
        
        self.base_path = os.path.expanduser(path)
        self.base_path += '/' + self.folder_key

        os.makedirs(self.base_path)
        
        self.curr_path = None
        
        self.amplitudes = None
        self.phases = None
    
        
    def listdir_nohidden(self, path): # Should return list of x bins (specified beforehand, e.g., 3)
        dir_list = []
        temp_list = os.listdir(path)
        for f in temp_list:
            if not f.startswith('.'):
                dir_list.append(f)
        
        dir_list = sorted(dir_list, reverse=True)
        return dir_list
    

    def get_datafiles(self, indir, match='*.pkl'):
        dfns = []
        for d, sds, fns in os.walk(indir):
            mfns = fnmatch.filter(fns, match)
            dfns += [os.path.join(d, fn) for fn in mfns]
        return dfns


    def save_bin_dict(self, session_path, bdict):
        if (self.nchunks % self.chunks_per_dir == 0 or
            self.current_path is None):
            
            # Make a new directory of bin chunks:
            self.curr_path = (session_path + '/analyzed/' + '%.10d' % (self.nchunks / self.chunks_per_dir))
            
            os.mkdir(self.curr_path)
        
        bindict = bdict
        bindict['which_bins'] = bdict.keys()
        
        bname = '%s/%i.pkl' % (self.curr_path, chunknum)
        
        with open(bname, 'w') as f:
            self.nchunks += 1
            pkl.dump(bindict, f)
            
            
    def get_binned_frames(self, session_path): # uniqe path to session create by ImageDumper
    
        ''' Input: folder name of 1 session (contains multiple bins of frames)
            Output: dict with keys=frame_numbers, values=arrays of corresponding frame
            
            data_dir = /Users/julianarhee/.camera_capture/data '''
        
        #path_to_bin = os.path.join(data_dir, session_path)
        bin_list = self.listdir_nohidden(path_to_bin)
        
        bin_paths = [os.path.join(data_dir, session_path, b) for b in bin_list]    
        #print bin_paths

        
        
            
            
            
            
        session_frames = {}    
        
        dicts_by_bin = {}
        for i,bin in enumerate(bin_paths):
            tmp_fnames = get_datafiles(bin, match='*.pkl')
            tmp_fdicts = [pkl.load(open(f)) for f in tmp_fnames]
            names = [os.path.splitext(os.path.basename(f)) for f in tmp_fnames]
            timestamps = [f[0] for f in names]
            whichbin = os.path.splitext(os.path.basename(bin))[0]
            try:
                #imarrays = [i['im_array'] for i in tmp_fdicts]
                dicts_by_bin[whichbin] = tmp_fdicts
                for d in tmp_fdicts:            
                    session_frames[d['frame_number']] = d['im_array']
            except ValueError:
                print "No imarray in:  %s" % timestamps[i]
            
        return session_frames, dicts_by_bin
    
    
    
    
    def analyze_image(self, image):
        
        self.analysis = {'amplitudes': pupil,
                         'phases': cr,
                         'nframes': pupil,
                         'frame_at_peak': cr,
                         'array_shape': image.shape,
                        }
        
        
    def get_results(self):
        return self.analysis