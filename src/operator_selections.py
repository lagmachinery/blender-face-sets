import bpy

class OT_FaceSet_Selections(bpy.types.Operator):
    bl_idname = "mesh.faceset_selections"
    bl_label = "Face Set Selections"

    param : bpy.props.StringProperty()

    def execute(self, context):
        obj = context.object

        faceset = context.object.data.attributes.active
        attribute_name = faceset.name

        bpy.ops.object.editmode_toggle()

        if attribute_name in obj.data.attributes:
            attribute = obj.data.attributes[attribute_name]
            for poly in obj.data.polygons:
                if attribute.data[poly.index].value:
                    if self.param == "Select":
                        poly.select = True
                    if self.param == "Deselect":
                        poly.select = False
            edge = bpy.context.object.data.edges
            for i in edge:
                i.select = False

        bpy.ops.object.editmode_toggle()

        return {"FINISHED"}