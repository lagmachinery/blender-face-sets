import bpy

class OT_FaceSet_Assign(bpy.types.Operator):
    bl_idname = "mesh.faceset_assign"
    bl_label = "Face Set Assign"

    param : bpy.props.StringProperty()

    def execute(self, context):
        obj = context.object
        faceset = context.object.data.attributes.active
        attribute_name = faceset.name

        bpy.ops.object.editmode_toggle()

        if attribute_name in obj.data.attributes:
            attribute = obj.data.attributes[attribute_name]
            for poly in obj.data.polygons:
                if poly.select:
                    if self.param == "Assign":
                        attribute.data[poly.index].value = True
                    if self.param == "Remove":
                        attribute.data[poly.index].value = False

        bpy.ops.object.editmode_toggle()

        return {"FINISHED"}