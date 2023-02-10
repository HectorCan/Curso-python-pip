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

with Docker:
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

# Conda Commands

Listar entornos

```sh
conda env list
```

Crear entorno

```sh
conda create --name py35 python=3.5 pandas
```

Activar entorno

```sh
conda activate py35
```

Desactivar entorno

```sh
conda deactivate
```

Listar dependencias

```sh
conda list
conda list pandas
```

Actualizar dependencia

```sh
conda update pandas
```

Instalar dependencia

```sh
conda install python=3.9 pandas=1.2
```

Remover dependencia

```sh
conda remove pandas
```

Remover entorno (tienes que salir de el)

```sh
conda env remove --name py35
```

Instalar paquetes de otro canal

```sh
conda install --chanel CHANNEL PACKAGE
```

Una mejor optimizacion de conda es mamba, usualmente todos los comandos de conda estan disponibles, ya que
realiza los procesos en paralelo

```sh
mamba env export --history
```