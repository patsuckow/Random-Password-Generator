"""
    @uthor Пацуков А.А. (https://vk.com/patsuckow) 🇷🇺
    https://github.com/patsuckow/Random-Password-Generator
"""
import random
import argparse


def arg() -> int:
    """ Get the value of the argument --len passed to the script """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--len',
        type=int,
        default=21,
        help='provide an integer (default: 21)'
    )

    return parser.parse_args().len


def random_password_generator() -> str:
    """ :return: random string """
    # random.choice() - extracts the required number of random characters from
    # the list.
    return ''.join([
        random.choice(
            [str(i) for i in range(10)] +
            [chr(i) for i in range(65, 91)] +
            [chr(i) for i in range(97, 123)]
        ) for _ in range(arg())
    ])


if __name__ == '__main__':
    print(random_password_generator())
