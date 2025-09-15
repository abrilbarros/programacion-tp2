import cancion

print("====== Ejercicio 2 ======")
cancion_1 = cancion.Cancion("From Eden", 200, "indie folk")
cancion_2 = cancion.Cancion("The Perfect Girl", 189, "darkwave")
cancion_3 = cancion.Cancion("Pretty Girl", 180, "bedroom pop")

print("====== Ejercicio 3 ======")

print(cancion_1.obtener_genero())
print(cancion_2.obtener_genero())
print(cancion_3.obtener_genero())


print("====== Ejercicio 4 ======")

# Cambio de género de la 2da canción
cancion_2.establecer_genero("post-punk")

# Muestro el género actualizado
print(cancion_2.obtener_genero())