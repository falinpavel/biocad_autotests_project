import allure

from helpers.application_manager.application_manager import biocad


@allure.epic('Хедер меню')
@allure.feature('Навигация по веб-приложению через хедер меню')
class TestNavigateHeaderMenu:

    @allure.story('Переход на страницу "О компании"')
    @allure.title('Проверка перехода на страницу "О компании" через хедер меню')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_transition_to_about_company_page_from_header_menu(self):
        biocad.home_page.open()
        biocad.header_menu \
            .hover_to_about_company() \
            .click_header_about_company_button()
        biocad.about_company_page.is_opened()

    @allure.story('Переход на страницу "Наука"')
    @allure.title('Проверка перехода на страницу "Наука" через хедер меню')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_transition_to_science_page_from_header_menu(self):
        biocad.home_page.open()
        biocad.header_menu \
            .hover_to_about_company() \
            .click_header_science_button()
        biocad.science_page.is_opened()

    @allure.story('Переход на страницу "Научные публикации"')
    @allure.title('Проверка перехода на страницу "Научные публикации" через хедер меню')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_transition_to_science_publications_page_from_header_menu(self):
        biocad.home_page.open()
        biocad.header_menu \
            .hover_to_about_company() \
            .click_header_science_publications_button()
        biocad.science_publications_page.is_opened()

    @allure.story('Переход на страницу "Партнерство"')
    @allure.title('Проверка перехода на страницу "Партнерство" через хедер меню')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_transition_to_partnership_page_from_header_menu(self):
        biocad.home_page.open()
        biocad.header_menu \
            .hover_to_about_company() \
            .click_header_partnership_button()
        biocad.partnership_page.is_opened()

    @allure.story('Переход на страницу "Заказать препарат"')
    @allure.title('Проверка перехода на страницу "Заказать препарат" через хедер меню')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_transition_to_order_the_drug_page_from_header_menu(self):
        biocad.home_page.open()
        biocad.header_menu.click_header_order_the_drug_button()
        biocad.order_the_drug_page.is_opened()
