from tire_ai_pattern.models.rule_models import Rule9Config
from tire_ai_pattern.rules.base import RuleExecutor
from tire_ai_pattern.rules.registry import register_rule_executor


@register_rule_executor
class Rule9Executor(RuleExecutor):
    rule_cls = Rule9Config
