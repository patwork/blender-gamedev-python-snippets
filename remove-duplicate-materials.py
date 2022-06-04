# https://blender.stackexchange.com/questions/91378/prevent-blender-to-add-numbers-behind-materials-when-importing-a-fbx

import bpy

# clean names for base materials
for m in bpy.data.materials:
    parts = m.name.rpartition('.')
    if parts[2].isnumeric():
        primary = bpy.data.materials.get(parts[0])
        if not primary:
            print('renaming %s to %s' % (m.name, parts[0]))
            m.name = parts[0]

# remap materials in slots
for o in bpy.data.objects:
    for s in o.material_slots:
        parts = s.name.rpartition('.')
        if parts[2].isnumeric():
            m = bpy.data.materials.get(parts[0])
            assert(m)
            print('remap %s to %s in %s' % (s.name, m.name, o.name))
            s.material = m

# EoF
