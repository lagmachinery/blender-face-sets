import bpy

class OT_FaceSet_Delete(bpy.types.Operator):
    bl_idname = "mesh.faceset_delete"
    bl_label = "Face Set Delete"
    bl_description = (
        "Delete Active face map "
    )
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        bpy.ops.geometry.attribute_remove()
        return {"FINISHED"}

