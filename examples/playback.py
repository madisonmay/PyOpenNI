#!/usr/bin/python
## The equivalent of:
##  "Recording and Playing Data (Playing)"
## in the OpenNI user guide.

"""
The following code opens up the recording file created by record.py, 
and takes the depth generator that was created for this purpose. 

It will replay the results of the recorded data, in a loop.

if speed is a concern, try compressing the array to smaller images 
for now we'll just work with the huge arrays 

"""


from openni import *
import numpy as np
import time

ctx = Context()
ctx.init()

# Open recording 
ctx.open_file_recording("tempRec.oni")

ctx.start_generating_all()
depth = ctx.find_existing_node(NODE_TYPE_DEPTH)

# frames is a list that stores the depth arrays
frames = []

prev = -1

start = time.time()
print 'start'

while depth.frame_id > prev:

    prev = depth.frame_id
    
    # Update to next frame
    nRetVal = ctx.wait_one_update_all(depth)

    depth_map = depth.map

    depth_data = np.array(depth.get_tuple_depth_map())
    depth_data = depth_data.reshape((depth_map.width, depth_map.height))

    #append data to frames (eventually will be saved to file)
    frames.append(depth_data)

whilelooptime = time.time() - start
print 'done with while loop %d' % whilelooptime

# typecase frames to tuple so we can use np.dstack
frames = tuple(frames)
print len(frames)

# dstacking it
np.dstack(frames)

# save the list of numpy arrays
np.savez("depthdata", frames)
