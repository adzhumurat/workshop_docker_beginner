# Использование docker build

Мы научились запускать уже готовые образы Docker. Хотелось бы начать создавать кастомные контейнеры.
Самое время узнать о Dockerfile и команде docker build!

## Dockerfile

В registry храняться уже готовые образы, которые мы использовали при разворачивании Postgres.
На базе готовых образов можно создавать свои образы и билдить на их основе контейнеры.
В этом уроке мы соберём свой собственный образ из базового образа Ubuntu:18.04.

Создать образ - значит, описать его в виде Dockerfile. В репозитории присутствует [Dockerfile](../docker_compose/data_client/Dockerfile) для образа с `psql` и `pipenv` на борту.

Как правильно создавать образы

1. Всегда указывайте конкретный тэг базового образа, никогда не используйте тэг `latest`
1. Docker использует [union fs](./docker_intro.md) - чем меньше слоёв в контейнере, тем лучше. Каждая инструкция `RUN`, `COPY`, `ADD` создаёт новый слой, поэтому старайтесь объединить как можно больше объединять команды друг с другом.
1. Используйте `COPY` вместо `ADD`

Обязательно почитайте две статьи на Хабре [Docker: вредные советы](https://habr.com/ru/company/southbridge/blog/449944/) и [Docker: невредные советы](https://habr.com/ru/company/southbridge/blog/452108/) и [советы от разработчиков Docker](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

## Запуск контейнеров

Чтобы собрать контейнер из образа, перейдите в директорию `data_client` и выполните команду
<pre>
docker build -t pg_client:1.0 .
</pre>

После того, как сборка будет завершена, подключитеcь в контейнер

<pre>
docker run --volume $(pwd)/pg_client:/srv/pg_client --network proj_network -it --rm pg_client:1.0 bash
</pre>

Отключитесь от контейнера и проверьте работу `docker-entrypoint.sh` запустив команду
<pre>
docker run -v $(pwd)/pg_client:/srv/pg_client -v ${SOURCE_DATA}/raw_data:/usr/share/raw_data -e APP_POSTGRES_HOST=proj-postgres --network proj_network -it --rm pg_client:1.0 load
</pre>

Ожидаемый результат - в консоли побегут логи загрузки данных
<pre>
DROP TABLE
DROP TABLE
Загружаем links.csv...
CREATE TABLE
COPY 45843
Загружаем ratings.csv...
CREATE TABLE
COPY 777776
</pre>

Мы научились собирать кастомные контейнеры с помощью `docker build` и модифицировать поведение контейнеров в `docker-entrypoint.sh`
Однако поднимать вручную десятки контейнеров не очень удобно, возникает желание как-то автоматизировать этот процесс - давайте воспользуемся предназначенной для этих целей [утилитой docker-compose](./docker_compose.md)
