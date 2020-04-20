import datetime
import hashlib
import json
import os
import zipfile


class Constant:
    # путь до директории с zip-архивом
    current_script_dir = os.path.dirname(os.path.realpath(__file__))
    # ищем путь до "соседней" директории, где будем хранить данные для работы
    data_dir = os.path.join(current_script_dir, '..', 'data_store')
    # сценариии обработки данных
    extract = 'extract'
    # список файлов, которые будем извлекать из архива - чтобы не извлекать ничего лишнего
    filenames = ('links.csv', 'ratings.csv', 'tags.json')
    # директории, которые будут созданы
    raw_data_dir = 'raw_data'
    postgres_data_dir = 'pg_data'
    mongo_data_dir = 'mongo_data'
    child_dirs = (postgres_data_dir, mongo_data_dir)
    # Архив для распаковки
    zipped_data_path = os.path.join(data_dir, 'raw_data.zip')


def extract():
    """Функция для извлечения файлов из архива movies_data.zip
    Создаём дочерние директории и извлекаем туда файлы
    Предварительно упаковали с помощью
    rm data_store/raw_data.zip; zip -rj data_store/raw_data.zip data_store/raw_data
    :return:
    """
    # создание дочерних директорий
    for child_dir in Constant.child_dirs:
        child_dir_path = os.path.join(Constant.data_dir, child_dir)
        if not os.path.exists(child_dir_path):
            os.mkdir(child_dir_path)
        else:
            print(f'Директория {child_dir_path} уже существует')

    # распаковываем файлы
    with zipfile.ZipFile(Constant.zipped_data_path, mode='r', compression=zipfile.ZIP_DEFLATED) as z:
        for member in Constant.filenames:
            file_name = os.path.basename(member)
            # распакуется в data_store/raw_data
            z.extract(os.path.join('raw_data', file_name), Constant.data_dir)
    print(f'Файлы распакованы в {Constant.data_dir}/{Constant.data_dir}')


if __name__ == '__main__':
    extract()