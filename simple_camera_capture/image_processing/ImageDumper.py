from FeatureFinder import FeatureFinder
import cPickle as pkl
import os.path
import os
import uuid
import time
import numpy as np

import sys

class ImageDumper:

    def __init__(self, path):
        num = 1
        message = sys.stdin.read()
        sys.stdin = open('/dev/tty')
        self.session_name = raw_input('Enter session name: ')

        # self.session_key = time.strftime('%Y-%m-%d-%H%M-%S',time.localtime(time.time())) + '_' + str(uuid.uuid1())
        #self.session_key = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
        self.n_frames = 0
        self.frames_per_dir = 1000

        self.base_path = os.path.expanduser(path)
        self.base_path += '/' + self.session_name

        try:
            num += 1
            os.makedirs(self.base_path)
        except OSError:
            self.base_path += str(num)
            os.makedirs(self.base_path)

        self.current_path = None
        self.subname = 'default'

        self.im_array = None

        self.recording = 0
        print "CREATED IT!"


    def status(self):

        if self.recording == 1:
            return 1
        else:
            self.current_path = None
            self.n_frames = 0
            return 0

    def save_image(self, fdict):

        # if self.subname is None:
        #     self.subname = 'default'

        if (self.n_frames % self.frames_per_dir == 0 or
            self.current_path is None):

            # make a new directory
            self.session_key = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
            #self.base_path += '/' + self.session_key
            self.current_path = (self.base_path + '/' + self.subname + '_' + 
                                self.session_key + '_' + '%.10d' % (self.n_frames / self.frames_per_dir))

            os.mkdir(self.current_path)

        fname = '%s/%i.pkl' % (self.current_path,
                                   int(fdict['timestamp'] * 1000.))

        with open(fname, 'wb') as f:
            self.n_frames += 1
            pkl.dump(fdict, f)
            # pkl.dump(image.astype('>u1'), f)


