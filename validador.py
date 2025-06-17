def validar_ip(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        num = int(parte)
        if num < 0 or num > 255:
            return False
        # Evitar ceros a la izquierda (excepto '0')
        if parte != str(num):
            return False
    return True

# Ejemplo de uso
if __name__ == "__main__":
    ip = input("Introduce una dirección IP: ")
    if validar_ip(ip):
        print("IP válida")
    else:
        print("IP no válida")