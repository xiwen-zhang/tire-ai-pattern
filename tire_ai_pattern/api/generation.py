"""Generation pipeline entrypoint placeholders."""

from __future__ import annotations

from collections.abc import Sequence

from tire_ai_pattern.models.rule_models import BaseRuleConfig


def run_generation_pipeline(
    input_data,
    rules_config: Sequence[BaseRuleConfig] | None = None,
):
    """Run the generation pipeline through node-level orchestration."""

    raise NotImplementedError("Generation pipeline placeholder is not implemented yet.")
