"""Pipeline-1 orchestration.

Pipeline-1 evaluates input small images, generates and stitches the big image,
then evaluates and scores the resulting big image in the shared ``TireStruct``.
"""

from __future__ import annotations

from tire_ai_pattern.common.exceptions import InputTypeError
from tire_ai_pattern.models.tire_struct import TireStruct
from tire_ai_pattern.nodes.small_image_evaluator import evaluate_small_images
from tire_ai_pattern.nodes.stitch_scheme_generator import generate_stitch_scheme
from tire_ai_pattern.nodes.big_image_stitcher import stitch_big_image
from tire_ai_pattern.nodes.big_image_evaluator import evaluate_big_image
from tire_ai_pattern.nodes.geometry_scorer import calculate_geometric_scores
from tire_ai_pattern.rules.executors import load_all_executors
from tire_ai_pattern.utils.logger import get_logger


PIPELINE_NAME = "pipeline1"
logger = get_logger("pipeline1")


def run_pipeline1(tire_struct: TireStruct) -> TireStruct:
    """Run Pipeline-1 through the currently implemented Node1 step.

    Args:
        tire_struct: Pipeline-1 input object. It must already be validated as
            ``TireStruct`` and contain the small images / rule configs needed by
            Node1.

    Returns:
        The same ``TireStruct`` instance with ``small_images[*].evaluation``
        filled by Node1. ``flag`` and ``err_msg`` are updated to reflect the
        pipeline step result.

    Raises:
        InputTypeError: If ``tire_struct`` is not a ``TireStruct`` instance.
    """

    # TODO: executor registration is loaded here for the current test path.
    # This boundary can be revisited when registry initialization is redesigned.
    load_all_executors()

    if not isinstance(tire_struct, TireStruct):
        raise InputTypeError(
            function="run_pipeline1",
            param="tire_struct",
            expected_type="TireStruct",
            actual_type=type(tire_struct).__name__,
        )

    STEP = "unknown"
    try:

        STEP = '小图评估'

        evaluate_small_images(
            tire_struct.small_images,
            tire_struct.rules_config,
            is_debug=tire_struct.is_debug,
        )

        STEP = '方案拼接'

        generate_stitch_scheme(
            tire_struct.big_image,
            tire_struct.small_images,
            tire_struct.rules_config,
            tire_struct.scheme_rank
        )

        STEP = '拼接大图'

        stitch_big_image(
            tire_struct.big_image
        )

        STEP = '大图评估'

        evaluate_big_image(
            tire_struct.big_image,
            tire_struct.rules_config,
            is_debug=tire_struct.is_debug,
        )

        STEP = '大图打分'

        calculate_geometric_scores(
            tire_struct.big_image,
            tire_struct.small_images,
            tire_struct.rules_config,
        )

    except Exception as exc:
        logger.exception("%s failed at step: %s", PIPELINE_NAME, STEP)
        tire_struct.flag = False
        tire_struct.err_msg = f"{PIPELINE_NAME}.{STEP} failed: {exc}"
        return tire_struct

    tire_struct.flag = True
    tire_struct.err_msg = None
    return tire_struct
