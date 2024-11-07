import bpy

class OT_FaceSet_Select(bpy.types.Operator):
    bl_idname = "mesh.faceset_select"
    bl_label = "Face Set Select"
    bl_description = (
        "Select faces based on active face set (+ Shift add to current selection)"
    )
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(self, context):
        return (
                context.mode == "EDIT_MESH"
                and context.active_object.type == "MESH"
                and context.active_object.data.attributes.active is not None
                and context.active_object.data.attributes.active.domain == "FACE"
                and context.active_object.data.attributes.active.data_type == "BOOLEAN"
        )

    def execute(self, context):
        if not self.__shift:
            bpy.ops.mesh.select_all(action="DESELECT")
        attribute_name = context.active_object.data.attributes.active.name
        bpy.ops.object.editmode_toggle()
        for polygon, faceset_attribute in zip(
                context.active_object.data.polygons,
                context.active_object.data.attributes[attribute_name].data,
        ):
            polygon.select |= (
                faceset_attribute.value
            )
        bpy.ops.object.editmode_toggle()
        return {"FINISHED"}

    def invoke(self, context, event):
        self.__shift = event.shift
        return self.execute(context)

