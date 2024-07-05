from ZoteRules import zote_rules
from random import randint

bad_id_responce = 'Всего есть 57 заповедей, выберите из них.'

def get_rule_by_id(id: int) -> str:
    if id < 1 or len(zote_rules) <= id:
        return bad_id_responce
    return zote_rules[id - 1]

def get_random_rule() -> str:
    return get_rule_by_id(randint(1, len(zote_rules)))

