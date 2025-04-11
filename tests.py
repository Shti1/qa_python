import pytest

class TestBooksCollector:

    def test_add_new_book_add_one_book(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.books_genre
        assert collector.books_genre["Гордость и предубеждение и зомби"] == ""

        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        'name, result',
        [
            ('Алые паруса', True),
            ('А' * 40, True),
            ('', False),
            ('А' * 41, False)
        ]
    )
    def test_add_new_book_len_check(self, name, result, collector):
        collector.add_new_book(name)
        assert (name in collector.books_genre) == result

    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Ужасы' in collector.genre
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Роман')
        assert 'Роман' not in collector.genre
        assert  collector.get_book_genre('Война и мир') == ''

    def test_get_book_genre_show_books_genre(self, collector):
        collector.add_new_book('Зима в Простоквашино')
        collector.set_book_genre('Зима в Простоквашино', 'Мультфильмы')
        collector.add_new_book('Метро 2033')
        assert collector.get_book_genre("Зима в Простоквашино") == "Мультфильмы"
        assert collector.get_book_genre("Метро 2033") == ''

    def test_get_books_with_specific_genre_horror(self, collector):
        collector.add_new_book('Сияние')
        collector.add_new_book('Темная половина')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Темная половина', 'Ужасы')
        assert 'Сияние' in collector.get_books_with_specific_genre('Ужасы')
        assert 'Темная половина' in collector.get_books_with_specific_genre('Ужасы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_genre_returns_correct_dictionary(self, collector, collector_with_books):
        test_books = {
            "Оно": "Ужасы",
            "Шерлок Холмс": "Детективы",
            "Хоббит": "Фантастика"
        }
        assert collector.get_books_genre() == test_books
        assert len(collector.get_books_genre()) == 3

    def test_get_books_for_children_show_not_in_genre_age_rating(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Гарри Поттер' in collector.get_books_for_children()
        assert 'Оно' not in collector.get_books_for_children()
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.add_book_in_favorites('Убийство в Восточном экспрессе')
        collector.add_book_in_favorites('Убийство в Восточном экспрессе')
        assert 'Убийство в Восточном экспрессе' in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_to_favorites_book_out_of_dict(self, collector):
        collector.add_book_in_favorites('Книга не из словаря')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book('Парфюмер')
        collector.add_book_in_favorites('Парфюмер')
        assert 'Парфюмер' in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites('Парфюмер')
        assert 'Парфюмер' not in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_2_books(self, collector):
        collector.add_new_book('Песнь льда и пламени')
        collector.add_new_book('НИ СЫ')
        collector.add_new_book('Дубровский')
        collector.add_book_in_favorites('Песнь льда и пламени')
        assert 'Песнь льда и пламени' in collector.get_list_of_favorites_books()
        collector.add_book_in_favorites('Дубровский')
        assert 'Дубровский' in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites('Парфюмер')
        assert len(collector.get_list_of_favorites_books()) == 2
