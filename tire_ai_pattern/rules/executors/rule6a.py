from tire_ai_pattern.models.rule_models import Rule6AConfig
from tire_ai_pattern.rules.base import RuleExecutor
from tire_ai_pattern.rules.registry import register_rule_executor


@register_rule_executor
class Rule6AExecutor(RuleExecutor):
    rule_cls = Rule6AConfig
