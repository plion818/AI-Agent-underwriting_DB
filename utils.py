import config_rules

def get_nested_value(data_dict, key_path, default="N/A"):
    """Safely get a value from a nested dictionary."""
    keys = key_path.split('.')
    val = data_dict
    for key in keys:
        if isinstance(val, dict) and key in val:
            val = val[key]
        else:
            return default
    return val if val is not None else default

def get_class_desc_map():
    """建立 類別 -> 描述 對照表"""
    class_desc_map = {}
    if hasattr(config_rules, 'config_rules') and isinstance(config_rules.config_rules, dict):
        for rule_group in config_rules.config_rules.values():
            if isinstance(rule_group, list):
                for rule in rule_group:
                    if isinstance(rule, dict) and rule.get("class"):
                        class_desc_map[rule.get("class")] = rule.get("description", "無類別描述")
    return class_desc_map

def get_rule_class_map():
    """建立 項目 -> 類別 對照表"""
    rule_class_map = {}
    if hasattr(config_rules, 'config_rules') and isinstance(config_rules.config_rules, dict):
        for rule_group in config_rules.config_rules.values():
            if isinstance(rule_group, list):
                for rule in rule_group:
                    if isinstance(rule, dict) and "keywords" in rule and isinstance(rule["keywords"], list):
                        for kw in rule["keywords"]:
                            rule_class_map[kw] = rule.get("class", "未分類規則")
    return rule_class_map

def get_rule_required_map():
    """建立 項目 -> 必要性 對照表 (返回 '✶ 必要' 或 '○ 選擇')"""
    rule_required_map = {}
    if hasattr(config_rules, 'config_rules') and isinstance(config_rules.config_rules, dict):
        for rule_group in config_rules.config_rules.values():
            if isinstance(rule_group, list):
                for rule in rule_group:
                    if isinstance(rule, dict) and "keywords" in rule and isinstance(rule["keywords"], list):
                        for kw in rule["keywords"]:
                            rule_required_map[kw] = "✶ 必要" if rule.get("required", False) else "○ 選擇"
    return rule_required_map
