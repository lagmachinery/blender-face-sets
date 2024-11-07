# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Face Maps Legacy, (c) 2024 Tyo 79
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Face Sets",
    "author": "LAGMACHINE, based on work by Tyo79 with contribution from Michel Anders (varkenvarken) Andrew Leichter (aleichter)",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "location": "Properties Panel >  Data > Face Sets",
    "description": "Create, Delete, Assign, Remove, Select, Deselect, Face Sets to Face Selection",
    "warning": "",
    "category": "Mesh",
}

import bpy
from .src.operator_assign import OT_FaceSet_Assign
from .src.operator_create import OT_FaceSet_Create
from .src.operator_delete import OT_FaceSet_Delete
from .src.operator_select import OT_FaceSet_Select
from .src.operator_selections import OT_FaceSet_Selections
from .src.panel import DATA_PT_facesets, MESH_UL_facesets
from .src import panel;

classes = [
    OT_FaceSet_Select,
    OT_FaceSet_Create,
    OT_FaceSet_Delete,
    OT_FaceSet_Assign,
    OT_FaceSet_Selections,
    MESH_UL_facesets,
    DATA_PT_facesets,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    panel.register()


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    panel.unregister()

