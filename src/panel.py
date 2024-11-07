import bpy
from bpy.types import Menu, Panel, UIList
from .operator_create import OT_FaceSet_Create
from .operator_select import OT_FaceSet_Select
from . import utils

class MESH_UL_facesets(UIList):
    def filter_items(self, context, data, propname):
        items = getattr(data, propname)

        flt_flags = [self.bitflag_filter_item if utils.attr_is_faceset(item) else 0 for item in items]
        return flt_flags, []

    def draw_item(self, _context, layout, _data, item, icon, _active_data, _active_propname, _index,):

        fmap = item
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(fmap, "name", text="", emboss=False, icon='FACE_MAPS')

        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)


class DATA_PT_facesets(Panel):
    bl_label = "Face Sets"
    bl_space_type = 'PROPERTIES'
    bl_context = 'data'
    bl_region_type = 'WINDOW'
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_EEVEE', 'BLENDER_WORKBENCH', 'BLENDER_WORKBENCH_NEXT'}

    @classmethod
    def poll(cls, context):
        obj = context.object
        return (obj and obj.type == 'MESH' and context.mode == "EDIT_MESH")

    def draw(self, context):
        layout = self.layout

        ob = context.object
        mesh = context.mesh
        attributes = context.object.data.attributes

        face_maps = [att for att in attributes if utils.attr_is_faceset(att)]

        faceset = mesh.attributes.active
        rows = 2
        if faceset:
            rows = 4

        row = layout.row()
        row.template_list("MESH_UL_facesets", "", ob.data, "attributes", ob.data.attributes, "active_index", rows=rows)

        col = row.column(align=True)
        col.operator("mesh.faceset_create", icon='ADD', text="")
        col.operator("mesh.faceset_delete", icon='REMOVE', text="")

        if len(face_maps)>0 and (ob.mode == 'EDIT' and ob.type == 'MESH'):
           row = layout.row()

           sub = row.row(align=True)
           sub.operator("mesh.faceset_assign", text="Assign").param = "Assign"
           sub.operator("mesh.faceset_assign", text="Remove").param = "Remove"

           sub = row.row(align=True)
           sub.operator("mesh.faceset_selections", text="Select").param = "Select"
           sub.operator("mesh.faceset_selections", text="Deselect").param = "Deselect"


def menu_func(self, context):
    self.layout.separator()
    self.layout.operator(OT_FaceSet_Select.bl_idname, text="From faceset")
    self.layout.operator(OT_FaceSet_Create.bl_idname, text="Create faceset")

def register():
    bpy.types.VIEW3D_MT_select_edit_mesh.append(menu_func)

def unregister():
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(menu_func)