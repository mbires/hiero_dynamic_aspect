# -*- coding: utf-8 -*-

import nuke
import os

from hiero.ui import registerAction

if nuke.NUKE_VERSION_MAJOR > 15:
    from PySide6.QtGui import QIcon, QAction
else:
    from PySide2.QtGui import QIcon
    from PySide2.QtWidgets import QAction

gizmo_path = os.path.dirname(__file__)
nuke.pluginAddPath(gizmo_path)

try:
    nuke.load("{}/{}".format(gizmo_path, 'MB_DynamicAspect.gizmo'))
    print("DynamicAspect gizmo loaded")
except Exception as e:
    print(f"Failed to load gizmo: {e}")

# This creates an action with an icon and effect
aspect_mask = QAction(QIcon("icons:LUT.png"), "MB_DynamicAspect", None)

# Soft effect actions can be found by prefixing the QAction's objectName with: 'foundry.timeline.effect'
aspect_mask.setObjectName("foundry.timeline.effect.MB_DynamicAspect")
aspect_mask.setData('MB_DynamicAspect')

# This registers your custom action with the Effects Menu
registerAction(aspect_mask)
