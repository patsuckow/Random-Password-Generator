"""
Author Пацуков А.А. (https://vk.com/patsuckow) 🇷🇺
https://github.com/patsuckow/Random-Password-Generator
"""
import random
import argparse



def arg():
    """ Get the value of the argument --len passed to the script """
    parser = argparse.ArgumentParser(description='Генератор случайных строк')
    parser.add_argument(
        '--len',
        type=int,
        default=21,
        help='Длина генерируемой строки (default: 21)'
    )

    return parser.parse_args()


def random_password_generator(length=21) -> str:
    """ :return: random string """
    # random.choice() - extracts the required number of random characters from
    # the list.
    # Можно использовать и 
    return ''.join([
        random.choice(
            [str(i) for i in range(10)] +
            [chr(i) for i in range(65, 91)] +
            [chr(i) for i in range(97, 123)]
        ) for _ in range(length)
    ])


if __name__ == '__main__':
    if arg().len < 1:
        print("Длина строки должна быть больше 0")
    else:
        print(random_password_generator(arg().len))
