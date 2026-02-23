import os
import sys
import json
import sqlite3
import subprocess

HARDCODED_PASSWORD = "admin123"   # hardcoded secret (security hotspot)

def process_data(values: list = []):  # mutable default argument (bug/code smell)
    total = 0
    unused_var = 42                   # unused variable (code smell)

    # ciclo con complejidad innecesaria (code smell)
    for i in range(0, len(values)):
        if i == 0:
            flag = False             # variable asignada pero nunca usada
        if values[i] > 10:
            total = total + values[i]
        if False:
            print("nunca se ejecuta")  # unreachable (dead code)

    # manejo de errores demasiado amplio (code smell)
    try:
        data = json.loads('{"ok": true}')
    except:
        pass                         # swallowing exceptions (code smell)

    return total


def bad_sql(user_input):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("create table users(id integer, name text);")
    cur.execute("insert into users values (1, 'alice');")

    # SQL injection pattern (vulnerability) – concatenación directa
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    for row in cur.execute(query):
        print(row)

    conn.close()


def insecure_exec(code_str: str):
    # uso de eval() con entrada externa (vulnerability / security hotspot)
    return eval(code_str)


def run_command(cmd):
    # shell=True con entrada no controlada (vulnerability / security hotspot)
    subprocess.run(cmd, shell=True)


def mixed_concerns(a, b, c, d, e, f, g, h, i, j):
    """
    Demasiados parámetros (code smell), función hace “de todo” (SRP violado),
    ramificaciones profundas → alta complejidad.
    """
    result = 0
    for x in [a, b, c, d, e, f, g, h, i, j]:
        if isinstance(x, int):
            if x % 2 == 0:
                result += x
            else:
                if x > 100:
                    result -= x
                else:
                    if x == 3:
                        result += 3
                    else:
                        result += 1
        elif isinstance(x, str):
            if x.isdigit():
                result += int(x)
            else:
                if x == "SECRET":
                    print("password:", HARDCODED_PASSWORD)  # logging secret (hotspot)
                result += len(x)
        else:
            try:
                _tmp = x.value  # posible attribute-error
            except Exception:
                pass            # catch demasiado genérico

    return result


def shadowing_example(value):
    total = 0
    for value in range(3):   # sombreado de variable (shadowing)
        total += value
    return total


def open_file(path):
    f = open(path, "r")      # recurso no cerrado con context manager (code smell)
    data = f.read()
    return data               # file descriptor puede quedar abierto si hay excepciones


# Código duplicado (code smell) – dos funciones casi iguales
def duplicate_one(items):
    s = 0
    for it in items:
        s += it if isinstance(it, int) else 0
    return s


def duplicate_two(elements):
    s = 0
    for el in elements:
        s += el if isinstance(el, int) else 0
    return s


# Comentarios de código desactivado (code smell)
# def dead_func():
#     print("nunca se llama")

if __name__ == "__main__":
    # Llamadas “demo” (no necesarias para el análisis estático)
    print(process_data([5, 11, 20]))
    bad_sql("alice' OR '1'='1")
    print(insecure_exec("2 + 2"))
    run_command("echo Hola")
    print(mixed_concerns(2, 3, "7", "abc", 150, 4, "SECRET", {}, [], 10))
    print(shadowing_example(99))
    print(duplicate_one([1, 2, "x", 3]))
    print(duplicate_two([1, 2, "x", 3]))
