from SRBA.state_adjust.buff.absBuff.TimeRestrictStatesBuff import TimeRestrictStatesBuff


class BronyaSkillBuff(TimeRestrictStatesBuff):
    def __init__(self, sourceEntity, targetEntity):
        # TODO 判断布洛妮娅星魂
        super().__init__(sourceEntity, targetEntity, 1)

    def applyStatesBuff(self):
        # TODO 读取布洛妮娅战技增伤倍率
        damage_increase_value = 0.3
        # TODO 对目标实体施加buff
        pass
