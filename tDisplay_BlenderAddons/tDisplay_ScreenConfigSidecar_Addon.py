bl_info = {
    "name:": "VP Volume Screen Config Sidecar",
    "description": "Add metadata for virutal production volume screen meshes for tDisplay.",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "category": "3D View",
}

import bpy
from bpy.types import Operator
from bpy.types import Panel
import csv
import os.path


def rename_active_mesh(active_obj, new_name):
    if active_obj.type == "MESH":
        active_obj.name = new_name


def check_if_config_filename_ends_with_csv(config_filename):
    if config_filename.endswith(".csv"):
        return config_filename

    return config_filename + ".csv"


def save_active_mesh_as_obj(active_obj):
    if active_obj.type == "MESH":
        file_name = active_obj.name + ".obj"
        file_path = os.path.join(
            os.path.dirname(bpy.data.filepath), "Screen_OBJs", file_name
        )

        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        bpy.ops.export_scene.obj(
            filepath=file_path,
            check_existing=True,
            filter_glob="*.obj;*.mtl",
            use_selection=True,
            use_animation=False,
            use_mesh_modifiers=True,
            use_edges=True,
            use_smooth_groups=False,
            use_smooth_groups_bitflags=False,
            use_normals=True,
            use_uvs=True,
            use_materials=False,
            use_triangles=False,
            use_nurbs=False,
            use_vertex_groups=False,
            use_blen_objects=True,
            group_by_object=False,
            group_by_material=False,
            keep_vertex_order=False,
            global_scale=1,
            path_mode="AUTO",
            axis_forward="-Z",
            axis_up="Y",
        )
        return file_path


class VPScreenConfigSideCar(Operator):
    """Save to screen config and rename the mesh to screen name."""

    bl_idname = "opr.vp_screen_config_sidecar"
    bl_label = "Save config for this screen and rename its mesh?"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        screen_name = str(context.scene.screen_name)
        resolution_x = str(context.scene.resolution_x)
        resolution_y = str(context.scene.resolution_y)
        config_filename = str(context.scene.config_filename)

        config_filename = check_if_config_filename_ends_with_csv(config_filename)
        working_dir = os.path.dirname(bpy.data.filepath)
        config_filename = os.path.join(working_dir, config_filename)

        rename_active_mesh(bpy.context.active_object, screen_name)
        obj_path = save_active_mesh_as_obj(bpy.context.active_object)

        if os.path.isfile(config_filename):
            with open(config_filename, "r", newline="") as csvfile:
                csv_reader = csv.reader(csvfile)

                rows = list(csv_reader)
                found_row = False
                for row in rows:
                    if row[0] == screen_name:
                        row[1] = resolution_x
                        row[2] = resolution_y
                        row[3] = obj_path
                        found_row = True
                        break
                if not found_row:
                    rows.append([screen_name, resolution_x, resolution_y, obj_path])

                with open(config_filename, "w", newline="") as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows(rows)

        else:
            obj_path = save_active_mesh_as_obj(bpy.context.active_object)
            with open(config_filename, "w", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(
                    ["screen_name", "resolution_x", "resolution_y", "OBJ_path"]
                )
                csv_writer.writerow([screen_name, resolution_x, resolution_y, obj_path])

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)


PROPS = [
    (
        "config_filename",
        bpy.props.StringProperty(name="Config Filename", default="screens_config.csv"),
    ),
    ("screen_name", bpy.props.StringProperty(name="Screen Name", default="Screen_1")),
    ("resolution_x", bpy.props.IntProperty(name="Resolution Width:", default=1920)),
    ("resolution_y", bpy.props.IntProperty(name="Resolution Height:", default=1080)),
]


class MESH_UL_VP_volume_screen_list(bpy.types.UIList):
    def draw_item(
        self, context, layout, data, item, icon, active_data, active_propname
    ):
        ob = data
        slot = item
        if self.layout_type in {"DEFAULT", "COMPACT"}:
            layout.prop(slot, "name", text="", emboss=False, icon_value=icon)
        elif self.layout_type in {"GRID"}:
            layout.alignment = "CENTER"
            layout.label(text="", icon_value=icon)


class VPScreenConfigSideCarPanel(Panel):
    bl_idname = "VIEW3D_PT_VPScreenConfigSidecar"
    bl_label = "VP Screen Config Sidecar"
    bl_category = "Virtual Production"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        col = self.layout.column()
        for prop_name, _ in PROPS:
            row = col.row()
            row.prop(context.scene, prop_name)
        col.operator("opr.vp_screen_config_sidecar", text="Commit Screen Config")

        col.separator_spacer()

        list_col = col.column()
        list_row = list_col.row()

        list_row.template_list(
            "MESH_UL_VP_volume_screen_list",
            "volumn_screen_list",
            context.scene,
            "volumn_screen_list",
            context.scene,
            "volumn_screen_list_index",
            rows=5,
        )
        list_button_col = col.column(align=True)


CLASSES = [
    VPScreenConfigSideCar,
    VPScreenConfigSideCarPanel,
    MESH_UL_VP_volume_screen_list,
]


def register():
    for prop_name, prop_value in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)

    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for prop_name, _ in PROPS:
        delattr(bpy.types.Scene, prop_name)

    for cls in CLASSES:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
