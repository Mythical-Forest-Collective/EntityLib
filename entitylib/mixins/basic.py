from ..bases import EntityEmptyBase
from ..exceptions import NoInteractEvent

class HealthMixin(object):
    """
    Health Mixin that adds an extremely basic health system to the Entity class

    Parameters
    ----------
    health:int
      The current health you want the entity to start with

    max_health:int
      The max health of the entity

    Attributes
    ----------
    health:int
      The current health you want the entity to start with

    max_health:int
      The max health of the entity
    """

    def __init__(self, health:int, max_health:int) -> None:
        self.max_health = max_health
        self.health = health

    def replenish_health(self, val:int) -> bool:
        self.health += val
        if self.health > self.max_health:
            return True
        return False

    def replenish_all_health(self) -> None:
        self.health = self.max_health

    def drain_health(self, val:int) -> None:
        self.health -= val
        if self.health < 0:
            self.health = 0


class ManaMixin(object):
    """
    Mana Mixin that adds an extremely basic mana system to the Entity class

    Parameters
    ----------
    mana:int
      The current mana you want the entity to start with

    max_mana:int
      The max mana of the entity

    Attributes
    ----------
    mana:int
      The current mana you want the entity to start with

    max_mana:int
      The max mana of the entity
    """

    def __init__(self, mana:int, max_mana:int) -> None:
        self.max_mana = max_mana
        self.mana = mana

    def replenish_mana(self, val:int) -> bool:
        self.mana += val
        if self.mana > self.max_mana:
            return True
        return False

    def replenish_all_mana(self) -> None:
        self.mana = self.max_mana

    def drain_mana(self, val:int) -> None:
        self.mana -= val
        if self.mana < 0:
            self.mana = 0

class InteractWithMixin(object):
    """
    Enables basic interaction
    """

    def __init__(self):
        pass


    def interact_with(self, entity:EntityEmptyBase):
        """
        Function that attempts to interact with an entity, target entity needs the OnInteractMixin

        Parameters
        ----------
        entity:EntityEmptyBase
          Requires any entity that is a subclass of EntityEmptyBase, with the OnInteractMixin

        Raises
        ------
        NoInteractEvent
          Raised when there is no `interact` method
        """
        try:
            entity.interact(self)
        except AttributeError:
            raise NoInteractEvent("`interact` method hasn't been implemented, either use the OnInteractMixin or implement an interact function yourself.")

class OnInteractMixin(object)
    """
    Mixin that is used to provide an interact function
    """

    def __init__(self):
        pass

    def interact(self, entity:EntityEmptyBase):
        """
        Function that allows interaction with any target entity with the InteractWithMixin

        Parameters
        ----------
        entity:EntityEmptyBase
          Requires any entity that is a subclass of EntityEmptyBase, with the InteractWithMixin
        """
        pass
