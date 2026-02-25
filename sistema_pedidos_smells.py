# sistema_pedidos.py
# Código funcional con problemas reales 

import os

class PedidoManager:

    def __init__(self):
        self.pedidos = []
        self.total_ventas = 0.0
        self.descuento_global = 0.05
        self.log = []   # 

    def procesar_pedido(self, cliente, productos, tipo_cliente, direccion, email):
        # 
        if cliente == "":
            cliente = "Anonimo"

        if productos is None:
            productos = []

        total = 0.0

        # 
        for p in productos:
            precio = p.get("precio", 0)
            cantidad = p.get("cantidad", 1)

            if precio >= 0:
                if cantidad > 0:
                    total = total + (precio * cantidad)
                else:
                    total = total + precio
            else:
                total = total + 0  # 

        # 
        if tipo_cliente == "VIP":
            total = total - (total * 0.15)
        elif tipo_cliente == "NORMAL":
            total = total - (total * self.descuento_global)
        elif tipo_cliente == "EMPRESA":
            total = total - (total * 0.1)
        else:
            total = total

        # 
        self._enviar_correo(email, cliente, total)
        self._registrar_envio(direccion, cliente)

        # 
        self.total_ventas += total

        pedido = {
            "cliente": cliente,
            "productos": productos,
            "total": total,
            "direccion": direccion,
            "email": email,
            "tipo": tipo_cliente
        }

        self.pedidos.append(pedido)

        # 
        self.log.append("Pedido procesado")

        return total

    def _enviar_correo(self, email, cliente, total):
        # 
        print(f"Correo enviado a {email} para {cliente} por ${total}")

    def _registrar_envio(self, direccion, cliente):
        print(f"Pedido de {cliente} enviado a {direccion}")

    def reporte_general(self):
        print("===== REPORTE GENERAL =====")
        print("Total ventas:", self.total_ventas)
        print("Número de pedidos:", len(self.pedidos))

        for p in self.pedidos:
            self._imprimir_pedido(p)

        # 
        if self.total_ventas > 50000:
            print("Estado: Buen rendimiento")
        else:
            print("Estado: Rendimiento medio")

        self.log.append("Reporte generado")

    def _imprimir_pedido(self, pedido):
        print("---------------------------")
        print("Cliente:", pedido["cliente"])
        print("Tipo:", pedido["tipo"])
        print("Total:", pedido["total"])
        print("Email:", pedido["email"])
        print("Dirección:", pedido["direccion"])

    def exportar_reporte(self, formato="csv"):
        # 
        if formato == "csv":
            archivo = open("reporte.csv", "w")
            archivo.write("cliente,total,email\n")
            for p in self.pedidos:
                archivo.write(f"{p['cliente']},{p['total']},{p['email']}\n")
            archivo.close()
        elif formato == "txt":
            archivo = open("reporte.txt", "w")
            for p in self.pedidos:
                archivo.write(f"{p['cliente']} - {p['total']}\n")
            archivo.close()
        else:
            print("Formato no soportado")


# ===== USO DEL SISTEMA =====

manager = PedidoManager()

productos = [
    {"nombre": "Laptop", "precio": 3000, "cantidad": 1},
    {"nombre": "Mouse", "precio": 50, "cantidad": 2},
    {"nombre": "Teclado", "precio": 100, "cantidad": 1}
]

total1 = manager.procesar_pedido(
    cliente="Juan",
    productos=productos,
    tipo_cliente="VIP",
    direccion="Calle 123",
    email="juan@email.com"
)

total2 = manager.procesar_pedido(
    cliente="EmpresaX",
    productos=productos,
    tipo_cliente="EMPRESA",
    direccion="Zona Industrial",
    email="contacto@empresax.com"
)

manager.reporte_general()
manager.exportar_reporte("csv")