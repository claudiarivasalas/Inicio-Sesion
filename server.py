from inicio_sesion_app import app
from inicio_sesion_app.controllers import usuarios
app.secret_key = "estessecreto"


if __name__=="__main__":
    app.run(debug=True)

