from entitylib.bases import EntityEmptyBase
from entitylib.mixins.basic import HealthMixin, ManaMixin

class Entity(EntityEmptyBase):
    def __init__(self, name, health, max_health, mana, max_mana):
        EntityEmptyBase.__init__(self, name)
        HealthMixin.__init__(self, health, max_health)
        ManaMixin.__init__(self, mana, max_mana)

if __name__ == '__main__':
    entity = Entity('Human', 10, 20, 5, 10)
