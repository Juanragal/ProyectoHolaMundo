import hashlib
def obtener_hash(password):
    encoded=password.encode()
    resumen=hashlib.sha256(encoded)
    return resumen.hexdigest()


candidatas = ["baseball","football","shadow","mustang","superman","jordan","soccer"]
password_secreta = "136c67657614311f32238751044a0a3c0294f2a521e573afa8e496992d3786ba"

for x in candidatas:
    if obtener_hash(x) == password_secreta:
        print("la contraseña es",x)
        break
else:
    print("La contraseña no es ninguna de las indicadas")
