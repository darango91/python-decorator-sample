from abc import ABCMeta, abstractmethod


class Human:
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


class HumanClothesDecorator(Human):
    """
    Human clothes' decorator base class
    """
    _human_wrapper: Human = None
    name: str = ""

    def __init__(self, human: Human) -> None:
        self._human_wrapper = human
        self.name = self._human_wrapper.name

    @property
    def wrapper(self) -> Human:
        """
        The Decorator delegates all work to the wrapped component.
        """
        return self._human_wrapper

    def get_clothes(self) -> str:
        return f"Nice dressing clothes & {self.wrapper.get_clothes()}"


class HumanShoesDecorator(HumanClothesDecorator):
    """
    Human shoes decorator
    """
    def get_clothes(self) -> str:
        return f"Fancy shoes & {self.wrapper.get_clothes()}"


class HumanSocksDecorator(HumanClothesDecorator):
    """
    Human socks decorator
    """
    def get_clothes(self) -> str:
        return f"Fancy socks & {self.wrapper.get_clothes()}"
