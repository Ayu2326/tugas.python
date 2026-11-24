password = ""

while password != "123456":
    password = input("masukkan password : ")
    
    if password != "123456":
        print("password salah, Silahkan coba lagi")
    else:
        print("password benar")    
    
print("login berhasil")