from abc import ABC, ABCMeta, abstractmethod


class Human(ABC):
    """
    Base abstract human class component
    """
    __metaclass__ = ABCMeta
    name: str

    @abstractmethod
    def get_clothes(self) -> str: raise NotImplementedError


class YoungHuman(Human):
    """
    Young human should be at least with underwear
    """
    def get_clothes(self) -> str:
        return "Underwear! :)"
