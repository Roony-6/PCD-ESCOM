import hashlib

with open("datos/revisiones_neumaticos.csv", "r", encoding="utf-8") as f:
    # Leemos el contenido una sola vez
    contenido = f.read()
    
    # Calculamos el hash una sola vez y lo guardamos en una variable
    hash_calculado = hashlib.sha256(contenido.encode("utf-8")).hexdigest()
    
    print(f"Hash calculado: {hash_calculado}")
    
    hash_esperado = "5e5b4e94488cf943acec8178956bdee6daccf97ae2bd569e0d12bc9cfad79ab4"
    
    if hash_calculado == hash_esperado:
        print("Los hash son iguales, SIUUUUUUU")
    else:
        print("No coinciden, revisa el archivo.")