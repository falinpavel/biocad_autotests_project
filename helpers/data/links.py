import os

from dotenv import load_dotenv

load_dotenv()


class Links:
    """
    Класс содержит ссылки на все страницы сайта biocad.ru.
    """
    BASE_URL = os.getenv('BASE_URL')

    ABOUT_COMPANY_URL = f"{BASE_URL}/we"

    PARTNERSHIP_URL = f"{BASE_URL}/partnership"

    SCIENCE_URL = f"{BASE_URL}/science"

    SCIENCE_PUBLICATIONS_URL = f"{BASE_URL}/publications"

    ORDER_THE_DRUG_URL = f"{BASE_URL}/knv"
