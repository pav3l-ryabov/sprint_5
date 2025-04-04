import random

class GeneratorCredentials: # класс с генераторами учетных данных

    def generate_valid_email(): # генератор валидной почты формата "логин@домен"
        login_length = random.randint(5, 10)
        domain_length = random.randint(3, 6)

        letters = "abcdefghijklmnopqrstuvwxyz"
        digits = "0123456789"

        login = ''.join(random.choices(letters + digits, k=login_length))
        domain = ''.join(random.choices(letters, k=domain_length))

        return f"{login}@{domain}.ru"

    def generate_invalid_email(): # генератор невалидной почты формата "логиндомен"
        login_length = random.randint(5, 10)
        domain_length = random.randint(3, 6)

        letters = "abcdefghijklmnopqrstuvwxyz"
        digits = "0123456789"

        login = ''.join(random.choices(letters + digits, k=login_length))
        domain = ''.join(random.choices(letters, k=domain_length))

        return f"{login}{domain}.ru"


    def generate_valid_pass(): # генератор валидного пароля (от 6 до 14 символов)
        pass_length = random.randint(6, 14)

        letters = "abcdefghijklmnopqrstuvwxyz"
        digits = "0123456789"
        characters = "~@#$%^&*()_+"

        password = ''.join(random.choices(letters + digits + characters, k=pass_length))

        return f"{password}"

    def generate_invalid_short_pass(): # генератор невалидного короткого пароля (от 1 до 6 символов)
        pass_length = random.randint(1, 5)

        letters = "abcdefghijklmnopqrstuvwxyz"
        digits = "0123456789"
        characters = "~@#$%^&*()_+"

        password = ''.join(random.choices(letters + digits + characters, k=pass_length))

        return f"{password}"

    def generate_valid_name(): # генератор валидного имени (кириллица, латиница)
        name_length = random.randint(6, 14)

        letters = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

        name = ''.join(random.choices(letters, k=name_length))

        return f"{name}"

