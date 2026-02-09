import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="practica5"
    )

# --- Funciones de Usuario ---
def registrar_usuario(usuario, password, email):
    conn = conectar()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO usuarios_futbol (usuario, password, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (usuario, password, email))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def verificar_usuario(usuario, password):
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT id, usuario FROM usuarios_futbol WHERE usuario = %s AND password = %s"
    cursor.execute(sql, (usuario, password))
    user = cursor.fetchone()
    conn.close()
    return user # Devuelve (id, nombre) o None

# --- Funciones de Contenido (Torneos) ---
def obtener_torneos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM torneos")
    datos = cursor.fetchall()
    conn.close()
    return datos

def crear_torneo(nombre, juego, premio, fecha):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO torneos (nombre, juego, premio, fecha) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, juego, premio, fecha))
    conn.commit()
    conn.close()