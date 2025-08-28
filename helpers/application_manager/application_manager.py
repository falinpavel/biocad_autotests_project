from helpers.pages.home_page.biocad_home_page import BiocadHomePage
from helpers.pages.science_page.biocad_science_page import BiocadSciencePage
from helpers.components.header_menu.component_header_menu import ComponentHeaderMenu
from helpers.pages.partnership_page.biocad_partnership_page import BiocadPartnershipPage
from helpers.pages.about_company_page.biocad_about_company_page import BiocadAboutCompanyPage
from helpers.pages.order_the_drug_page.biocad_order_the_drug_page import BiocadOrderTheDrugPage
from helpers.pages.science_publications_page.biocad_science_publications_page import BiocadSciencePublicationsPage


class BiocadApplicationManager:
    """
    Класс менеджера приложения который инкапсулирует в себе все Page Object и другие объекты,
    необходимые для взаимодействия с приложением. Как итог - любые страницы и компоненты доступны в любом тесте.
    """
    def __init__(self):
        self.header_menu = ComponentHeaderMenu()

        self.home_page = BiocadHomePage()
        self.about_company_page = BiocadAboutCompanyPage()
        self.partnership_page = BiocadPartnershipPage()
        self.science_page = BiocadSciencePage()
        self.science_publications_page = BiocadSciencePublicationsPage()
        self.order_the_drug_page = BiocadOrderTheDrugPage()


biocad = BiocadApplicationManager()
