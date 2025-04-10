# Тестирование класса BooksCollector

Этот проект содержит автоматизированные тесты для класса `BooksCollector`, который реализует функционал коллекции книг с возможностью добавления жанров и работы с избранным.

## Реализованные тесты

### 1. Тесты для метода `add_new_book`
- `test_add_new_book_add_one_book`:
  - Проверка добавления одной книги
  - Проверка невозможности добавления дубликата
- `test_add_new_book_len_check` (параметризованный):
  - Корректные названия (1-40 символов)
  - Некорректные названия (пустая строка, >40 символов)

### 2. Тесты для метода `set_book_genre`
- `test_set_book_genre_valid_genre`:
  - Установка валидного жанра ("Ужасы")
- `test_set_book_genre_invalid_genre`:
  - Попытка установки невалидного жанра ("Роман")

### 3. Тесты для метода `get_book_genre`
- `test_get_book_genre_show_books_genre`:
  - Получение жанра для книги с установленным жанром
  - Проверка для книги без жанра

### 4. Тесты для метода `get_books_with_specific_genre`
- `test_get_books_with_specific_genre_horror`:
  - Получение списка книг жанра "Ужасы"
  - Проверка количества найденных книг

### 5. Тесты для метода `get_books_genre`
- `test_get_books_genre_returns_correct_dictionary`:
  - Проверка возвращаемого словаря
  - Проверка количества элементов

### 6. Тесты для метода `get_books_for_children`
- `test_get_books_for_children_show_not_in_genre_age_rating`:
  - Проверка фильтрации по возрастному рейтингу
  - Проверка включения/исключения книг

### 7. Тесты для работы с избранным
- `test_add_book_in_favorites_twice`:
  - Добавление в избранное с проверкой на дублирование
- `test_add_book_to_favorites_book_out_of_dict`:
  - Попытка добавления несуществующей книги
- `test_delete_book_from_favorites_success`:
  - Удаление из избранного
- `test_get_list_of_favorites_books_2_books`:
  - Получение списка избранного с несколькими книгами
