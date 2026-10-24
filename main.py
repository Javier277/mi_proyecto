import os
import psycopg

url = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(url) as connection:
        with connection.cursor() as cur:
            # Inserción parametrizada de Madrid
            cur.execute(
                "INSERT INTO viajes (destino, pais, fecha_inicio, fecha_fin, presupuesto) VALUES (%s, %s, %s, %s, %s)",
                ("Madrid", "España", "2026-12-01", "2026-12-08", 650.00)
            )
            
            # Consulta para mostrar todos los registros (incluyendo Madrid)
            cur.execute("SELECT * FROM viajes;")
            filas = cur.fetchall()

            for fila in filas:
                print(fila)

except Exception as e:
    print("Error:", e)
    raise