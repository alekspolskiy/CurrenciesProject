# Currencies
This is a simple application that simulates the work of the currency exchange. We have test data with a test currency name and price for each point in time. This data is updated every second.
## How to run project 
Go to CurrenciesProject/backend and run:
```
make docker-build-local
```
After backend builded go to CurrenciesProject/frontend and run:
```
npm install
```
And finally:
```
npm run serve
```
Open browser at http://localhost:8080/main

## API
### Get currencies
GET: /api/v1/currency/list
#### Request Example:
```
curl -v -X GET "http://localhost:8000/api/v1/currency/list"
```
#### Response Example:
```
{
    "items": [
        {
            "unique_id": "21e3a40e-9aac-40da-8e9b-3f178e610020",
            "dt_create": "2022-06-03T04:09:13.753041",
            "dt_update": "2022-06-03T04:09:13.753046",
            "name": "currency_1",
            "iso": "i1",
            "price": -8.0
        },
      ],
    "total": 1,
    "page": 1,
    "size": 50
}
```
### Get currencies prices history
GET: /api/v1/currency/history
#### Request Example:
```
curl -v -X GET "http://localhost:8000/api/v1/currency/history"
```
#### Response Example:
```
{
    "items": [
        {
            "unique_id": "21e3a40e-9aac-40da-8e9b-3f178e610020",
            "dt_create": "2022-06-03T04:09:13.753041",
            "dt_update": "2022-06-03T04:09:13.753046",
            "name": "currency_1",
            "iso": "i1",
            "price": -8.0
        },
      ],
    "total": 1,
    "page": 1,
    "size": 50
}
```
