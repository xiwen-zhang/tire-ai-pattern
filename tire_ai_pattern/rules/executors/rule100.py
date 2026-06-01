from __future__ import annotations

from tire_ai_pattern.models.image_models import BaseImage
from tire_ai_pattern.models.rule_models import (
    BaseRuleFeature, BaseRuleScore,
    Rule100Config, Rule100Feature, Rule100Score,
)
from tire_ai_pattern.rules.base import RuleExecutor
from tire_ai_pattern.rules.registry import register_rule_executor


@register_rule_executor
class Rule100Executor(RuleExecutor):
    rule_cls = Rule100Config

    def exec_feature(
        self,
        image: BaseImage,
        config: Rule100Config,
    ) -> BaseRuleFeature:
        return Rule100Feature()

    def exec_score(
        self,
        config: Rule100Config,
        feature: Rule100Feature,
    ) -> BaseRuleScore:
        return Rule100Score(score=None)
