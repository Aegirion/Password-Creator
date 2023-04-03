import random
import string

while True:

    def gen_password(uzunluk):

        karakterler = string.ascii_letters + string.digits

        passwrd="".join(random.choice(karakterler)for i in range (uzunluk))

        return passwrd

    uzunluk = int(input("Şifre uzunluğunu giriniz:"))

    passwrd = gen_password(uzunluk)
    print("Oluşturulan Şifre:",passwrd)