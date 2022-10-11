from flask import render_template, redirect, request, session, flash
from inicio_sesion_app import app
from inicio_sesion_app.models.usuario import Users
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_register', methods=['POST'])
def registro():

    if not Users.validacion(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'email':request.form['email'],
        'password':pw_hash
    }
    usuario_id = Users.save(data)
    # guardamos el id del usuario registrado en la sesion para empezar a darle seguimiento
    session ['usuario_id'] = usuario_id
    return redirect ('/')

@app.route("/create_login", methods=['POST'])
def iniciar_login():
    usuario_loggeado = Users.validar_login(request.form)
    print(usuario_loggeado, 'QUE CONTIENES ESTO_')
    if not usuario_loggeado[0]:
        return redirect("/")
    # guardamos el id del usuario registrado en la sesion para empezar a darle seguimiento
    session['usuario_id'] = usuario_loggeado[1].id
    #return redirect('/')
    return redirect('/show/'+str(session['usuario_id']))

    
@app.route("/show/<int:id_usuario>")
def ver_usuario(id_usuario):  
        data={"id_usuario":id_usuario}
        id_usuario=Users.get_one(data) 
        print(id_usuario)
        return render_template("show.html",id_usuario=id_usuario)
    

@app.route('/logout')
def logout():
    if 'id_usuario' in session:
        del session['id_usuario']
    
    return redirect("/")




