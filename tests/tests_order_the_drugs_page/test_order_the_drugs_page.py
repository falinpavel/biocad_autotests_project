import allure

from helpers.application_manager.application_manager import biocad


@allure.epic('Страница "Заказать препарат"')
@allure.feature('Пользователь может на странице "Заказать препарат" выбрать препарат')
class TestOrderTheDrugsPage:

    @allure.story('Неавторизованный пользователь может на странице "Заказать препарат" '
                  'выбрать препарат и перейти к оформлению заказа')
    @allure.title('Проверка перехода к оформлению заказа препарата')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_choose_and_order_the_drugs(self):
        biocad.home_page.open()
        biocad.header_menu.click_header_order_the_drug_button()
        biocad.order_the_drug_page \
            .is_opened() \
            .click_order_the_drug_button() \
            .click_to_drug(drug_name='Тенексиа')
