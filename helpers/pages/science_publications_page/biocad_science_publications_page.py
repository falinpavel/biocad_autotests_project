import allure
from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class BiocadSciencePublicationsPage:
    """
    Класс страницы "Научные публикации" сайта biocad.ru.
    Описывает методы для работы со страницей "Научные публикации".
    """
    def __init__(self):
        self.url = Links.SCIENCE_PUBLICATIONS_URL

    @allure.step("Открытие страницы 'Научные публикации'")
    def open(self) -> 'BiocadSciencePublicationsPage':
        """
        Метод открытия страницы "Научные публикации".
        """
        browser.open(self.url)
        return self

    @allure.step("Проверка что страница 'Научные публикации' открыта")
    def is_opened(self) -> 'BiocadSciencePublicationsPage':
        """
        Метод для проверки открытия страницы "Научные публикации" открыта.
        Проверяем появление элемента с описанием.
        """
        with allure.step('Проверить отображение описания на странице'):
            browser.element('//p[contains(text(),"В этом разделе представлены научные публикации")]').should(
                Condition.by_and(be.present, be.visible))
        return self
