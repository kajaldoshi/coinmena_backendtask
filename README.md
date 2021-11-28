# Backend Task - CoinMena

Problem Statement: Write an API using Django that fetches the price of BTC/USD from the Alphavantage
API every hour, and stores it on postgres. This API must be secured which means that you will need an API key to use it.
<br> There should be two endpoints:<br>
`GET /api/v1/quotes` - returns the exchange rate <br>
`POST /api/v1/quotes` - which triggers force requesting the prices from alphavantage.
<br> The API and DB should be containerized using Docker as well.
<ul> Technologies to be used: Celery, Redis or RabbitMQ, Docker and Docker Compose</ul>


<b>Steps to setup the repository locally:</b>
<ul>Clone the git repository : https://github.com/kajaldoshi/coinmena_backendtask.git
</ul>

<ul>Execute the below docker-compose commands for deploying and starting up the containers
 <br><ul>- docker-compose build</ul>
 <br><ul>- docker-compose up -d</ul>
 <br><ul>- docker-compose exec web python manage.py initadmin<br>
 <small>** This needs to be executed once for creating the admin user to access the API</small></ul>
</ul>
<small> Note: During first time setup, postgres database setup may need time and web container will have errors as db connection is not established.<br>
In this scenario: Once the database setup is ready for accepting connections, spin up the containers again using below commands:
<br>1. docker-compose down
<br>2. docker-compose up -d 
</small><br><br>
The API endpoints are accessible using the below:
<br><ul>Get a token authentication using username and password before calling the below endpoints</ul>
<small>`POST /api-token-auth/ HTTP/1.1` <br>
`Host: 127.0.0.1:8000` <br>
`Content-Type: application/json` <br>
`Content-Length: 43` <br>
`{"username":"kajal", "password":"password"}`</small> <br>
<br><ul>GET http://127.0.0.1:8000/api/v1/quotes</ul>
<small>`GET /api/v1/quotes/ HTTP/1.1`<br>
`Host: 127.0.0.1:8000`<br>
`Authorization: Token 9799c607b2c6f7ccf6c3324f8beb5e1fb9216a97` </small><br>
<br><ul>POST http://127.0.0.1:8000/api/v1/quotes</ul>
<small>`POST /api/v1/quotes/ HTTP/1.1` <br>
`Host: 127.0.0.1:8000`<br>
`Authorization: Token 9799c607b2c6f7ccf6c3324f8beb5e1fb9216a97`
</small>

<br>The celery task `fetch_exchange_price` is scheduled to run every hour which will fetch the exchange rate and store in postgres DB

<br> The celery tasks can be monitored using flower UI  at below address:
http://0.0.0.0:5557

