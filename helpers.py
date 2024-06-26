import random
import allure
import requests
from faker import Faker

from urls import EndPoints


class NewUserCreds:

    @staticmethod
    @allure.step("Генерация фейковых кредов для регистрации пользователя")
    def generate_creds_set():
        fake = Faker("ru_RU")

        email = fake.email()
        password = fake.password()
        name = fake.user_name()

        creds = {"email": email,
                 "password": password,
                 "name": name,
                 }
        return creds


class User:
    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def create_user(user_data):
        return requests.post(EndPoints.create_user, data=user_data)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(user_token):
        headers = {"Authorization": user_token}
        response = requests.delete(EndPoints.login_user, headers=headers)
        return response


class Order:
    @staticmethod
    @allure.step("Создание нового заказа")
    def create_order(ingredients, token=""):
        headers = {"Authorization": token}
        data = {"ingredients": ingredients}
        respons = requests.post(EndPoints.create_order, data=data, headers=headers)

        return respons

    @allure.step("Создание набора хешей для нового бургера")
    def create_burger(self):
        ingredients = self.get_ingredients()[0]  # Получаем словарь с ингредиентами
        burger_ingredients = []
        for value in ingredients.values():
            ingredient_hash = random.choice(value)
            burger_ingredients.append(ingredient_hash)

        return burger_ingredients

    @staticmethod
    @allure.step("Получение списка ингредиентов и словаря ингредиентов с разбивкой по типу")
    def get_ingredients():
        ingredients_dict = {"bun": [],
                            "main": [],
                            "sauce": []
                            }
        ingredient_list = []
        response = requests.get(EndPoints.ingridients)
        for ingredient in response.json()["data"]:
            current_hashs = ingredients_dict.pop(ingredient["type"])
            current_hashs.append(ingredient["_id"])
            ingredients_dict[ingredient["type"]] = current_hashs
            ingredient_list.append(ingredient["_id"])

        return ingredients_dict, ingredient_list