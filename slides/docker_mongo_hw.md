# Домашняя работа

Для выполнения домашней работы нужно

1. Поднимите контейнер MongoDB с тэгом `mongo:4.1.6`, подключив его к сети `proj_network`
1. Поднимите контейнер `pg_client:1.0`замаунтив директорию `${SOURCE_DATA}/raw_data`
1. Залейте в MongoDB файл `tags.json` с помощью команды `/usr/bin/mongoimport --host $APP_MONGO_HOST --port $APP_MONGO_PORT --db movie --collection tags --file /usr/share/mongo_data/tags.json`
1. Проверьте, что данные успешно попали в MongoDB `/usr/bin/mongo $APP_MONGO_HOST:$APP_MONGO_PORT/movies`
1. Добавьте сервис с MomgoDB в `docker-compose.yml`