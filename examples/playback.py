#!/usr/bin/python
## The equivalent of:
##  "Recording and Playing Data (Playing)"
## in the OpenNI user guide.

"""
The following code opens up the recording file created by record.py, 
and takes the depth generator that was created for this purpose. 

It will replay the results of the recorded data, in a loop.
"""


from openni import *
import numpy as np

ctx = Context()
ctx.init()

# Open recording 
ctx.open_file_recording("tempRec.oni")

ctx.start_generating_all()
depth = ctx.find_existing_node(NODE_TYPE_DEPTH)

prev = -1

while depth.frame_id > prev:

    prev = depth.frame_id
    
    # Update to next frame
    nRetVal = ctx.wait_one_update_all(depth)

    depth_map = depth.map

    depth_data = np.array(depth.get_tuple_depth_map())
    depth_data = depth_data.reshape((depth_map.width, depth_map.height))
    print depth_data
