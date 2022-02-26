from components.human import \
    Human, YoungHuman, \
    HumanClothesDecorator, \
    HumanShoesDecorator, \
    HumanSocksDecorator

from decorators.function_decorator import \
    p_decorate


@p_decorate
def get_text(name):
    return f"Hello, im here and my name is {name}"


def get_human_clothing(human: Human):
    clothes_information = human.get_clothes()
    print(clothes_information)


if __name__ == '__main__':
    young_human = YoungHuman()
    young_human.name = "John Doe"
    get_human_clothing(young_human)

    human_with_clothes = HumanClothesDecorator(young_human)
    get_human_clothing(human_with_clothes)

    human_with_clothes_and_shoes = HumanShoesDecorator(human_with_clothes)
    get_human_clothing(human_with_clothes_and_shoes)

    fully_dressed_human = HumanSocksDecorator(human_with_clothes_and_shoes)
    get_human_clothing(fully_dressed_human)

    # Decoradores de funciones
    # print(get_text("Diego Arango"))
