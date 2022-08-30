# sync objects data names
# https://blender.stackexchange.com/questions/158913/how-to-rename-an-objects-mesh-data-with-python

import bpy

for obj in bpy.data.objects:
    if obj.data:
        name = "%s_%s" % (obj.name, obj.type.lower())
        if obj.data.name != name:
            print("- %s -> %s" % (obj.data.name, name))
            obj.data.name = name

# EoF
