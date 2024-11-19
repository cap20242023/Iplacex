from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/notas', methods=['GET', 'POST'])
def notas():
    if request.method == 'POST':

        nota1 = float(request.form['n1'])
        nota2 = float(request.form['n2'])
        nota3 = float(request.form['n3'])


        promedio = (nota1+nota2+nota3)/3
        if (promedio >= 4):
          respuesta = 'Aprobado '
        else:
            respuesta = 'Reprobado '

        return render_template("notas.html",respuesta=respuesta, promedio=promedio)
    return render_template('notas.html')

@app.route('/nombres', methods=['GET', 'POST'])
def nombres():
    if request.method == 'POST':
        nombre1 = str(request.form['nom1'])
        nombre2 = str(request.form['nom2'])
        nombre3 = str(request.form['nom3'])


        return render_template("nombres.html", respuesta=respuesta,nombre=nombre)
    return render_template('nombres.html')

if __name__ == '__main__':
    app.run(debug=True)