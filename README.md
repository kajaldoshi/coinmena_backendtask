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
 <br><ul>docker-compose build</ul>
 <br><ul>docker-compose up -d</ul>
 <br><ul>docker-compose exec web python manage.py initadmin<br>
 <small>** This needs to be executed once for creating the admin user to access the API</small></ul>
</ul>

The API endpoints are accessible using the below:
<br><small>** Authentication is basic authentication using username and password, tested in POSTMAN client</small> 
<br><ul>GET http://127.0.0.1:8000/api/v1/quotes</ul>
<small>`GET /api/v1/quotes/ HTTP/1.1`<br>
`Host: 127.0.0.1:8000`<br>
`Authorization: Basic a2FqYWw6QzBpbm1lbkA=` </small>
<br><ul>POST http://127.0.0.1:8000/api/v1/quotes</ul>
<small>`POST /api/v1/quotes/ HTTP/1.1` <br>
`Host: 127.0.0.1:8000`<br>
`Authorization: Basic a2FqYWw6QzBpbm1lbkA=`
</small>

<br>The celery task `fetch_exchange_price` is scheduled to run every hour which will fetch the exchange rate and store in postgres DB

<br><br> The celery tasks can be monitored using flower UI  at below address:
http://0.0.0.0:5557  


 