from flask import Flask, render_template, request, redirect, session, url_for
import db_module  # Importamos el archivo de funciones de base de datos

app = Flask(__name__)

# IMPORTANTE: Necesario para que funcionen las sesiones (login/logout)
# Cambia esto por cualquier texto aleatorio
app.secret_key = 'clave_secreta_esports_futbol_2024'

# --- RUTAS PÚBLICAS (Cualquiera puede verlas) ---

@app.route("/")
def home():
    # Pasa el usuario de la sesión a la plantilla para saber si mostrar "Login" o "Logout"
    return render_template("home.html")

@app.route("/about")
def about():
    # Requisito: Portafolio de proyectos hechos en clase
    mis_proyectos = [
        {"nombre": "Cálculo Edad 100", "desc": "Formulario simple con lógica matemática."},
        {"nombre": "Gestor de Mails", "desc": "Aplicación CRUD conectada a MySQL."},
        {"nombre": "FutbolEsports League", "desc": "Plataforma completa con Login y gestión de torneos."}
    ]
    return render_template("about.html", proyectos=mis_proyectos)

# --- RUTAS DE REGISTRO Y LOGIN ---

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Recogemos datos del formulario HTML
        user = request.form['usuario']
        pwd = request.form['password']
        email = request.form['email']
        
        # Intentamos guardar en BD
        if db_module.registrar_usuario(user, pwd, email):
            # Si sale bien, le mandamos al login
            return redirect(url_for('login'))
        else:
            # Si sale mal (ej: usuario repetido), mostramos error
            return render_template("register.html", error="Error: El nombre de usuario ya existe.")
            
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        pwd = request.form['password']
        
        # Verificamos si existe en la BD
        datos_usuario = db_module.verificar_usuario(user, pwd)
        
        if datos_usuario:
            # ¡Login correcto! Guardamos datos en la "mochila" (session)
            session['user_id'] = datos_usuario[0]  # El ID
            session['username'] = datos_usuario[1] # El nombre
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos.")
            
    return render_template("login.html")

@app.route("/logout")
def logout():
    # Borramos los datos de la sesión (cerrar sesión)
    session.clear()
    return redirect(url_for('home'))

# --- RUTAS PRIVADAS (Solo si estás logueado) ---

@app.route("/dashboard")
def dashboard():
    # PROTECCIÓN: Si no hay usuario en la sesión, fuera
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Obtenemos la lista de torneos de la BD
    lista_torneos = db_module.obtener_torneos()
    
    return render_template("dashboard.html", torneos=lista_torneos)

@app.route("/nuevo_torneo", methods=['GET', 'POST'])
def nuevo_torneo():
    # PROTECCIÓN
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Recogemos los datos del 3er formulario
        nombre = request.form['nombre']
        juego = request.form['juego']
        premio = request.form['premio']
        fecha = request.form['fecha']
        
        # Guardamos en BD
        db_module.crear_torneo(nombre, juego, premio, fecha)
        
        return redirect(url_for('dashboard'))
        
    return render_template("nuevo_torneo.html")

if __name__ == "__main__":
    app.run(debug=True)