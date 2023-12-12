import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) ==2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('genre',
                             [
                                 'Фантастика',
                                 'Ужасы',
                                 'Детективы',
                                 'Мультфильмы',
                                 'Комедии'
                             ]
                             )
    def test_get_genres_true(self, genre):  # 1 проверить список доступных  жанров genre
        for i in genre:
            assert genre

    def test_add_new_book_true(self):  # 2 добавляем новую книгу
        books_collection = BooksCollector()
        books_collection.add_new_book('Братья Карамазовы')
        books_collection.add_new_book('Машина времени')
        assert len(books_collection.get_books_genre()) == 2

    def test_set_genre_for_book_true(self):  # 3 устанавливаем книге жанр
        books_collection = BooksCollector()
        books_collection.add_new_book('Щелкунчик')
        books_collection.set_book_genre('Щелкунчик', 'Мультфильмы')
        assert 'Мультфильмы' == books_collection.get_book_genre('Щелкунчик')

    def test_get_book_genre_true(self):  # 4 получаем жанр книги по её имени
        books_collection = BooksCollector()
        books_collection.add_new_book('Щелкунчик')
        books_collection.set_book_genre('Щелкунчик', 'Мультфильмы')
        assert books_collection.get_book_genre('Щелкунчик')== 'Мультфильмы'

    def test_get_books_with_specific_genre(self):  # 5. выводим список книг с определённым жанром
        books_specific_genre = BooksCollector()
        books_specific_genre.add_new_book('Парк юркского периода')
        books_specific_genre.set_book_genre('Парк юркского периода', 'Ужасы')
        books_specific_genre.get_books_with_specific_genre('Парк юркского периода')
        assert len(books_specific_genre.get_books_with_specific_genre('Ужасы')) == 1

    def test_get_books_genre_true(self):  # 6 получаем словарь books_genre
        books_collection = BooksCollector()
        books_collection.add_new_book('Братья Карамазовы')
        books_collection.set_book_genre('Братья Карамазовы', 'Классика')
        assert books_collection.get_books_genre()

    def test_get_books_for_children(self):  # 7 возвращаем книги, подходящие детям
        books_collection = BooksCollector()
        books_collection.add_new_book('Алые паруса')
        books_collection.set_book_genre('Алые паруса', 'Мультфильмы')
        assert len(books_collection.get_books_for_children()) == 1

    def test_add_book_in_favorites(self):  # 8 добавляем книгу в Избранное
        book_favorites = BooksCollector()
        book_favorites.add_new_book('Братья Карамазовы')
        book_favorites.add_book_in_favorites('Братья Карамазовы')
        assert len(book_favorites.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):  # 9 удаляем книгу из Избранного
        book_favorites = BooksCollector()
        book_favorites.add_new_book('Братья Карамазовы')
        book_favorites.add_new_book('Анна Каренина')
        book_favorites.add_book_in_favorites('Братья Карамазовы')
        book_favorites.add_book_in_favorites('Анна Каренина')
        book_favorites.delete_book_from_favorites('Анна Каренина')
        assert len(book_favorites.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_true(self):  # 10 получаем список Избранных книг
        book_favorites = BooksCollector()
        book_favorites.add_new_book('Братья Карамазовы')
        book_favorites.add_book_in_favorites('Братья Карамазовы')
        assert len(book_favorites.get_list_of_favorites_books()) == 1