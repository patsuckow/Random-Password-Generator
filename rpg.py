"""
Author Пацуков А.А. (https://vk.com/patsuckow) 🇷🇺
https://github.com/patsuckow/Random-Password-Generator
"""
import random
import argparse


def arg():
    """Get the value of the argument --len passed to the script"""
    parser = argparse.ArgumentParser(description="Генератор случайных строк")
    parser.add_argument(
        "--len", type=int, default=21, help="Длина генерируемой строки (default: 21)"
    )
    parser.add_argument(
        "--str", type=int, default=3, help="Кол-во генерируемых строк (default: 3)"
    )

    return parser.parse_args()


def random_password_generator(length=21) -> str:
    """:return: random string"""
    # random.choice() - extracts the required number of random characters from
    # the list. Можно использовать конечно и модуль string и выборку сделать 
    # однойстрокой типа:
    # random.choice(string.ascii_letters + string.digits) for _ in range(length)
    # но мне так больше нравится и можно ручками добавить выборку и других символов
    # если это понадобится
    return "".join(
        [
            random.choice(
                [str(i) for i in range(10)]
                + [chr(i) for i in range(65, 91)]
                + [chr(i) for i in range(97, 123)]
            )
            for _ in range(length)
        ]
    )


if __name__ == "__main__":
    if (arg().len < 1) or (arg().str < 1):
        print("Передаваемый параметр должен быть больше 0")
    else:
        for i in range(arg().str):
            print(random_password_generator(arg().len))
