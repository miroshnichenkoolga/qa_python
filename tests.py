import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_one_book_true(self):
        collector = BooksCollector()

        wantBook = 'Гордость и предубеждение и зомби'
        collector.add_new_book(wantBook)

        wantCount = 1
        gotBooks = collector.get_books_genre()

        assert len(gotBooks) == wantCount


    @pytest.mark.parametrize('name_book',
                             ['', '41символ полночи Автор:Семен Бобриковский',
                              '42символа Тройке:Аркадий, Борис Стругацкие'])
    def test_add_new_book_zero_or_more_41_(self, name_book):
        collector = BooksCollector()
        count = len(collector.get_books_genre())

        collector.add_new_book(name_book)

        wantCount = count
        gotBooks = collector.get_books_genre()

        assert len(gotBooks) == wantCount


    def test_set_book_genre_one_book_true(self):
        collector = BooksCollector()
        name = 'Зомби'
        collector.add_new_book(name)
        want = 'Ужасы'

        collector.set_book_genre(name, want)

        got = collector.get_book_genre(name)
        assert got == want

    def test_get_book_genre_positive_result(self):
        collector = BooksCollector()
        name = 'Золушка'
        collector.add_new_book(name)
        want = 'Мультфильмы'
        collector.set_book_genre(name, want)

        got = collector.get_book_genre(name)
        assert got == want

    def test_get_books_with_specific_genre_positive_result(self):
        collector = BooksCollector()
        name = 'Золушка'
        collector.add_new_book(name)
        genre = 'Мультфильмы'
        collector.set_book_genre(name, genre)

        name1 = 'Зол'
        collector.add_new_book(name1)
        genre1 = 'Ужасы'
        collector.set_book_genre(name1, genre1)

        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_for_children_positive_result(self):
        collector = BooksCollector()
        name = 'Золушка'
        collector.add_new_book(name)
        genre = 'Мультфильмы'
        collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == [name]

    def test_get_books_for_children_genre_age_rating_negative_result(self):
        collector = BooksCollector()
        name = 'Зол'
        collector.add_new_book(name)
        genre = 'Ужасы'
        collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_positive_result(self):
        collector = BooksCollector()
        name = 'Зди15'
        collector.add_new_book(name)
        genre = 'Ужасы'
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books() == [name]


    def test_add_book_in_favorites_add_same_book_twice_negative_result(self):
        collector = BooksCollector()

        name = 'Зди15'
        collector.add_new_book(name)
        genre = 'Ужасы'
        collector.set_book_genre(name, genre)

        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books() == [name]

    def test_delete_book_from_favorites_positive_result(self):
        collector = BooksCollector()
        name = 'Зди15'
        collector.add_new_book(name)
        genre = 'Ужасы'
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_positive_result(self):
        collector = BooksCollector()
        name = 'Зодиак15'
        collector.add_new_book(name)
        genre = 'Ужасы'
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books() == [name]
