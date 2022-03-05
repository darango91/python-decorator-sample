from components.human import Human


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
