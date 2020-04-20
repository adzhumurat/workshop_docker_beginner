# Утилита docker-compose

В этом уроке мы автоматизируем запуск нескольких контейнеров с помощью docker-compose.

## Конфигурация docker-compose

Утилита конфигурируется с помощью yml-файлов. В репозитории присутствует файл [docker-compose.yml](../docker_compose/)

Для начала перейдём в директорию `docker_compose` и запустим сборку контейнера в виде

<pre>
docker-compose --project-name data-client -f docker-compose.yml build pg-cli
</pre>

После сборки нужно инициировать загрузку данных

<pre>
SOURCE_DIR=$(pwd) docker-compose --project-name data-cli -f docker-compose.yml run --rm --name pg-cli pg-cli load
</pre>

Проверим, что данные успешно загрузились

<pre>
SOURCE_DIR=$(pwd) docker-compose --project-name data-cli -f docker-compose.yml run --name pg-client --rm pg-cli psql -h postgres_proj -U postgres -c "SELECT COUNT(*) FROM ratings;"
</pre>

Ожидаемый результат
<pre>
Starting postgres_proj ... done
 count  
--------
 777776
(1 row)
</pre>

**Упражнение**: познакомьтесь в командой `docker exec`: подключитесь в терминал `psql` запущенного контейнера с Postgres `postgres_proj` с помощью этой команды и выполните SQL запрос.
Чем `docker exec` отличается от `docker run`.

Если всё получилось - вы великолемны! Переходите к выполнению [домашней работы](./docker_mongo_hw.md)