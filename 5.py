# В прикреплённом файле содержится программа, которая вычисляет количество строк кода в некотором каталоге.
# Не переименовывая функции, допишите недостающий код в функциональном стиле.
# Императивные конструкции if/for/while в этой задаче использовать нельзя. Допустимо частичное решение.

import os
import sys
import itertools

def project_stats(path, extensions):
    """
    Вернуть число строк в исходниках проекта.

    Файлами, входящими в проект, считаются все файлы
    в папке ``path`` (и подпапках), имеющие расширение
    из множества ``extensions``.
    """
    pass

###   работает, но неизвестно зачтено или нет
def total_number_of_lines(filenames):
    """
    Вернуть общее число строк в файлах ``filenames``.
    """
    return sum(map(number_of_lines, filenames.split()))


###   ЗАЧТЕНО
def number_of_lines(filename):
    """
    Вернуть число строк в файле.
    """
    with open(filename) as f: # файл является итерируемым объектом по строкам, поэтомы такое возможно
        count = sum(1 for _ in f)

    return count
### ============


def iter_filenames(path):
    """
    Итератор по именам файлов в дереве.
    """
    pass


def with_extensions(extensions, filenames):
    """
    Оставить из итератора ``filenames`` только
    имена файлов, у которых расширение - одно из ``extensions``.
    """
    pass

### РАБОТАЕТ, ЗАЧТЕНО ИЛИ НЕТ ХЗ
def get_extension(filename):
    """ Вернуть расширение файла """
    filename, file_extension = os.path.splitext(filename)
    return file_extension



def print_usage():
    print("Usage: python project_sourse_stats_3.py <project_path>")


#if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        print_usage()
#        sys.exit(1)
#
#    project_path = sys.argv[1]
#    print(project_stats(project_path, {'.py'}))

# print(total_number_of_lines('testText.txt testText1.txt'))

# print(get_extension('testText.txt'))


