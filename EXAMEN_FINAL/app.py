from flask import Flask, render_template, request

app = Flask(__name__)


# PÁGINA PRINCIPAL
@app.route('/')
def index():
    return render_template('index.html')


# EJERCICIO 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])
        precio_unitario = 9000
        total_sin_descuento = cantidad_tarros * precio_unitario

        # CALCULO DE LOS DESCUENTOS
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('formulario1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento)

    return render_template('formulario1.html', total_sin_descuento=None)


# SEGUNDO EJERCICIO
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    # DICCIONARIO CON LOS USUARIOS PREDETERMINADOS
    usuarios = {'juan': 'admin', 'pepe': 'user'}

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # VERIFICACION DE LOS USURARIOS Y SUS CONTRASEÑAS
        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f'Bienvenido {"administrador" if usuario == "juan" else "usuario"} {usuario}'
            return render_template('formulario2.html', mensaje=mensaje)
        else:
            mensaje = 'Usuario o contraseña incorrectos'
            return render_template('formulario2.html', mensaje=mensaje)

    return render_template('formulario2.html', mensaje=None)


if __name__ == '__main__':
    app.run(debug=True)
