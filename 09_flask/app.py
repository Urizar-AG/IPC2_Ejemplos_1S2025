#Comando para instalar Flask -> pip install flask
#Comando para instalar CORS -> pip install flask_cors
#jsonify es para serializar los datos en format JSON

#Importar librerias
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from estudiante import Estudiante

#Intanciar la clase Flask y habilitar CORS
app = Flask(__name__)
CORS(app)

estudiantes = []

#Endpoint -> Si no se especifica 'methods' por default es tipo GET
#http://direccion_host:port/ ó http://direccion_host:port
@app.route('/')
def index():
    return "Hola, IPC2"


#Endpoint -> GET: Devuelve la lista de todos los estudiante registrados
#http://host:port/api/estudiantes
@app.route('/api/estudiantes', methods=['GET'])
def get_estudiantes():
    return jsonify({'estudiantes': [estudiante.get_info() for estudiante in estudiantes]}), 200


#Endpoint -> GET con Query Params: Obtener un estudiante específico por medio del carnet
#http://host:port/api/estudiantes/obtener?carnet=123456789
@app.route('/api/estudiante/obtener', methods=['GET'])
def get_estudiante():
    carnet = int(request.args.get('carnet')) #Obtener el carnet enviado a la API
    
    for estudiante in estudiantes:
        if estudiante.get_carnet() == carnet:
            return jsonify(estudiante.get_info()), 200

    return jsonify({'error': f'No existe un estudiante con el carnet {carnet}'}), 400
        

#Endpoint -> POST: Registrar un nuevo estudiante en el sistema
#http://host:port/api/estudiantes/registrar
@app.route('/api/estudiante/registrar', methods=['POST'])
def registrar_estudiante():
    data = request.get_json() #Recuperar información envíada

    for estudiante in estudiantes:
        if estudiante.get_carnet() == int(data['carnet']):
            return jsonify({'error': 'El carnet ingresado ya está asociado a un estudiante'}), 400
    
    estudiantes.append(Estudiante(int(data['carnet']), data['nombre'], data['correo']))
    return jsonify({'msg': 'Estudiante registrado correctamente'}), 200


#Endpoint -> PUT: Actualizar información del estudiante  en el sistema
#<int:param>
#<float:param>
#<str:param> 
#Si no se específica el tipo <carnet> por default el dato es un string
@app.route('/api/estudiante/actualizar/<int:carnet>', methods=['PUT'])
def acutilizar_estudiante(carnet):
    data = request.get_json()

    for estudiante in estudiantes:
        if estudiante.get_carnet() == carnet:
            estudiante.set_nombre(data.get('nombre'))
            estudiante.set_correo(data.get('correo'))
            return jsonify({'msg': 'Estudiante actualizado correctamente'}), 200
    
    return jsonify({'error': f'No existe un estudiante con el carnet {carnet}'}), 400


#Endpoint -> DELETE: Elimina un estudiante según el número de carnet
#http://direccion_host/eliminar?carnet=123456789
@app.route('/api/estudiante/eliminar', methods=['DELETE'])
def eliminar_estudiante():
    carnet = int(request.args.get('carnet'))
    
    aux = 0
    for estudiante in estudiantes:
        if estudiante.get_carnet() == carnet:
            del estudiantes[aux]
            return jsonify({'msg': 'Estudiante eliminado correctamente'}), 200
        aux += 1
    
    return jsonify({'error': f'No existe un estudiante con el carnet {carnet}'}), 400


#Ver en el navegador
@app.route('/inicio')
def inicio():
    return render_template('index.html')

#Ver en el navegador
@app.route('/estudiantes')
def mostrar_estudiantes():
    return render_template('estudiantes.html', estudiantes=estudiantes)



if __name__ == '__main__':
    #app.run() -> Corregir la aplicación configuraciones por default
    #host='0.0.0.0' -> hace disponible la aplicación para cualquier IP
    #debug=True -> Modo depuración en FLask, muestra mensajes detallados y actualiza la aplicación automáticmamente al modificar código
    app.run(host='0.0.0.0', port=5000,  debug=True)
