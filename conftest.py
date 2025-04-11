import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def collector_with_books(collector):
    collector.add_new_book("Оно")
    collector.set_book_genre("Оно", "Ужасы")
    collector.add_new_book("Шерлок Холмс")
    collector.set_book_genre("Шерлок Холмс", "Детективы")
    collector.add_new_book("Хоббит")
    collector.set_book_genre("Хоббит", "Фантастика")
    return collector