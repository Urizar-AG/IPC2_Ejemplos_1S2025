from flask import Flask, request, jsonify
from functools import wraps
import jwt
from datetime import datetime, timedelta

#Llave secreta para JWT
SECRET_KEY = 'ipc2-key-1234'

#Usuarios
usuarios = {
    'ipc2': {'password': 'pass123', 'role': 'usuario'},
    'admin': {'password': 'admin123', 'role': 'administrador'}
}

app = Flask(__name__)

#Validar token de autenticación
def autenticacion(f):
    @wraps(f) #Mantener metadata de la función
    def verificar_autenticacion(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            print('Sin token de autorización')
            return jsonify({'error': 'Token de autorización requerido'}), 401
        try: 
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user = data #usuario, tipo_usuario
        except Exception as e:
            print('Error al validar el token: ', e)
            return jsonify({'error': 'Algo salio mal al validar el Token'}), 401
        return f(*args, *kwargs) #Ejecuta la función original
    return verificar_autenticacion

#Verificar el tipo de usuario que accede
def tipo_usuario(role):
    def verificar_tipo_usuario(f):
        @wraps(f)
        def validar_tipo_usuario(*args, **kwargs):
            if request.user.get('role') != role:
                print('El usuario no está autorizado')
                return jsonify({'error': 'Permisos insuficientes para acceder'}), 403
            return f(*args, **kwargs)
        return validar_tipo_usuario
    return verificar_tipo_usuario

#Login de usuarios con JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('username')
    password = data.get('password')
    print(usuario)

    if usuario not in usuarios or usuarios[usuario]['password'] != password:
        return jsonify({'error': 'Credenciales invalidas'}), 401
    token = jwt.encode({
        'username': usuario,
        'role': usuarios[usuario]['role'],
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, SECRET_KEY, algorithm='HS256')

    return jsonify({'token': token})

#Ruta protegida
@app.route('/user', methods=['GET'])
@autenticacion
def get_data():
    return jsonify({'message': 'Bienvenido al laboratorio', 'user': request.user.get('username')})

#Ruta protegida y con restricción de rol
@app.route('/admin', methods=['GET'])
@autenticacion
@tipo_usuario('administrador')
def admin():
    return jsonify({'message': 'Bienvenido administrador'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)