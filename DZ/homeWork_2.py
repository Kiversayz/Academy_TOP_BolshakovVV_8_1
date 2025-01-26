import pickle

class MusicGroupAlbumDict:
    """
    Класс для управления данными музыкальных групп и их альбомов.
    """

    def __init__(self):
        """
        Инициализация пустого словаря для хранения данных групп и альбомов.
        """
        self.data = {}

    def add_group(self, group, albums):
        """
        Добавление новой музыкальной группы и её альбомов в словарь.
        param group Название музыкальной группы
        param albums Список альбомов группы
        """
        self.data[group] = albums
        print(f"Группа {group} с альбомами {albums} добавлена.")

    def remove_group(self, group):
        """
        Удаление музыкальной группы из словаря по названию.
        param group Название группы для удаления
        """
        if group in self.data:
            del self.data[group]
            print(f"Группа {group} удалена.")
        else:
            print(f"Группа {group} не найдена.")

    def find_group(self, group):
        """
        Поиск альбомов группы по её названию.
        param group Название музыкальной группы
        """
        if group in self.data:
            print(f"Группа {group} имеет альбомы: {self.data[group]}.")
        else:
            print(f"Группа {group} не найдена.")

    def edit_group(self, group, new_albums):
        """
        Изменение альбомов для существующей группы.
        param group Название группы, для которой нужно изменить альбомы
        param new_albums Новый список альбомов
        """
        if group in self.data:
            self.data[group] = new_albums
            print(f"Альбомы группы {group} изменены на {new_albums}.")
        else:
            print(f"Группа {group} не найдена.")


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
    music_group_album = MusicGroupAlbumDict()
    print('Добавляем несколько групп и их альбомы')         
    
    music_group_album.add_group("The Beatles", ["Abbey Road", "Let It Be", "Revolver"])
    music_group_album.add_group("Queen", ["A Night at the Opera", "News of the World", "Bohemian Rhapsody"])
    music_group_album.add_group("Pink Floyd", ["The Dark Side of the Moon", "The Wall", "Wish You Were Here"])
    print()
    
    print('Редактируем альбомы группы')
    music_group_album.edit_group("Pink Floyd", ["Animals", "The Final Cut", "The Piper at the Gates of Dawn"])
    print()
    
    print('Ищем группу')
    music_group_album.find_group("Queen")
    music_group_album.find_group("Led Zeppelin")
    print()
    
    print('Удаляем группу')
    music_group_album.remove_group("The Beatles")
    print()
    
    print('Создаем объект для сохранения и загрузки данных')
    packer = DataPacker("music_groups_and_albums.pkl")
    print()
    
    print('Сохраняем данные в файл')
    packer.save_data(music_group_album.data)
    print()
    
    print('Загружаем данные из файла')
    loaded_data = packer.load_data()
    print("\nЗагруженные данные:", loaded_data)