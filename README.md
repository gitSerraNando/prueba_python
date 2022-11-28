# Inicialización de la Prueba 

* Se utilizó la tecnología de  [poetry](https://python-poetry.org/docs/) para la creación del entorno

* En la carpeta raíz del proyecto se utiliza el comando ``` poetry shell ``` para inicializar la activación del entorno
 ![poetry shell](/assets/img/poetry_shell.png "poetry shell")


* Para la instalación de dependencias ejecutamos ``` poetry install ``` 
 ![poetry install](/assets/img/poetry_install.png "poetry install")


* Luego de esto se ejecutamos  ``` uvicorn main:app --reload  ``` 
 y podemos acceder a la url de la documentacion

 http://127.0.0.1:8000/docs#/ 

 # Heroku url
 https://testpython.herokuapp.com/docs#/