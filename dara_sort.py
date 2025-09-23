"""
data_sorter.py

Модуль для сортировки данных с использованием pandas.
Задача: сортировка строк датафрейма по убыванию признака,
вывод первых N строк и проверка порядка.
"""

import pandas as pd
from sklearn.datasets import fetch_california_housing


def load_dataset():
    """
    Загружает датасет Boston Housing и возвращает DataFrame.
    
    Returns:
        pd.DataFrame: Датафрейм с признаками и целевой переменной.
    """
    try:
        data = fetch_california_housing(as_frame=True)
        df = data.frame
        return df
    except Exception as e:
        raise RuntimeError(f"DataSet loading error: {e}")


def sort_dataframe(df, column_name, top_n=10):
    """
    Сортирует датафрейм по убыванию указанного признака.

    Args:
        df (pd.DataFrame): Входной датафрейм.
        column_name (str): Название признака для сортировки.
        top_n (int): Количество строк для отображения (по умолчанию 10).

    Returns:
        pd.DataFrame: Отсортированный датафрейм.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' is missing from dataframe.")

    sorted_df = df.sort_values(by=column_name, ascending=False)
    return sorted_df.head(top_n)


def check_order(sorted_df, column_name):
    """
    Проверяет, отсортирован ли датафрейм по убыванию.

    Args:
        sorted_df (pd.DataFrame): Отсортированный датафрейм.
        column_name (str): Название признака.

    Returns:
        bool: True, если порядок правильный, иначе False.
    """
    return sorted_df[column_name].is_monotonic_decreasing


def main():
    """
    Основная функция:
    1. Загружает датасет.
    2. Сортирует по признаку.
    3. Выводит результат.
    4. Проверяет корректность сортировки.
    """
    try:
        df = load_dataset()
        column_to_sort = "HouseAge"  # параметр можно менять
        top_n = 10

        sorted_head = sort_dataframe(df, column_to_sort, top_n)
        print(f"First {top_n} lines, sorted by '{column_to_sort}':")
        print(sorted_head)

        if check_order(sorted_head, column_to_sort):
            print("Sorting is done correctly.")
        else:
            print("Sort errpr.")

    except Exception as e:
        print(f"Error occured: {e}")


if __name__ == "__main__":
    main()