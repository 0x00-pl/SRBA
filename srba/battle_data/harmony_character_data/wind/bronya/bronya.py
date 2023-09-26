from srba.character import Character
from srba.combatEntity import ToughnessReduce, InteractMethod, DamageType
from srba.damage_manager import attack
from srba.state_adjust.buff.bronya.bronya_attack_boost import BronyaAttackBoost


class Bronya(Character):

    def __init__(self, level, trace_set, relics, light_cone):
        super().__init__("布洛妮娅", level, trace_set, relics, light_cone)

    def normal_attack(self, targetSet):
        """
        布洛妮娅普通攻击
        :param target: combat_obj 对象
        """
        current_target = targetSet.target
        attack_value = self.Attack
        radio = 1

        # TODO  读取布洛妮娅普攻倍率
        base_damage = attack_value * radio
        # TODO 检查布洛妮娅行迹1
        hasTrace = True
        # 普攻必定暴击
        if hasTrace:
            self.CriticalChance = self.CriticalChance + 1.0
        attack(
            base_damage, DamageType.WIND, InteractMethod.NormalAttack, self, current_target, ToughnessReduce.Normal, [1]
        )
        if hasTrace:
            self.CriticalChance = self.CriticalChance - 1.0

        self.add_adjust(BronyaAttackBoost(self, self))

    def skill_attack(self, targetSet):
        """
        布洛妮娅战技
        :param target: combat_obj 对象
        """
        current_target = targetSet.target

        # TODO 施加增伤buff

        # 拉条100%
        if current_target is not self:
            current_target.Timer.change_distance(-100)

    def ult_attack(self, targetSet):
        targets = targetSet.targets
        # TODO 检查自身是否还有大招加成 在覆盖之前先取消大招加成

        for target in targets:
            # TODO 施加爆伤和攻击力提升.
            pass
