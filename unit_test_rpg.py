import unittest
from rpg import random_password_generator

class RandomPasswordGeneratorTest(unittest.TestCase):

    def test_generate_password_length(self):
        """
        Проверяет, что сгенерированный пароль имеет правильную длину.
        """
        # Генерируем пароль длиной 8 символов
        password = random_password_generator(8)
        self.assertEqual(len(password), 8)

        # Генерируем пароль длиной 12 символов
        password = random_password_generator(12)
        self.assertEqual(len(password), 12)

        # Другие проверки на длину пароля

    def test_generate_password_characters(self):
        """
        Проверяет, что сгенерированный пароль состоит только из указанных символов.
        """
        allowed_characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        password = random_password_generator(10)
        for char in password:
            self.assertIn(char, allowed_characters)


if __name__ == '__main__':
    unittest.main()
