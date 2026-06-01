from tire_ai_pattern.models.rule_models import Rule14Config
from tire_ai_pattern.rules.base import RuleExecutor
from tire_ai_pattern.rules.registry import register_rule_executor


@register_rule_executor
class Rule14Executor(RuleExecutor):
    rule_cls = Rule14Config
