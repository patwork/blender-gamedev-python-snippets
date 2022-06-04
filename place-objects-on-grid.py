# arranges all objects on the grid

import math
import bpy

step = 7.0
width = math.floor(math.sqrt(len(bpy.data.objects)))
shift = (step * width) / 2.0

x = 0
y = 0

for o in bpy.data.objects:
    o.location = (x * step - shift, y * step - shift, 0.0)
    o.rotation_euler = (0.0, 0.0, 0.0)
    x = (x + 1) % width
    if x == 0:
        y += 1

# EoF
