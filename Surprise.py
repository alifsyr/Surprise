nama = input("Halo, dengan siapa ni ??? : ").lower()
correct = False

while (not correct):
    if (nama == "fara" or "fathiya" or "fathiya shafira" or "shafira"):
        print("Hai, ",nama,". kamu cantik banget hari ini 💕.")
        correct = True
    else:
        print("Kami tidak mengenal ",nama,". silahkan masukan kembali nama kamu :)")