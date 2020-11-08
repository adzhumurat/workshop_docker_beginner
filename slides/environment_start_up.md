# Подготовка машины к работе

## Установка docker

Если у вас Мак или Линукс, то проблем с установкой докера не будет - на офсайте есть хорошие инструкции
* [тут Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [тут MacOS](https://docs.docker.com/docker-for-mac/install/)
* Если у вас Windows, то для установки `docker toolbox` нужно использовать вот [эту инструкцию](https://docs.docker.com/toolbox/toolbox_install_windows/) и затем [установить сам docker](https://docs.docker.com/docker-for-windows/install/)

Когда docker будет установлен, проверьте его работу командой
```shell script
docker run hello-world
```

Если не работает, или работает только с `sudo` - продолжайте настраивать. Когда заработает - можно переходить к загрузке исходных данных.

Так же понадобится утилита `docker-compose`, устанавливать [строго по инструкции с официального сайта](https://docs.docker.com/compose/install/)

## Распаковка csv

Данные для воркшопа содержатся в архиве `raw_data.zip` директории [data_store](../data_store)

Файлы должны быть извлечены в директорию `data_store/raw_data`. Это можно сделать вручную, либо запустив скрипт

```shell script
python3 -m data_tools
```

```shell script
ls data_store
```

Результат работы команды
```shell script
raw_data, pg_data, mongo_data
```

Проверьте корректность распаковки с помощью команды

```shell script
ls data_store/raw_data
```

Результат работы команды
```shell script
links.csv ratings.csv tags.json
```

Если данные в директории есть - поздравляю, вы полностью готовы к участию в воркшопе! Перед началом практики познакомимся с [основными концепциями Docker](./docker_intro.md).
