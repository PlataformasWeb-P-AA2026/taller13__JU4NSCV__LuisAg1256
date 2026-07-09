# taller13

## Creación de Servicio Web y Consumo vía Flask

## Integrantes
- Juan Cueva 
- Luis Aguilar

### Revisar
- Ejemplo de servicios web con Django y Django-Rest [ejemplos]
- Ejemplo de consumo de servicios web desde flask [consumo-api]

### Ejemplos

* Usando requests (librería de python)

```

# GET
import requests
r = requests.get("http://127.0.0.1:8000/api/estudiantes/", auth=('user', 'passs'))
r.content

# POST
r = requests.post('http://127.0.0.1:8000/api/numerost/', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/12/', 'telefono':'99999999', 'tipo'='principal' }, auth=('user', 'pass'))
print(r)

# PUT
r = requests.put('http://127.0.0.1:8000/api/numerost/26', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/13/', 'telefono':'99999999', 'tipo':'principal' }, auth=('user', 'pass'))
print(r)

# DELETE
r = requests.delete('http://127.0.0.1:8000/api/numerost/26/', auth=('user', 'pass'))
print(r)
```


### Problemática

Dadas dos entidades:

* Edificio:
	* nombre
	* dirección
	* ciudad
	* tipo [residencial, comercial]

* Departamento
	* nombre completo del propietario
	* costo del departamento
	* número de cuartos
	* edificio

Nota: Un departamento pertenece a un edificio

### Tecnologías y herramientas:

- Base de datos Sqlite / Postgres (agregar en el readme, evidencias de las tablas en ambas BD)

Postgres informacion de departamentos y de edificios:
<img width="1920" height="1200" alt="cap1" src="https://github.com/user-attachments/assets/4ff2782b-182e-44dc-9d3c-23295af5adb6" />

<img width="1920" height="1200" alt="cap2" src="https://github.com/user-attachments/assets/55ab89e3-0193-4b8a-9060-ac5ddcbcfa9c" />

- Lenguaje Python
- Framework Django
- Django-Rest
- Flask


### Tarea a realizar:

- Crear un proyecto de Django.
- Crear una aplicación en el proyecto en Django.
- Generar el modelo de la aplicación usando las entidades descritas.
- Activar la interfaz de administración de la aplicación de Django.
- A través de views/template presentar un menú para listar en tablas: Edificios, Departamentos (usar el template adjunto)
- Agregar servicios web que permitan lista; crear; actualizar y eliminar entidades (todas deben tener acceso con token)
- Crear una aplicación en Flask que permita:
	-	Listar Edificios haciendo uso de los servicios web creados en el proyecto de Django
	- Listar Departamentos haciendo uso de los servicios web creados en el proyecto de Django.
	- Crear Edificios haciendo uso de los servicios web creados en el proyecto de Django.
	- Crear Departamentos haciendo uso de los servicios web creados en el proyecto de Django.
