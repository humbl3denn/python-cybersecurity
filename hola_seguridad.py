# Mi primer script de ciberseguridad
ip_sospechosa = "192.168.1.50"
intentos_fallidos = 7

print("Analizando IP: ", ip_sospechosa)

if(intentos_fallidos > 5):
    print("ALERTA: posible ataque de fuerza bruta")
else:
    print("Actividad normal")

# Ejecutar en terminal con la instruccion: python hola_seguridad.py