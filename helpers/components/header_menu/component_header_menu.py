import allure

from selene import browser, be, have
from selene.core.condition import Condition


class ComponentHeaderMenu:
    """
    Класс компонента хедер меню. Описывает методы для работы с хедер меню.
    Возвращает объект класса ComponentHeaderMenu - паттерн Fluent Page Object.
    """

    @allure.step("Навести курсор на кнопку 'О компании'")
    def hover_to_about_company(self) -> 'ComponentHeaderMenu':
        """
        Метод наведения курсора на кнопку "О компании" в хедер меню.
        Condition используется для явного ожидания видимости элемента и проверки текста на кнопке.
        """
        with allure.step('Навести курсов на кнопку "О компании" и проверить текст на кнопке'):
            browser.element('//button[text()="О компании"]').should(Condition.by_and(
                be.visible, have.text("О компании"))).hover()
        return self

    @allure.step('Нажать на кнопку "О компании" из списка подменю')
    def click_header_about_company_button(self) -> 'ComponentHeaderMenu':
        """
        Метод нажатия кнопки "О компании" из хедер меню после наведения на одноименную кнопку.
        После клика проверяем что страница открылась, а именно, проверяем что появился элемент с описанием.
        """
        with allure.step('После наведения курсора на кнопку "О компании" нажать на кнопку "О компании" из списка'):
            browser.element('//a[@href="/we"]').should(Condition.by_and(
                be.clickable, have.text("О компании"))).hover().click()
            browser.element('//div[@class="excerpt"]').should(Condition.by_and(
                be.visible, have.text("BIOCAD — ведущая биотехнологическая компания России")))
        return self

    @allure.step('Навести курсор на кнопку "Наука" из списка подменю')
    def click_header_science_button(self) -> 'ComponentHeaderMenu':
        """
        Метод наведения курсора на кнопку "Наука" в подменю (после наведения на кнопку "О компании").
        После наводим курсор на кнопку "Наука" в другом подменю и нажимаем.
        После проверяем что страница открылась, а именно, проверяем что появился элемент с текстом.
        """
        browser.element('//li[@class="sub"]/button[contains(text(),"Наука")]').should(Condition.by_and(
            be.visible, have.text('Наука'))).hover()
        browser.element('//a[@href="/science"]').should(Condition.by_and(
            be.clickable, have.text('Наука'))).hover().click()
        browser.element('//p[contains(text(),"Полный цикл разработки")]').should(Condition.by_and(
            be.present, be.visible))
        return self

    @allure.step("Наведение курсора на кнопку 'Продукты'")
    def hover_to_products(self) -> 'ComponentHeaderMenu':
        """
        Метод наведения курсора на кнопку "Продукты" в хедер меню.
        Condition используется для явного ожидания видимости элемента и проверки текста на кнопке.
        """
        with allure.step('Навести курсов на кнопку "Продукты" и проверить текст на кнопке'):
            browser.element('//button[text()="Продукты"]').should(Condition.by_and(
                be.visible, have.text("Продукты"))).hover()
        return self
