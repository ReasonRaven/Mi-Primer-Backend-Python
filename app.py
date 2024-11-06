from flask import Flask, render_template


app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
