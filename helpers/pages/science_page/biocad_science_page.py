import allure
from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class BiocadSciencePage:
    """
    Класс страницы "Наука" сайта biocad.ru.
    Описывает методы для работы со страницей "Наука".
    """
    def __init__(self):
        self.url = Links.SCIENCE_URL

    @allure.step("Открытие страницы 'Наука'")
    def open(self) -> 'BiocadSciencePage':
        """
        Метод открытия страницы "Наука".
        """
        browser.open(self.url)
        return self

    @allure.step("Проверка что страница 'Наука' открыта")
    def is_opened(self) -> 'BiocadSciencePage':
        """
        Метод для проверки открытия страницы "Наука" открыта.
        Проверяем появление элемента с описанием.
        """
        with allure.step('Проверить отображение описания на странице'):
            browser.element('//p[contains(text(),"Полный цикл разработки")]').should(Condition.by_and(
                be.present, be.visible))
        return self
