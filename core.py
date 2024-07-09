import bpy

from .register_class import _get_cls
from .starry_sky import make_object


class CSS_OT_starry_sky(bpy.types.Operator):
    bl_idname = "object.starry_sky"
    bl_label = "Starry Sky"
    bl_description = "Create starry sky."

    def execute(self, context):
        make_object()
        return {"FINISHED"}


# 自動的にこのモジュールのクラスを設定
ui_classes = _get_cls(__name__)


def draw_item(self, context):
    """メニューの登録と削除用"""
    for ui_class in ui_classes:
        self.layout.operator(ui_class.bl_idname)


def register():
    """追加登録用（クラス登録は、register_class内で実行）"""
    bpy.types.VIEW3D_MT_object.append(draw_item)


def unregister():
    """追加削除用（クラス削除は、register_class内で実行）"""
    bpy.types.VIEW3D_MT_object.remove(draw_item)
