
# coding: utf-8

# In[1]:

# %load enceladus_jets.py
# vispy: gallery 10
# Copyright (c) 2015, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

""" Demonstrates use of visual.Markers to create a point cloud with a
standard turntable camera to fly around with and a centered 3D Axis.
"""

import sys
import numpy as np
from vispy import scene
from vispy.scene import visuals

# read in particle data
data = np.load('/Users/klay6683/Dropbox/SternchenAndMe/Enceladus_stuff/jet_run_15000_20h33m39_p.dat')
# scale positions to units of Enceladus radius
data /= 252000 

#
# Make a canvas and add simple view
#
canvas = scene.SceneCanvas(keys='interactive', show=True, bgcolor='w')

view = canvas.central_widget.add_view()

view.camera = 'arcball'
view.camera.fov = 30
enc = visuals.Sphere(radius=1, parent=view.scene)

# add a colored 3D axis for orientation
# axis = visuals.XYZAxis(parent=view.scene, width=10, scale=-1.1)

# create scatter object and fill in the data
def set_scatters(scatter, i, color=(0,1,0,0.5)):
    scatter.set_data(data[..., i], edge_color=None,
                     face_color=color, size=5)
    view.add(scatter)

# initial setting:
scatter = visuals.Markers()
set_scatters(scatter, 0)

# scatter2 = visuals.Markers()
# set_scatters(scatter2, 1, color=(1,0,0,0.5))

# view.camera.zoom_factor /= 10

if __name__ == '__main__' and sys.flags.interactive == 0:
    canvas.app.run()


# In[1]:

import sys
import numpy as np
from vispy import scene
from vispy.scene import visuals

# read in particle data
data = np.load('/Users/klay6683/Dropbox/SternchenAndMe/Enceladus_stuff/jet_run_15000_20h33m39_p.dat')
# scale positions to units of Enceladus radius
data /= 252000 

#
# Make a canvas and add simple view
#
canvas = scene.SceneCanvas(keys='interactive', show=True, bgcolor='w')

view = canvas.central_widget.add_view()

view.camera = 'arcball'
view.camera.fov = 30
enc = visuals.Sphere(radius=1, parent=view.scene)

# add a colored 3D axis for orientation
# axis = visuals.XYZAxis(parent=view.scene, width=10, scale=-1.1)

# create scatter object and fill in the data
def set_scatters(scatter, i, color=(0,1,0,0.5)):
    scatter.set_data(data[..., i], edge_color=None,
                     face_color=color, size=5)
    view.add(scatter)

# initial setting:
scatter = visuals.Markers()
set_scatters(scatter, 0)

# scatter2 = visuals.Markers()
# set_scatters(scatter2, 1, color=(1,0,0,0.5))

# view.camera.zoom_factor /= 10

if __name__ == '__main__' and sys.flags.interactive == 0:
    canvas.app.run()


# In[10]:

view._subvisuals


# In[3]:

get_ipython().magic('pinfo scatter.set_data')


# In[4]:

get_ipython().magic('pinfo view.remove_subvisual')


# In[ ]:



