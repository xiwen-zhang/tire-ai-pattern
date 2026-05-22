"""
参考配置 2：5个RIB，所有对称性 (symmetry_0/1/2) + 所有连续性 (continuity_0/1/2)
RIB数量: 5
对称性候选: [symmetry_0, symmetry_1, symmetry_2]
连续性候选: [continuity_0, continuity_1, continuity_2]
"""

from pathlib import Path
from src.models.enums import RegionEnum, StitchingSchemeName, DecorationPositionEnum
from src.utils.image_utils import load_image_to_base64

CONFIG = {
    "scheme_rank": 1,
    "is_debug": False,
    "big_image": None,
    "small_images": [
        {"image_base64": load_image_to_base64(Path("tests/datasets/stitching/rib1.png"), with_prefix=True), "region": RegionEnum.SIDE},
        {"image_base64": load_image_to_base64(Path("tests/datasets/stitching/rib2.png"), with_prefix=True), "region": RegionEnum.CENTER},
        {"image_base64": load_image_to_base64(Path("tests/datasets/stitching/rib3.png"), with_prefix=True), "region": RegionEnum.CENTER},
        {"image_base64": load_image_to_base64(Path("tests/datasets/stitching/rib4.png"), with_prefix=True), "region": RegionEnum.CENTER},
        {"image_base64": load_image_to_base64(Path("tests/datasets/stitching/rib5.png"), with_prefix=True), "region": RegionEnum.SIDE},
    ],
    "rules_config": [
        {"rule": "rule1", "description": "rib无对称", "max_score": 10},
        {"rule": "rule2", "description": "rib中心对称", "max_score": 10},
        {"rule": "rule3", "description": "rib左右对称", "max_score": 10},
        {"rule": "rule6", "description": "节距纵向关系无缝拼接", "max_score": 10},
        {
            "rule": "rule8",
            "description": "横沟数量约束",
            "max_score": 4,
            "groove_width_center": 25.0,
            "groove_width_side": 13.0,
        },
        {
            "rule": "rule11",
            "description": "纵向钢片与细沟数量约束",
            "max_score": 4,
            "groove_width": 1,
            "min_width_offset_px": 1,
            "edge_margin_ratio": 0.1,
            "min_segment_length_ratio": 0.5,
            "max_angle_from_vertical": 10,
            "max_count_center": 3,
            "max_count_side": 2,
        },
        {
            "rule": "rule12",
            "description": "两个RIB间横向钢片及横沟连续性占比是否满足要求",
            "max_score": 6,
            "continuity_ratio_upper": 0.7,
            "continuity_ratio_lower": 0.6,
            "continuity_mode_list": [
                StitchingSchemeName.CONTINUITY_0,
                StitchingSchemeName.CONTINUITY_1,
                StitchingSchemeName.CONTINUITY_2,
            ],
        },
        {
            "rule": "rule16",
            "description": "中心RIB上的横沟或横向钢片可任意组合连续性",
            "max_score": 4,
            "continuity_mode_list": [
                StitchingSchemeName.CONTINUITY_0,
                StitchingSchemeName.CONTINUITY_1,
                StitchingSchemeName.CONTINUITY_2,
            ],
        },
        {
            "rule": "rule13",
            "description": "海陆比28%-35%",
            "max_score": 2,
            "land_ratio_min": 0.28,
            "land_ratio_max": 0.35,
        },
        {
            "rule": "rule20",
            "description": "文生图",
            "prompt": "tire tread pattern design",
            "num_images": 1,
            "output_width": 512,
            "output_height": 512,
        },
        {
            "rule": "rule22",
            "description": "图像分辨率",
            "target_width": 512,
            "target_height": 512,
            "keep_aspect_ratio": True,
            "output_format": "png",
        },
        {
            "rule": "rule100", "rib_number": 5,
            "rib_sizes": [
                {"rib_name": "rib1", "num_pitchs": 5, "rib_width": 400, "rib_height": 640},
                {"rib_name": "rib2", "num_pitchs": 5, "rib_width": 200, "rib_height": 640},
                {"rib_name": "rib3", "num_pitchs": 5, "rib_width": 200, "rib_height": 640},
                {"rib_name": "rib4", "num_pitchs": 5, "rib_width": 200, "rib_height": 640},
                {"rib_name": "rib5", "num_pitchs": 5, "rib_width": 400, "rib_height": 640},
            ],
        },
        {
            "rule": "rule101",
            "groove_sizes": [
                {"groove_width": 20, "groove_height": 640},
                {"groove_width": 20, "groove_height": 640},
                {"groove_width": 20, "groove_height": 640},
                {"groove_width": 20, "groove_height": 640},
            ],
        },
        {
            "rule": "rule102",
            "decorations": [
                {"position": DecorationPositionEnum.LEFT, "decoration_width": 300, "decoration_height": 640, "decoration_opacity": 128},
            ],
        },
    ],
}

from src.config._builder import build_tire_struct

tire_struct = build_tire_struct(CONFIG)
