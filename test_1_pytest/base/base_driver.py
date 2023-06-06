import requests
from bs4 import BeautifulSoup


class BaseDriver:
    """Базовый драйвер для работы со страницей
    """

    @staticmethod
    def get(url, params=None, **kwargs) -> requests.Response:
        return requests.get(url, params, **kwargs)

    def get_page_content(self, url, status_code=200) -> str:
        """Метод получает и возвращает содержимое страницы
        """
        result = self.get(url)
        assert result.status_code == status_code
        return result.text

    def get_page_parsed_content(self, url: str) -> BeautifulSoup:
        """Метод парсит страницу для дальнейшей обработки
        """
        content = self.get_page_content(url)
        return BeautifulSoup(content, 'lxml')
