from helpers.components.header_menu.component_header_menu import ComponentHeaderMenu
from helpers.pages.home_page.biocad_home_page import BiocadHomePage


class BiocadApplicationManager:
    """
    Класс менеджера приложения который инкапсулирует в себе все Page Object и другие объекты,
    необходимые для взаимодействия с приложением. Как итог - любые страницы и компоненты доступны в любом тесте.
    """
    def __init__(self):

        self.header_menu = ComponentHeaderMenu()

        self.home_page = BiocadHomePage()


biocad = BiocadApplicationManager()
