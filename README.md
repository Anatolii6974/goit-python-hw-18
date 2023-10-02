HomeWork 08

Part 1
poetry new hw8nosql
cd hw8nosql
poetry install
https://account.mongodb.com/account/login
mongodb+srv://anatolii:<password>@cluster0.wgxobak.mongodb.net/?retryWrites=true&w=majority

-- Create models and download json --
poetry add pymongo mongoengine
poetry run py load_json.py

-- Search for quotes by tag, by author's name, or by a set of tags --
poetry run py search_quotes.py
Accepts commands from the offensive format - command: value

Example: 
    name: Steve Martin
	tag:life
	tags:life,live
	exit

Part 2	
docker run -it --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
http://localhost:15672/
poetry add pika
cd rabbitmq-hw
models_rmq.py
poetry run producer.py
poetry run concumer.py





