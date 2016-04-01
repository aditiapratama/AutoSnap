import bpy

generated_text_ops = '''
# This file is auto-generated by addon AutoSnap
# http://julienduroure.com/AutoSnap
# for any questions, please ask contact@julienduroure.com
import bpy
import mathutils
import math

autosnap_rig_id = "###rig_id###"

### Warning : any modification on this enum must be reported on live source code
IK_type_items = [
	("POLE", "With Pole", "", 1),
	("ROTATION", "With Rotation", "", 2),
]

### Warning : any modification on this enum must be reported on live source code
scale_type_items = [
	("NONE", "None", "", 1),
	("PARENT", "Parenting", "", 2),
]

### Warning : any modification on this enum must be reported on live source code
location_type_items = [
	("NONE", "None", "", 1),
	("PARENT", "Parenting", "", 2),
]

### Warning : any modification on this enum must be reported on live source code
switch_way = [
	("IK2FK", "ik2fk", "", 1),
	("FK2IK", "fk2ik", "", 2),
]

### Warning : any modification on this enum must be reported on live source code
autodisplay_items = [
	("LAYER", "Layer", "", 1),
	("HIDE", "Hide", "", 2),
]

### Warning : any modification on this enum must be reported on live source code
autokeyframe_items = [
	("AVAILABLE", "Available", "", 1),
	("KEYING_SET", "Keying Set", "", 2),
]

### Warning : any modification on this enum must be reported on live source code
switch_invert_items = [
	("IKIS0", "IK is 0", "", 1),
	("FKIS0", "FK is 0", "", 2),
]

### Warning : any modification on this PorpertyGroup must be reported on live source code
class BoneItem(bpy.types.PropertyGroup):
	name = bpy.props.StringProperty(name="Bone name")
	
### Warning : any modification on this PorpertyGroup must be reported on live source code
class BonePairItem(bpy.types.PropertyGroup):
	name_FK = bpy.props.StringProperty(name="Bone name FK")
	name_IK = bpy.props.StringProperty(name="Bone name IK")

def get_poll_snapping_op(context):
	return context.active_object and context.active_object.type == "ARMATURE" and context.active_object.data.get("autosnap_rig_id") is not None and context.active_object.data.get("autosnap_rig_id") == autosnap_rig_id and context.mode == 'POSE'

###CLASS_switch_FKIK###


def register():
	bpy.utils.register_class(BoneItem)
	bpy.utils.register_class(BonePairItem)
	bpy.utils.register_class(###CLASS_switch_FKIK_name###)
	
def unregister():
	bpy.utils.unregister_class(BoneItem)
	bpy.utils.unregister_class(BonePairItem)
	bpy.utils.unregister_class(###CLASS_switch_FKIK_name###)

register()
'''		

ui_generated_switch_param = '''
###tab###op.root = "###root###"
###tab###op.ik_type = "###ik_type###"
###tab###op.global_scale = ###global_scale###
###tab###op.ik_scale_type = '###ik_scale_type###'
###tab###op.fk_scale_type = '###fk_scale_type###'
###tab###op.ik_location_type = '###ik_location_type###'
###tab###op.fk_location_type = '###fk_location_type###'
###tab###op.with_limb_end_fk	= ###with_limb_end_fk###
###tab###op.with_limb_end_ik	= ###with_limb_end_ik###

###tab###op.ik1 = "###ik1###"
###tab###op.ik2 = "###ik2###"
###tab###op.ik3 = "###ik3###"
###tab###op.ik4 = "###ik4###"
###tab###op.ik5 = "###ik5###"
		
###tab###op.fk1 = "###fk1###"
###tab###op.fk2 = "###fk2###"
###tab###op.fk3 = "###fk3###"
###tab###op.fk4 = "###fk4###"
		
###tab###op.ik_scale = "###ik_scale###"
###tab###op.fk_scale = "###fk_scale###"
###tab###op.ik_location = "###ik_location###"
###tab###op.fk_location = "###fk_location###"

###tab###op.with_reinit_bones = ###WITH_REINIT_BONES###
###tab###op.with_add_bones = ###WITH_ADD_BONES###

###tab###populate_reinit_bones(op, ###limb_reinit_bones###)
###tab###populate_add_bones(op, ###limb_add_bones###)
'''

ui_layout_basic_limb_name ='''
###tab###row_ = box.row()
###tab###row_.label("###limb###")
'''

ui_layout_on_select ='''
###tab_minus###if bpy.context.active_pose_bone.name in ###ON_SELECT_TAB###:
'''

ui_layout_basic ='''
###ON_SELECT###
###tab###row = layout.row()
###tab###box = row.box()
###LIMB_NAME###
###tab###row_ = box.row()
###tab###op = row_.operator("pose.limb_switch_ikfk_###rig_id###", text="###FK2IK_LABEL###")
###tab###op.layout_basic = True
###tab###op.switch_way = "FK2IK"
###GENERATED_bone_PARAM###
###tab###row_ = box.row()
###tab###op = row_.operator("pose.limb_switch_ikfk_###rig_id###", text="###IK2FK_LABEL###")
###tab###op.layout_basic = True
###tab###op.switch_way = "IK2FK"
###GENERATED_bone_PARAM###
'''
ui_autoswitch_param='''
###tab###op.autoswitch = bpy.context.active_object.pose.bones["###AUTOSWITCH_BONE_STORE###"].autosnap_autoswitch
###tab###op.autoswitch_data_bone = "###AUTOSWITCH_BONE###"
###tab###op.autoswitch_data_property = "###AUTOSWITCH_PROPERTY###"
###tab###op.autoswitch_keyframe = bpy.context.active_object.pose.bones["###AUTOSWITCH_BONE_STORE###"].autosnap_autoswitch_keyframe
'''

ui_autodisplay_param_layer ='''
###tab###op.autodisplay_data_layer_ik = ###AUTODISPLAY_LAYER_IK###
###tab###op.autodisplay_data_layer_fk = ###AUTODISPLAY_LAYER_FK###
'''

ui_autodisplay_param='''
###tab###op.autodisplay = bpy.context.active_object.pose.bones["###AUTODISPLAY_BONE_STORE###"].autosnap_autodisplay
###tab###op.autodisplay_data_type = "###AUTODISPLAY_TYPE###"
###AUTODISPLAY_PARAM_TYPE###
'''
ui_autokeyframe_param_keyingset ='''
###tab###op.autokeyframe_data_keying_set_FK = "###AUTOKEYFRAME_KEYING_SET_FK###"
###tab###op.autokeyframe_data_keying_set_IK = "###AUTOKEYFRAME_KEYING_SET_IK###"
'''

ui_autokeyframe_param='''
###tab###op.autokeyframe = bpy.context.active_object.pose.bones["###AUTOKEYFRAME_BONE_STORE###"].autosnap_autokeyframe
###tab###op.autokeyframe_data_type = "###AUTOKEYFRAME_TYPE###"
###AUTOKEYFRAME_PARAM###
'''

ui_autoswitch_param_ko='''
###tab###op.autoswitch = False
###tab###op.autoswitch_keyframe = False
'''

ui_autodisplay_param_ko='''
###tab###op.autodisplay = False
'''

ui_autokeyframe_param_ko='''
###tab###op.autodkeyframe = False
'''

ui_layout_non_basic_autoswitch_keyframe = '''
###tab###	row_.prop(bpy.context.active_object.pose.bones["###SWITCH_BONE_STORE###"], "autosnap_autoswitch_keyframe", text="Keyframe")
'''

ui_layout_non_basic_autoswitch = '''
###tab###row_ = box.row()
###tab###row_.prop(bpy.context.active_object.pose.bones["###SWITCH_BONE_STORE###"], "autosnap_autoswitch", text="AutoSwitch")
###tab###if bpy.context.active_object.pose.bones["###SWITCH_BONE_STORE###"].autosnap_autoswitch == True:
###tab###	###GENERATED_interaction_AUTOSWITCH_KEYFRAME###
###tab###	pass
'''

ui_layout_non_basic_autodisplay = '''
###tab###row_ = box.row()
###tab###row_.prop(bpy.context.active_object.pose.bones["###AUTODISPLAY_BONE_STORE###"], "autosnap_autodisplay", text="AutoDisplay")
'''

ui_layout_non_basic_autokeyframe = '''
###tab###row_ = box.row()
###tab###row_.prop(bpy.context.active_object.pose.bones["###AUTOKEYFRAME_BONE_STORE###"], "autosnap_autokeyframe", text="AutoKeyframe")
'''

ui_layout_non_basic_limb_name ='''
###tab###row_ = box.row()
###tab###row_.label("###limb###")
'''

ui_layout_non_basic ='''
###ON_SELECT###
###tab###label = ""
###tab###try:
###tab###	if int(armature.pose.bones["###SWITCH_BONE###"].get("###SWITCH_PROPERTY###")) == 1.0 and "###SWITCH_INVERT###" == "IKIS0":
###tab###		label = "###IK2FK_LABEL###"
###tab###	elif int(armature.pose.bones["###SWITCH_BONE###"].get("###SWITCH_PROPERTY###")) == 1.0 and "###SWITCH_INVERT###" == "FKIS0":
###tab###		label = "###FK2IK_LABEL###"
###tab###	if int(armature.pose.bones["###SWITCH_BONE###"].get("###SWITCH_PROPERTY###")) == 0.0 and "###SWITCH_INVERT###" == "IKIS0":
###tab###		label = "###FK2IK_LABEL###"
###tab###	elif int(armature.pose.bones["###SWITCH_BONE###"].get("###SWITCH_PROPERTY###")) == 0.0 and "###SWITCH_INVERT###" == "FKIS0":
###tab###		label = "###IK2FK_LABEL###"
###tab###except:
###tab###	label = ""
###tab###row = layout.row()
###tab###box = row.box()
###LIMB_NAME###
###tab###row_ = box.row()
###tab###op = row_.operator("pose.limb_switch_ikfk_###rig_id###", text=label)
###tab###op.layout_basic = False
###tab###op.switch_bone = "###SWITCH_BONE###"
###tab###op.switch_property = "###SWITCH_PROPERTY###"
###tab###op.switch_invert   = "###SWITCH_INVERT###"
###GENERATED_autoswitch_PARAM###
###GENERATED_autodisplay_PARAM###
###GENERATED_autokeyframe_PARAM###
###GENERATED_bone_PARAM###
###GENERATED_autoswitch_UI###
###GENERATED_autodisplay_UI###
###GENERATED_autokeyframe_UI###
'''

ui_generated_text = '''
# This file is auto-generated by addon AutoSnap
# http://julienduroure.com/AutoSnap
# for any questions, please ask contact@julienduroure.com
import bpy

autosnap_rig_id = "###rig_id###"

def populate_reinit_bones(op, list_):
	for bone in list_:
		item_dst = op.reinit_bones.add()
		item_dst.name = bone
		
def populate_add_bones(op, list_):
	for bone in list_:
		item_dst = op.add_bones.add()
		item_dst.name_FK = bone[0]
		item_dst.name_IK = bone[1]

class POSE_PT_BeSpanned_Snap_###rig_id###(bpy.types.Panel):
	bl_label = "###LABEL###"
	bl_space_type = 'VIEW_3D'
	bl_region_type = '###REGION_TYPE###'
	bl_category = "###CATEGORY###"
	
	@classmethod
	def poll(self, context):
		return context.active_object and context.active_object.type == "ARMATURE" and context.active_object.data.get("autosnap_rig_id") is not None and context.active_object.data.get("autosnap_rig_id") == autosnap_rig_id and context.mode == 'POSE'
		
			
	def draw(self, context):
		layout = self.layout
		armature = context.object
		
###LAYOUT###

def register():
	bpy.utils.register_class(POSE_PT_BeSpanned_Snap_###rig_id###)
	
def unregister():
	bpy.utils.unregister_class(POSE_PT_BeSpanned_Snap_###rig_id###)

register()
'''
