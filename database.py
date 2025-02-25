import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Crear una conexión a la base de datos SQLite especificada por db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conexión establecida a la base de datos SQLite: {db_file}")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return conn

def create_table(conn, create_table_sql):
    """Crear una tabla desde la sentencia create_table_sql"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(f"Error al crear la tabla: {e}")

def initialize_database():
    database = "billguard.db"

    sql_create_usuarios_table = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        contraseña_hash TEXT NOT NULL,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """

    sql_create_suscripciones_table = """
    CREATE TABLE IF NOT EXISTS suscripciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        nombre_servicio TEXT NOT NULL,
        costo_mensual REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_renovacion DATE NOT NULL,
        estado TEXT NOT NULL,
        metodo_pago_id INTEGER NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
        FOREIGN KEY (metodo_pago_id) REFERENCES metodos_pago (id)
    );
    """

    sql_create_metodos_pago_table = """
    CREATE TABLE IF NOT EXISTS metodos_pago (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        tipo TEXT NOT NULL,
        numero TEXT NOT NULL,
        fecha_vencimiento DATE NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    );
    """

    sql_create_historial_pagos_table = """
    CREATE TABLE IF NOT EXISTS historial_pagos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        suscripcion_id INTEGER NOT NULL,
        monto REAL NOT NULL,
        fecha_pago DATETIME DEFAULT CURRENT_TIMESTAMP,
        metodo_pago_id INTEGER NOT NULL,
        FOREIGN KEY (suscripcion_id) REFERENCES suscripciones (id),
        FOREIGN KEY (metodo_pago_id) REFERENCES metodos_pago (id)
    );
    """

    sql_create_notificaciones_table = """
    CREATE TABLE IF NOT EXISTS notificaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        mensaje TEXT NOT NULL,
        fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
        leido BOOLEAN NOT NULL CHECK (leido IN (0, 1)),
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    );
    """

    # Crear una conexión a la base de datos
    conn = create_connection(database)

    # Crear las tablas
    if conn is not None:
        create_table(conn, sql_create_usuarios_table)
        create_table(conn, sql_create_suscripciones_table)
        create_table(conn, sql_create_metodos_pago_table)
        create_table(conn, sql_create_historial_pagos_table)
        create_table(conn, sql_create_notificaciones_table)
    else:
        print("Error! No se pudo crear la conexión a la base de datos.")

if __name__ == "__main__":
    initialize_database()