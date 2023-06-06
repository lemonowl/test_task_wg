import pytest
from test_1_pytest.base.base_test_case import BaseTestCase
from test_1_pytest.pages.popular_websites_table import MostPopularWebsitesTable


class TestPLInPopularWebsitesTable(BaseTestCase):
    """Тесты таблицы на странице Programming languages used in most popular websites
    """
    # url страницы
    page_url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

    sites_table = None

    @classmethod
    def setup_class(cls):
        page_tree = cls.driver.get_page_parsed_content(cls.page_url)
        cls.sites_table = MostPopularWebsitesTable(page_tree)

    @pytest.mark.parametrize('expected',
                             (10**7, int(1.5*10**7), 5*10**7, 10**8, 5*10**8, 10**9, int(1.5*10**9)))
    def test_01_check_table(self, expected):
        """Тест проверяет, что в таблице нет строк, у которых значение в столбце
        «Popularity(unique visitors per month)» меньше передаваемого в качестве параметра в тест значения
        """
        errors = []
        for item in self.sites_table:
            if item.popularity < expected:
                errors.append(f"{item.website} (Frontend:{', '.join(item.frontend)}|Backend:{', '.join(item.backend)}) "
                              f"has {item.popularity} unique visitors per month. (Expected more than {expected})")
        assert errors == []
