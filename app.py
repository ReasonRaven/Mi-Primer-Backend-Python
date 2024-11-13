from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

usuario = {
    'email': 'jonathan23_09@outlook.com',
    'password': 'batman2006'
}


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/misProyectos')
def misProyectos():
    return render_template('misProyectos.html')
@app.route('/pagina')
def pagina():
    return render_template('mi_Pagina_WEB.html')
@app.route('/koala')
def koala():
    return render_template('scanerKoala.html')
@app.route('/reporteVR')
def reporte():
    return render_template('reporte.html')
@app.route('/frameworks')
def frameworks():
    return render_template('frameworks.html')
@app.route('/stackoverflow')
def stackoverflow():
    return render_template('stackOverflow.html')
@app.route('/success', methods=['POST'])
def success():
    email = request.form['email']
    password = request.form['password']
    print(email,password)
    if email == usuario['email'] and password == usuario['password']:
        return render_template('success.html')
    else:
        print('Vete')
        return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True)
