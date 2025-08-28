import allure
from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class BiocadAboutCompanyPage:
    """
    Класс страницы "О компании" сайта biocad.ru.
    Описывает методы для работы со страницей "О компании".
    """
    def __init__(self):
        self.url = Links.ABOUT_COMPANY_URL

    @allure.step("Открытие страницы 'О компании'")
    def open(self) -> 'BiocadAboutCompanyPage':
        """
        Метод открытия страницы "О компании".
        """
        browser.open(self.url)
        return self

    @allure.step("Проверка что страница 'О компании' открыта")
    def is_opened(self) -> 'BiocadAboutCompanyPage':
        """
        Метод для проверки открытия страницы "О компании" открыта.
        Проверяем появление элемента с описанием.
        """
        with allure.step('Проверить отображение описания на странице'):
            browser.element('//div[@class="excerpt"]').should(Condition.by_and(
                be.visible, have.text("BIOCAD — ведущая биотехнологическая компания России")))
        return self
