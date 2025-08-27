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
