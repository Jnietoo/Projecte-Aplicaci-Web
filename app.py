from flask import Flask, render_template, request, redirect, session, url_for
import db_module

app = Flask(__name__)
app.secret_key = 'mi_secreto_super_seguro' # Necesario para usar session

# --- RUTHAS PÚBLICAS ---

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    # Aquí va tu portafolio
    proyectos = [
        {"nombre": "Cálculo Edad 100", "desc": "Calculadora simple"},
        {"nombre": "Par/Impar", "desc": "Lógica matemática"},
        {"nombre": "Gestor Mails", "desc": "CRUD con Base de Datos"}
    ]
    return render_template("about.html", proyectos=proyectos)

# --- RUTAS DE AUTENTICACIÓN ---

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['usuario']
        pwd = request.form['password']
        email = request.form['email']
        if db_module.registrar_usuario(user, pwd, email):
            return redirect(url_for('login'))
        else:
            return render_template("register.html", error="El usuario ya existe")
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        pwd = request.form['password']
        datos_usuario = db_module.verificar_usuario(user, pwd)
        
        if datos_usuario:
            session['user_id'] = datos_usuario[0]
            session['username'] = datos_usuario[1]
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos")
            
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

# --- RUTAS PRIVADAS (Solo si estás logueado) ---

@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    lista_torneos = db_module.obtener_torneos()
    return render_template("dashboard.html", torneos=lista_torneos)

@app.route("/nuevo_torneo", methods=['GET', 'POST'])
def nuevo_torneo():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        juego = request.form['juego']
        premio = request.form['premio']
        fecha = request.form['fecha']
        db_module.crear_torneo(nombre, juego, premio, fecha)
        return redirect(url_for('dashboard'))
        
    return render_template("nuevo_torneo.html")

if __name__ == "__main__":
    app.run(debug=True)