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
try:
    data = np.load(sys.argv[1])
except IndexError:
    print("Numpy data has to be first argument.")
    sys.exit(-1)
try:
    i = sys.argv[2]
except IndexError:
    i = 0

# scale positions to units of Enceladus radius
data /= 252000

#
# Make a canvas and add simple view
#
canvas = scene.SceneCanvas(keys='interactive', show=True, bgcolor='w')

view = canvas.central_widget.add_view()
# view.camera = 'turntable'
view.camera = 'arcball'
view.camera.fov = 60

# create Enceladus
enc = visuals.Sphere(radius=1, parent=view.scene)

# add a colored 3D axis for orientation
axis = visuals.XYZAxis(parent=view.scene, width=10, scale=-1.1)


# create scatter object and fill in the data
def set_scatters(scatter, i, color=(0, 1, 0, 1)):
    scatter.set_data(data[..., i], edge_color=None,
                     face_color=color, size=5)
    view.add(scatter)

# initial setting:
scatter = visuals.Markers()
if i == 0:
    set_scatters(scatter, i)
else:
    set_scatters(scatter, i, color=(1, 0, 0, 1))


if __name__ == '__main__' and sys.flags.interactive == 0:
    canvas.app.run()
