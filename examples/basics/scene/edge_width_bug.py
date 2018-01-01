# vispy: gallery 10
# Copyright (c) 2015, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

""" Demonstrates use of visual.Markers to create a point cloud with a
standard turntable camera to fly around with and a centered 3D Axis.
"""
import sys
from vispy import scene
from vispy.scene import visuals

#
# Make a canvas and add simple view
#
canvas = scene.SceneCanvas(keys='interactive', show=True, bgcolor='w')

view = canvas.central_widget.add_view()
view.camera = 'arcball'

# create Enceladus
sphere = visuals.Sphere(radius=0.8, color=(0, 0, 1),
                        edge_color=(1, 0, 0), parent=view.scene)

# add a colored 3D axis for orientation
axis = visuals.XYZAxis(parent=view.scene, width=5)


if __name__ == '__main__' and sys.flags.interactive == 0:
    canvas.app.run()
