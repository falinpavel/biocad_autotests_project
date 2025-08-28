import allure
from selene import browser, be, have, command
from selene.core.condition import Condition

from helpers.data.links import Links


class BiocadOrderTheDrugPage:
    """
    Класс страницы "Партнерство" сайта biocad.ru.
    Описывает методы для работы со страницей "Партнерство".
    """
    def __init__(self):
        self.url = Links.ORDER_THE_DRUG_URL

    @allure.step("Открытие страницы 'Заказать препарат'")
    def open(self) -> 'BiocadOrderTheDrugPage':
        """
        Метод открытия страницы "Заказать препарат".
        """
        browser.open(self.url)
        return self

    @allure.step("Проверка что страница 'Заказать препарат' открыта")
    def is_opened(self) -> 'BiocadOrderTheDrugPage':
        """
        Метод для проверки открытия страницы "Заказать препарат" открыта.
        Проверяем появление элемента с описанием.
        """
        with allure.step('Проверить отображение описания на странице'):
            browser.element('div[class="heading flex"] h2').should(
                Condition.by_and(be.present, be.visible, have.text('Как оформить заказ')))
        return self

    @allure.step('Нажать на кнопку "Заказать препараты"')
    def click_order_the_drug_button(self) -> 'BiocadOrderTheDrugPage':
        with allure.step('На странице "Заказать препараты" нажать на кнопку "Заказать препараты"'):
            browser.element('//div[@class="button" and contains(text(),"Заказать препараты")]').should(
                Condition.by_and(be.clickable)).double_click()
        return self

    @allure.step('Нажать на наименование препарата')
    def click_to_drug(self, drug_name: str) -> 'BiocadOrderTheDrugPage':
        with allure.step(f'Нажать на препарат под наименованием {drug_name}'):
            browser.element(f'//a[contains(text(),"{drug_name}")]').perform(command.js.scroll_into_view).should(
                Condition.by_and(be.clickable, have.text(drug_name))).click()
        return self

    @allure.step('Нажать кнопку назад на странице препарата')
    def click_back_to_list_drugs(self):
        with allure.step('Нажать на иконку со стрелкой назад для перехода к списку всех препаратов'):
            browser.element('.back').should(Condition.by_and(be.visible, be.clickable)).click()
        return self

    @allure.step('Нажать на кнопку "Заказать препарат"')
    def click_to_order_the_current_drug(self) -> 'BiocadOrderTheDrugPage':
        with allure.step('На странице конкретного препарата нажать на кнопку "Заказать препарат"'):
            browser.element('.order').should(Condition.by_and(be.clickable, have.text('Заказать препарат'))).click()
        return self
