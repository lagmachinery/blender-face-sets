import bpy

class OT_FaceSet_Create(bpy.types.Operator):
    bl_idname = "mesh.faceset_create"
    bl_label = "Face Set Create"
    bl_description = (
        "Create a new boolean face set and set value according to current selection"
    )
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(self, context):
        return context.mode == "EDIT_MESH" and context.active_object.type == "MESH"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        faceset = context.active_object.data.attributes.new(
            name="FaceSet", domain="FACE", type="BOOLEAN"
        )
        for polygon in context.active_object.data.polygons:
            faceset.data[polygon.index].value = polygon.select
        bpy.ops.object.editmode_toggle()

        attrs = context.object.data.attributes
        attrs.active = attrs[-1]


        return {"FINISHED"}
