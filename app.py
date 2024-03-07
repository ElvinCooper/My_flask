from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    mi_nombre = 'Andrew Elias Cooper Castro'
    favorite_colors = ['rojo', 'verde', 'amarillo','purpura',23,224]
    return render_template ('index.html', 
                            hijo=mi_nombre,
                              colores = favorite_colors)

# localhost:5000/user  
@app.route('/<name>')

def user():
    return render_template  ('login.html' )
    #return '<h1>Hola {}  </h1>'.format(name)


# URL Invalida    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Error interno del servidor
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




if app == '__main__':
    app.run(debug=True)

