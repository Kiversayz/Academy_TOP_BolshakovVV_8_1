import pickle

class CountryCapitalDict:
    """
    Класс для управления данными стран и столиц.
    """

    def __init__(self):
        """
        Инициализация пустого словаря для хранения данных стран и столиц.
        """
        self.data = {}

    def add_country(self, country, capital):
        """
        Добавление новой страны и её столицы в словарь.
        param country Название страны
        param capital Столица страны
        """
        self.data[country] = capital
        print(f"Страна {country} со столицой {capital} добавлена.")

    def remove_country(self, country):
        """
        Удаление страны из словаря по названию.
        param country Название страны для удаления
        """
        if country in self.data:
            del self.data[country]
            print(f"Страна {country} удалена.")
        else:
            print(f"Страна {country} не найдена.")

    def find_country(self, country):
        """
        Поиск столицы страны по её названию.
        param country Название страны
        """
        if country in self.data:
            print(f"Страна {country} имеет столицу {self.data[country]}.")
        else:
            print(f"Страна {country} не найдена.")

    def edit_country(self, country, new_capital):
        """
        Изменение столицы для существующей страны.
        param country Название страны, для которой нужно изменить столицу
        param new_capital Новая столица
        """
        if country in self.data:
            self.data[country] = new_capital
            print(f"Столицу страны {country} изменили на {new_capital}.")
        else:
            print(f"Страна {country} не найдена.")


class DataPacker:
    """
    Класс для упаковки и распаковки данных с использованием модуля pickle.
    """

    def __init__(self, filename):
        """
        Инициализация с именем файла для сохранения и загрузки данных.
        param filename Имя файла для сохранения и загрузки
        """
        self.filename = filename

    def save_data(self, data):
        """
        Сохранение данных в файл с использованием pickle.
        param data Данные для сохранения (например, словарь)
        """
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)
        print(f"Данные сохранены в файл {self.filename}.")

    def load_data(self):
        """
        Загрузка данных из файла с использованием pickle.
        return Загруженные данные, если файл существует, иначе пустой словарь
        """
        try:
            with open(self.filename, 'rb') as f:
                data = pickle.load(f)
            print(f"Данные загружены из файла {self.filename}.")
            return data
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден.")
            return {}



if __name__ == "__main__":
    country_capital = CountryCapitalDict()

    print('Добавляем несколько стран и их столицы')
    country_capital.add_country("Россия", "Москва")
    country_capital.add_country("Франция", "Париж")
    country_capital.add_country("Япония", "Токио")

    print('\nРедактируем столицу')
    country_capital.edit_country("Япония", "Осака")

    print('\nИщем страну')
    country_capital.find_country("Франция")
    country_capital.find_country("Италия")

    print('\nУдаляем страну')
    country_capital.remove_country("Россия")

    print('\nСоздаем объект для сохранения и загрузки данных')
    packer = DataPacker("countries_and_capitals.pkl")

    print('\nСохраняем данные в файл')
    packer.save_data(country_capital.data)

    print('\nЗагружаем данные из файла')
    loaded_data = packer.load_data()
    print("\nЗагруженные данные:", loaded_data)