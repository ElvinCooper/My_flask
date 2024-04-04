from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = " mi super clave secreta jajaja"

# creando la clase formulario
class formulario(FlaskForm):
    name = StringField(' ¿ Cual es tu nombre ?' , validators=[DataRequired()])
    submit = SubmitField("Submit")

# ruta raiz
@app.route('/')
def home():
    return render_template ('base.html')

# localhost:5000/user  
@app.route('/index.html')
def user():
    return render_template  ('index.html' )
    #return '<h1>Hola {}  </h1>'.format(name)


# URL Invalida    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Error interno del servidor
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/nombre', methods=['GET', 'POST'])
def nombre ():
    nombre = None
    my_form = formulario()
    # validacion del formulario
    if my_form.validate_on_submit():
        nombre = my_form.name.data
        my_form.name.data = ' '

    return render_template ('nombre.html',
                             v_nombre = nombre,
                             vform = my_form)

if app == '__main__':
    app.run(debug=True)

