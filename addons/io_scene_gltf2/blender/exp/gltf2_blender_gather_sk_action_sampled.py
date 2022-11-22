# Copyright 2018-2022 The glTF-Blender-IO authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import bpy
import typing
from io_scene_gltf2.io.com import gltf2_io
from .gltf2_blender_gather_sk_channels import gather_sk_sampled_channels

#TODOANIM : if we don't bake SK, no need to have optional blender_action here. To check if we need to bake SK (drivers?)
def gather_action_sk_sampled(object_uuid: str, blender_action: typing.Optional[bpy.types.Action], export_settings):

    # If no animation in file, no need to bake
    if len(bpy.data.actions) == 0:
        return None

    animation = gltf2_io.Animation(
        channels=__gather_channels(object_uuid, blender_action.name if blender_action else object_uuid, export_settings),
        extensions=None,
        extras=None,
        name=__gather_name(object_uuid, blender_action, export_settings),
        samplers=[]
    )

    if not animation.channels:
        return None

    #TODOANIM add hook

    return animation

def __gather_name(object_uuid: str, blender_action: typing.Optional[bpy.types.Action], export_settings):
    return blender_action.name if blender_action else export_settings['vtree'].nodes[object_uuid].blender_object.name
    
def __gather_channels(object_uuid: str, blender_action_name: str, export_settings) -> typing.List[gltf2_io.AnimationChannel]:
    return gather_sk_sampled_channels(object_uuid, blender_action_name, export_settings)