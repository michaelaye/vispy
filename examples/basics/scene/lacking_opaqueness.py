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

# create particle data

z = np.linspace(0.8, 2, 100)
x = np.zeros_like(z)
y = np.zeros_like(z)

data = np.vstack([x, y, z]).T
#
# Make a canvas and add simple view
#
canvas = scene.SceneCanvas(keys='interactive', show=True, bgcolor='w')

view = canvas.central_widget.add_view()
# view.camera = 'turntable'
view.camera = 'arcball'
view.camera.fov = 60

# create Enceladus
enc = visuals.Sphere(radius=0.8, color=(0, 0, 1),
                     edge_color=(1, 0, 0), parent=view.scene)

# add a colored 3D axis for orientation
axis = visuals.XYZAxis(parent=view.scene, width=1)

scatter = visuals.Markers(depth_test=True)

scatter.set_data(data, edge_color=None, face_color=(0.6, 0.5, 0.4), size=5)

view.add(scatter)


if __name__ == '__main__' and sys.flags.interactive == 0:
    canvas.app.run()
