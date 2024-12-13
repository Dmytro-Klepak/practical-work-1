Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def remove_duplicates(lst):
...     # Видаляємо повтори за допомогою set
...     return list(set(lst))
... 
... def sort_list(lst):
...     # Спочатку відокремлюємо числа і рядки
...     numbers = [x for x in lst if isinstance(x, int)]
...     strings = [x for x in lst if isinstance(x, str)]
...     
...     # Сортуємо числа по зменшенню
...     numbers.sort(reverse=True)
...     
...     # Сортуємо рядки в алфавітному порядку
...     strings.sort()
...     
...     # Об'єднуємо результати: числа перші, потім рядки
...     return numbers + strings
... 
... # Приклад використання
... input_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'Hello']
... list_without_duplicates = remove_duplicates(input_list)
... sorted_list = sort_list(list_without_duplicates)
... 
... print("Список без повторів:", list_without_duplicates)
... print("Відсортований список:", sorted_list)
