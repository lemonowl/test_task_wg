import re
from bs4 import BeautifulSoup
from test_1_pytest.pages.dataclass.table_item import TableItem


class MostPopularWebsitesTable(list):
    """"""
    pattern = r'(\[\d+\]|\n)'
    # текст для поиска правильной таблицы на странице
    caption = 'Programming languages used in most popular websites'
    # заголовки таблицы для проверки порядка столбцов
    expected_titles = ['Websites', 'Popularity(unique visitors per month)', 'Front-end(Client-side)',
                       'Back-end(Server-side)', 'Database', 'Notes']
    table = None

    def __init__(self, page_tree: BeautifulSoup):
        """Собирает таблицу Programming languages used in most popular websites
        """
        super().__init__()
        self.table = self.get_table(page_tree)
        self.check_titles()
        self.create_items_list()

    def get_table(self, page_tree):
        result = page_tree.findAll('caption', string=re.compile(self.caption))
        assert result != [], f'На странице не найден <caption> с текстом {self.caption}'
        return result[0].findParent('table')

    def get_titles(self):
        """Возвращает заголовки th таблицы
        """
        return [re.sub(self.pattern, '', item.text) for item in self.table.findAll('tr')[0].findAll('th')]

    def check_titles(self):
        """Проверяет, что столбцы расположены в правильном порядке
        """
        assert self.get_titles() == self.expected_titles

    @staticmethod
    def _convert_table_values(row_data):
        """Подготовка данных перед сохранением в LanguageItem
        """
        delimetr = ', '

        # преобразуем popularity в int
        row_data[1] = int(re.sub(r'(\D+)', '', row_data[1]))
        # преобразуем данные о front-end/back-end/databases в списки
        row_data[2] = row_data[2].split(delimetr)
        row_data[3] = row_data[3].split(delimetr)
        row_data[4] = row_data[4].split(delimetr)

    def create_items_list(self):
        """Метод получает данные со страницы, парсит их и возвращает список [LanguageItem]
        """
        # первый элемент таблицы - заголовки столбцов
        for tr in self.table.findAll('tr')[1:]:
            # удаляем сноски и символы переноса строки
            row_data = [re.sub(self.pattern, '', item.text) for item in tr.findAll('td')]
            self._convert_table_values(row_data)
            item = TableItem(*row_data)
            self.append(item)
