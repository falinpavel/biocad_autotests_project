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
        """
        with allure.step('После наведения курсора на кнопку "О компании" нажать на кнопку "О компании" из списка'):
            browser.element('//a[@href="/we"]').should(Condition.by_and(
                be.clickable, have.text("О компании"))).hover().click()
        return self

    @allure.step('Навести курсор на кнопку "Наука" из списка подменю')
    def click_header_science_button(self) -> 'ComponentHeaderMenu':
        """
        Метод наведения курсора на кнопку "Наука" в подменю (после наведения на кнопку "О компании").
        После наводим курсор на кнопку "Наука" в другом подменю и нажимаем.
        """
        browser.element('//li[@class="sub"]/button[contains(text(),"Наука")]').should(Condition.by_and(
            be.visible, have.text('Наука'))).hover()
        browser.element('//a[@href="/science"]').should(Condition.by_and(
            be.clickable, have.text('Наука'))).hover().click()
        return self

    @allure.step('Навести курсор на кнопку "Научные публикации" из списка подменю')
    def click_header_science_publications_button(self) -> 'ComponentHeaderMenu':
        """
        Метод наведения курсора на кнопку "Наука" в подменю (после наведения на кнопку "О компании").
        После наводим курсор на кнопку "Научные публикации" в другом подменю и нажимаем.
        """
        browser.element('//li[@class="sub"]/button[contains(text(),"Наука")]').should(Condition.by_and(
            be.visible, have.text('Наука'))).hover()
        browser.element('//a[@href="/publications"]').should(Condition.by_and(
            be.clickable, have.text('Научные публикации'))).hover().click()
        return self

    @allure.step('Навести курсор на кнопку "Партнерство" из списка подменю')
    def click_header_partnership_button(self) -> 'ComponentHeaderMenu':
        """
        Метод наведения курсора на кнопку "Наука" в подменю (после наведения на кнопку "О компании").
        После наводим курсор на кнопку "Партнерство" в другом подменю и нажимаем.
        """
        browser.element('//li[@class="sub"]/button[contains(text(),"Наука")]').should(Condition.by_and(
            be.visible, have.text('Наука'))).hover()
        browser.element('//a[@href="/partnership"]').should(Condition.by_and(
            be.clickable, have.text('Партнерство'))).hover().click()
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

    @allure.step('Нажать на кнопку "Заказать препарат" из списка подменю')
    def click_header_order_the_drug_button(self) -> 'ComponentHeaderMenu':
        """
        Метод нажатия кнопки "Заказать препарат" из хедер меню для перехода на страницу.
        """
        with allure.step('Нажать на кнопку "Заказать препарат" из хедер меню для перехода на страницу'):
            browser.element('//a[@href="/knv"]').should(Condition.by_and(
                be.clickable, have.text("Заказать препарат"))).hover().click()
        return self
