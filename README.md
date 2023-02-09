# Game Project

To play the game you must follow the instructions:

```sh
cd game
python3 main.py 
```

# App Project

To use the app follow the instructions:

```sh
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

How to do it on docker:

```sh
# to build
docker-compose build

# to check resources

docker-compose ps

# to run
docker-compose up

# to access
docker-compose exec app-csv bash
```

# Web-Server Project

Follow the instructions:

```sh
cd web-server
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```