[33mcommit 3b9bb148a895098d84fbcee46b8e0a8f437b151a[m
Author: Наталья Никитина <153123991+NataliSnail@users.noreply.github.com>
Date:   Tue Dec 12 21:01:40 2023 +0300

    Initial commit

[1mdiff --git a/README.md b/README.md[m
[1mnew file mode 100644[m
[1mindex 0000000..1cc701d[m
[1m--- /dev/null[m
[1m+++ b/README.md[m
[36m@@ -0,0 +1 @@[m
[32m+[m[32m# qa_python[m
\ No newline at end of file[m
[1mdiff --git a/__pycache__/main.cpython-38.pyc b/__pycache__/main.cpython-38.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..5786eeb[m
Binary files /dev/null and b/__pycache__/main.cpython-38.pyc differ
[1mdiff --git a/__pycache__/test.cpython-38-pytest-7.1.2.pyc b/__pycache__/test.cpython-38-pytest-7.1.2.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..b2898a8[m
Binary files /dev/null and b/__pycache__/test.cpython-38-pytest-7.1.2.pyc differ
[1mdiff --git a/main.py b/main.py[m
[1mnew file mode 100644[m
[1mindex 0000000..d3e0a17[m
[1m--- /dev/null[m
[1m+++ b/main.py[m
[36m@@ -0,0 +1,57 @@[m
[32m+[m[32mclass BooksCollector:[m
[32m+[m
[32m+[m[32m    def __init__(self):[m
[32m+[m[32m        self.books_genre = {}[m
[32m+[m[32m        self.favorites = [][m
[32m+[m[32m        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'][m
[32m+[m[32m        self.genre_age_rating = ['Ужасы', 'Детективы'][m
[32m+[m
[32m+[m[32m    # добавляем новую книгу[m
[32m+[m[32m    def add_new_book(self, name):[m
[32m+[m[32m        if not self.books_genre.get(name) and 0 < len(name) < 41:[m
[32m+[m[32m            self.books_genre[name] = ''[m
[32m+[m
[32m+[m[32m    # устанавливаем книге жанр[m
[32m+[m[32m    def set_book_genre(self, name, genre):[m
[32m+[m[32m        if name in self.books_genre and genre in self.genre:[m
[32m+[m[32m            self.books_genre[name] = genre[m
[32m+[m
[32m+[m[32m    # получаем жанр книги по её имени[m
[32m+[m[32m    def get_book_genre(self, name):[m
[32m+[m[32m        return self.books_genre.get(name)[m
[32m+[m
[32m+[m[32m    # выводим список книг с определённым жанром[m
[32m+[m[32m    def get_books_with_specific_genre(self, genre):[m
[32m+[m[32m        books_with_specific_genre = [][m
[32m+[m[32m        if self.books_genre and genre in self.genre:[m
[32m+[m[32m            for name, book_genre in self.books_genre.items():[m
[32m+[m[32m                if book_genre == genre:[m
[32m+[m[32m                    books_with_specific_genre.append(name)[m
[32m+[m[32m        return books_with_specific_genre[m
[32m+[m
[32m+[m[32m    # получаем словарь books_genre[m
[32m+[m[32m    def get_books_genre(self):[m
[32m+[m[32m        return self.books_genre[m
[32m+[m
[32m+[m[32m    # возвращаем книги, подходящие детям[m
[32m+[m[32m    def get_books_for_children(self):[m
[32m+[m[32m        books_for_children = [][m
[32m+[m[32m        for name, genre in self.books_genre.items():[m
[32m+[m[32m            if genre not in self.genre_age_rating and genre in self.genre:[m
[32m+[m[32m                books_for_children.append(name)[m
[32m+[m[32m        return books_for_children[m
[32m+[m
[32m+[m[32m    # добавляем книгу в Избранное[m
[32m+[m[32m    def add_book_in_favorites(self, name):[m
[32m+[m[32m        if name in self.books_genre:[m
[32m+[m[32m            if name not in self.favorites:[m
[32m+[m[32m                self.favorites.append(name)[m
[32m+[m
[32m+[m[32m    # удаляем книгу из Избранного[m
[32m+[m[32m    def delete_book_from_favorites(self, name):[m
[32m+[m[32m        if name in self.favorites:[m
[32m+[m[32m            self.favorites.remove(name)[m
[32m+[m
[32m+[m[32m    # получаем список Избранных книг[m
[32m+[m[32m    def get_list_of_favorites_books(self):[m
[32m+[m[32m        return self.favorites[m
[1mdiff --git a/tests.py b/tests.py[m
[1mnew file mode 100644[m
[1mindex 0000000..383385e[m
[1m--- /dev/null[m
[1m+++ b/tests.py[m
[36m@@ -0,0 +1,24 @@[m
[32m+[m[32mfrom main import BooksCollector[m
[32m+[m
[32m+[m[32m# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector[m
[32m+[m[32m# обязательно указывать префикс Test[m
[32m+[m[32mclass TestBooksCollector:[m
[32m+[m
[32m+[m[32m    # пример теста:[m
[32m+[m[32m    # обязательно указывать префикс test_[m
[32m+[m[32m    # дальше идет название метода, который тестируем add_new_book_[m
[32m+[m[32m    # затем, что тестируем add_two_books - добавление двух книг[m
[32m+[m[32m    def test_add_new_book_add_two_books(self):[m
[32m+[m[32m        # создаем экземпляр (объект) класса BooksCollector[m
[32m+[m[32m        collector = BooksCollector()[m
[32m+[m
[32m+[m[32m        # добавляем две книги[m
[32m+[m[32m        collector.add_new_book('Гордость и предубеждение и зомби')[m
[32m+[m[32m        collector.add_new_book('Что делать, если ваш кот хочет вас убить')[m
[32m+[m
[32m+[m[32m        # проверяем, что добавилось именно две[m
[32m+[m[32m        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2[m
[32m+[m[32m        assert len(collector.get_books_rating()) == 2[m
[32m+[m
[32m+[m[32m    # напиши свои тесты ниже[m
[32m+[m[32m    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()[m
\ No newline at end of file[m
