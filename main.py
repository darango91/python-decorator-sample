from components.human import \
    Human, YoungHuman, \
    HumanClothesDecorator, \
    HumanShoesDecorator, \
    HumanSocksDecorator


def get_human_clothing(human: Human):
    return f"Hi, my name is {human.name} \n" \
           f"And this is my clothing: {human.get_clothes()} \n"


if __name__ == '__main__':
    young_human = YoungHuman()
    young_human.name = "John Doe"
    print(get_human_clothing(young_human))

    human_with_clothes = HumanClothesDecorator(young_human)
    print(get_human_clothing(human_with_clothes))

    human_with_clothes_and_shoes = HumanShoesDecorator(human_with_clothes)
    print(get_human_clothing(human_with_clothes_and_shoes))

    fully_dressed_human = HumanSocksDecorator(human_with_clothes_and_shoes)
    print(get_human_clothing(fully_dressed_human))
