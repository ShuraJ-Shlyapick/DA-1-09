# DA-1-09

## Описание
Программа загружает датасет "California Housing" из библиотеки "scikit-learn" и выводит 10 строчек отсортированные по заданному признаку (column_to_sort) с помощью функции pandas.DataFrame.sort_values.

Использование датасета "Boston Housing Dataset" не является возможным, потому что он устарел и не используется библиотекой с версии 1.2

## Требования

* Python 3.13+
* sandas 
* scikit-learn 

### Установка

pip install requirements.txt

## Запуск программы 

python DA-1-09.py

## Обзор функций

load_dataset() -> pd.DataFrame

Загружает датасет California Housing.

sort_dataframe(df: pd.DataFrame, column_name: str, top_n: int = 10) -> pd.DataFrame

Сортирует датафрейм по убыванию выбранного признака, возвращает первые top_n строк.
Выполняет проверки на тип данных и корректность аргументов.

check_order(sorted_df: pd.DataFrame, column_name: str) -> bool

Проверяет, отсортированы ли данные по убыванию.

main()

Пример использования: загрузка датасета, сортировка по колонке, вывод результата и проверка.
