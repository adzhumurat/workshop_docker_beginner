# Утилита docker-compose

В этом уроке мы автоматизируем запуск нескольких контейнеров с помощью docker-compose.

## Конфигурация docker-compose

Утилита конфигурируется с помощью yml-файлов. В репозитории присутствует файл [docker-compose.yml](../docker_compose/)

Сборку контейнера запускаем в виде

<pre>
docker-compose --project-name data-client -f docker-compose.yml build pg-cli
</pre>

После сборки нужно инициировать загрузку данных

<pre>
docker-compose --project-name data-cli -f docker-compose.yml run --rm --name pg-cli pg-cli load
</pre>

Проверим, что данные успешно загрузились

<pre>
docker-compose --project-name data-cli -f docker-compose.yml run --name pg-client --rm pg-cli psql -h postgres_ivi -U postgres -c "SELECT COUNT(*) FROM ratings;"
</pre>

Ожидаемый результат
<pre>
Starting postgres_ivi ... done
 count  
--------
 777776
(1 row)
</pre>

**Упражнение**: познакомьтесь в командой `docker exec`: подключитесь в терминал `psql` запущенного контейнера с Postgres `postgres_ivi` с помощью этой команды и выполните SQL запрос.
Чем `docker exec` отличается от `docker run`.

Если всё получилось - вы великолемны! Переходите к выполнению [домашней работы](./docker_mongo_hw.md)