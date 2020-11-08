# Команда `docker network`

В этом разделе поговорим о том, как общаются контейнеры друг с другом и внешним миром

## Создание сети для докер-контейнеров

Чтобы создать сеть достаточно выполнить команду 

```shell script
docker network create -d bridge proj_network
```

В данной команде `bridge` - это тип драйвера для сети. У докера есть и [другие типы драйверов](https://blog.docker.com/2016/12/understanding-docker-networking-drivers-use-cases/), обсуждение их различиий выходит за пределы данного воркшопа.

Чтобы проверить успешность создания сети, воспользуйтесь командой 
```shell script
docker network ls
```

Результат работы команды
```shell script
NETWORK ID          NAME                        DRIVER              SCOPE
8fa50d79adf1        proj_network            bridge              local
```

Готово! Теперь мы знаем, как создать сеть между контейнерами. Осталось научиться [использовать эту сеть](./container_connection.md)

