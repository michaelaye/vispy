# -*- coding: utf-8 -*-
# vispy: gallery 30
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
"""
This example demonstrates the use of the SurfacePlot visual.
"""

import sys
import numpy as np

from vispy import app, scene, color
from vispy.util.filter import gaussian_filter

import gdal
from pathlib import Path

# read terrain
root = Path('/Users/klay6683/data/hirise/dem/inca')
fulldata = {'dtm': root / 'DTM_Inca_City_ngate_1m_forPDS_no_special.cub',
       'data1': root / 'ESP_022607_0985_REDmos_hijitreged_1m_o_forPDS.cub',
       'data2': root / 'ESP_022699_0985_REDmos_hijitreged_1m_o_forPDS.cub'}
spider = {'dtm': root / 'big_spider_dem.cub',
          'data1': root / 'ESP_022607_0985_cropped_big_spider.cub',
          'data2': root / 'ESP_022699_0985_cropped_big_spider.cub'}





canvas = scene.SceneCanvas(keys='interactive')
view = canvas.central_widget.add_view()
view.camera = scene.TurntableCamera(up='z')

# Simple surface plot example
# x, y values are not specified, so assumed to be 0:50
z = gaussian_filter(np.random.normal(size=(50, 50)), (1, 1)) * 10
p1 = scene.visuals.SurfacePlot(z=z, color=(0.5, 0.5, 1, 1), shading='smooth')
p1.transform = scene.transforms.AffineTransform()
p1.transform.scale([1/49., 1/49., 0.02])
p1.transform.translate([-0.5, -0.5, 0])

view.add(p1)

# Add a 3D axis to keep us oriented
axis = scene.visuals.XYZAxis(parent=view.scene)

if __name__ == '__main__':
    canvas.show()
    if sys.flags.interactive == 0:
        app.run()
