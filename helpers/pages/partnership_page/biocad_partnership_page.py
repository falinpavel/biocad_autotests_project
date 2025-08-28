import allure
from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class BiocadPartnershipPage:
    """
    Класс страницы "Партнерство" сайта biocad.ru.
    Описывает методы для работы со страницей "Партнерство".
    """
    def __init__(self):
        self.url = Links.PARTNERSHIP_URL

    @allure.step("Открытие страницы 'Партнерство'")
    def open(self) -> 'BiocadPartnershipPage':
        """
        Метод открытия страницы "Партнерство".
        """
        browser.open(self.url)
        return self

    @allure.step("Проверка что страница 'Партнерство' открыта")
    def is_opened(self) -> 'BiocadPartnershipPage':
        """
        Метод для проверки открытия страницы "Партнерство" открыта.
        Проверяем появление элемента с описанием.
        """
        with allure.step('Проверить отображение описания на странице'):
            browser.element('//h1[@class="badge"]').should(
                Condition.by_and(be.present, be.visible, have.text('Научное сотрудничество с BIOCAD')))
        return self
