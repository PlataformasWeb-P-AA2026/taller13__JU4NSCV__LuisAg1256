from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import json

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'una-clave-secreta-000001'

token = 'bb63f5e934b93043072ea191d3cdc52aec6404c7'
headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

@app.route("/")
def index():
    """
    """
    total_edificios = 0
    total_departamentos = 0

    try:
        r_edificios = requests.get(f"http://localhost:8000/api/edificios/", headers=headers)
        if r_edificios.status_code == 200:
            total_edificios = json.loads(r_edificios.content).get('count', 0)
            
        r_departamentos = requests.get(f"http://localhost:8000/api/departamentos/", headers=headers)
        if r_departamentos.status_code == 200:
            total_departamentos = json.loads(r_departamentos.content).get('count', 0)
    except:
        pass

    return render_template("index.html", 
                           total_edificios=total_edificios, 
                           total_departamentos=total_departamentos)


@app.route("/los/edificios")
def los_edificios():
    """
    """
    r = requests.get("http://localhost:8000/api/edificios/", headers=headers)
    print("---------------------")
    print(r.content)
    print("---------------------")
    edificios = json.loads(r.content)['results']

    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/los/departamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://localhost:8000/api/departamentos/", headers=headers)
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("losdepartamentos.html", departamentos=datos,
    numero_departamentos=numero)


@app.route("/crear/edificio", methods=['GET', 'POST'])
def crear_edificio():
    """
    """
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        tipo = request.form['tipo']

        # Datos a enviar a la API de Django
        edificio_data = {
            'nombre': nombre,
            'direccion': direccion,
            'ciudad': ciudad,
            'tipo': tipo
        }

        # Realizar la petición POST a la API de Django
        r = requests.post("http://localhost:8000/api/edificios/",
                              json=edificio_data,
                              headers=headers)

        print(f"Status Code (Crear Edificio): {r.status_code}")
        # Si todo fue bien (código 201 Created), la API devuelve el objeto creado
        nuevo_edificio = json.loads(r.content)
        flash(f"Edificio '{nuevo_edificio['nombre']}' creado exitosamente!", 'success')
        return redirect(url_for('los_edificios')) # Redirigir a la lista de edificios

    # Si es una petición GET o si hubo un error en POST, muestra el formulario
    return render_template("crear_edificio.html")


@app.route("/crear/departamento", methods=['GET', 'POST'])
def crear_departamento():

    edificios_disponibles = []

    r_edificios = requests.get("http://localhost:8000/api/edificios/", headers=headers)
    edificios_disponibles = json.loads(r_edificios.content)['results']

    if request.method == 'POST':
        nombre_propietario = request.form['nombre_propietario']
        costo = request.form['costo']
        num_cuartos = request.form['num_cuartos']

        edificio_url = request.form['edificio']

        departamento_data = {
            'nombre_propietario': nombre_propietario,
            'costo': costo,
            'num_cuartos': num_cuartos,
            'edificio': edificio_url # Enviamos la URL del edificio
        }

        r = requests.post("http://localhost:8000/api/departamentos/",
                              json=departamento_data,
                              headers=headers)

        print(f"Status Code (Crear Departamento): {r.status_code}")

        nuevo_departamento = json.loads(r.content)
        flash(f"Departamento '{nuevo_departamento['nombre_propietario']}' creado exitosamente!", 'success')
        return redirect(url_for('los_departamentos')) 

    return render_template("crear_departamento.html",
                           edificios=edificios_disponibles,
                           )


if __name__ == "__main__":
    app.run(debug=True)
