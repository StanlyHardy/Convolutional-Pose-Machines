# Copyright 2018 Stanly Moses (stanlimoses@gmail.com)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===================================================================================
# -*- coding: utf-8 -*-


BODY_PARTS = {"top_head": 0, "neck": 1,
              "right_shoulder": 2, "right_elbow": 3,
              "right_wrist": 4, "left_shoulder": 5,
              "left_elbow": 6, "left_wrist": 7,
              "right_hip": 8, "right_knee": 9,
              "right_ankle": 10, "left_hip": 11,
              "left_knee": 12, "left_angle": 13}

# [0,1],
POSE_PAIRS = [["top_head", "neck"],  # 01
              ["neck", "right_shoulder"],  # 12
              ["right_shoulder", "right_elbow"],  # 23
              ["right_elbow", "right_wrist"],  # 34
              ["neck", "left_shoulder"],  # 15
              ["left_shoulder", "left_elbow"],  # 56
              ["left_elbow", "left_wrist"],  # 67
              ["neck", "left_hip"],  # 1,11
              ["left_hip", "left_knee"],  # 11,12
              ["left_knee", "left_angle"],  # 12,13
              ["neck", "right_hip"],  # 1,8
              ["right_hip", "right_knee"],
              ["right_knee", "right_ankle"]]  # 8,9

COLORS = ((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (192, 192, 192),
          (128, 128, 128), (128, 0, 0), (128, 128, 0), (0, 128, 0), (128, 0, 128), (0, 128, 128), (0, 0, 128))
