# API для категоризации тренировок 

Система классификации типов тренировок на основе данных о физической активности

---

#### Для запуска необходимо выполнить команду:
```
docker compose up --build
```

#### API будет доступно по адресу:

```
http://localhost:8080/api/v1/
```

#### Интерактивная документация доступна по адресу:
```
http://localhost:8080/docs/swagger/
```

---

### Описание эндпоинтов

Подсчет оценки интенсивности и типа переданных тренировок:
- На вход подается список тренировок в формате json
- На выходе список переданных тренировок с подсчитанными интенсивность и типом

Пример запроса:

```
curl -X 'POST' \
  'http://127.0.0.1:8080/api/v1/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "content": [
    {
      "average_heartrate": 130.0,
      "average_speed": 9.0,
      "distance": 35000.0,
      "moving_time": 3700.0,
      "total_elevation_gain": 150.0,
      "type": "Ride"
    },
    {
      "average_heartrate": 190.0,
      "average_speed": 5,
      "distance": 200,
      "moving_time": 60,
      "total_elevation_gain": 300,
      "type": "Run"
    }
  ]
}'
```

Пример ответа:

```
{
  "content": [
    {
      "average_heartrate": 130,
      "average_speed": 9,
      "distance": 35000,
      "intensity_score": 0.7569731347900616,
      "moving_time": 3700,
      "target": 3,
      "total_elevation_gain": 150,
      "type": "Ride"
    },
    {
      "average_heartrate": 190,
      "average_speed": 5,
      "distance": 200,
      "intensity_score": 1.186110545598754,
      "moving_time": 60,
      "target": 5,
      "total_elevation_gain": 300,
      "type": "Run"
    }
  ]
}
```

---