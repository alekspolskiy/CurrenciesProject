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
