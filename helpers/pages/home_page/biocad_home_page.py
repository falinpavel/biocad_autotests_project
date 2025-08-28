from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class BiocadHomePage:
    """
    Класс главной страницы сайта biocad.ru.
    Описывает методы для работы с главной страницей
    (за исключением хедер меню, методы работы с этим компонентом вынесены в отдельный Page Object.)
    """
    def __init__(self):
        self.url = Links.BASE_URL

    def open(self) -> 'BiocadHomePage':
        """
        Метод открытия главной страницы сайта biocad.ru.
        """
        browser.open(self.url)
        return self
