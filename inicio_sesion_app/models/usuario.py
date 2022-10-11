from inicio_sesion_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from inicio_sesion_app import app
import re
from flask_bcrypt import Bcrypt

Bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$')


class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.fname = data['first_name']
        self.lname= data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('schema_login').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        get_usuario = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for usuarios in results:
            get_usuario.append( cls(usuarios) )
        return get_usuario

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuario WHERE id = %(id_usuario)s;"
        result = connectToMySQL('schema_login').query_db(query,data)
        return cls(result[0])


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuario ( first_name, last_name , email , password, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , %(password)s, NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('schema_login').query_db( query, data )

    @classmethod
    def obtener_email(cls, data):
        solicitud = "SELECT * FROM usuario WHERE email = %(email)s;"
        resultado = connectToMySQL('schema_login').query_db(solicitud, data)
        print(resultado, 'QUE CONTIENES ESTO_')
        #validar si el resultado contiene algo
        if len(resultado) < 1 or resultado == False:
            return False
        return cls(resultado[0])

    @staticmethod
    def validacion(user):
        is_valid = True # asumimos que esto es true
        if len(user['fname']) < 3:
            flash("Name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user['lname']) < 3:
            flash("Last name must be at least 3 characters.", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'register')
            is_valid = False
        if len(user['password']) < 6:
            flash("password must be at least 6 characters.", 'register')
            is_valid = False
        return is_valid

    @staticmethod
    def validar_login(formulario_login):
        is_valid = True
        obtener_usuario = Users.obtener_email(formulario_login)
        print(obtener_usuario, "Obtener Us validar login")
        if not obtener_usuario:
            is_valid = False
            flash("Correo electronico no existe!", "login")   
        elif not Bcrypt.check_password_hash(obtener_usuario.password, formulario_login['password']):
            # si obtenemos False después de verificar la contraseña
            is_valid = False
            flash("Invalid Email/Password")
            
        #session['user_id'] = obtener_usuario.id
        return is_valid, obtener_usuario


    

