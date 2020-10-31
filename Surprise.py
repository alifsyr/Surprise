import urllib.request
def verifikasi(nama):
    if(nama == "Fara" or nama == "Fathiya" or nama == "Fathiya Shafira" or nama == "Shafira" or nama == "fara" or nama == "fathiya" or nama == "fathiya shafira" or nama == "shafira"):
        print("Hai,",nama,". kamu cantik banget hari ini 💕.")
        pertanyaan(input("Kamu pacarnya aladdin yang ganteng dan lucu itu bukan sih ? (iya/bukan) :"))

    else:
        print("Aku tidak mengenal",nama,)
        Exit (input("Apakah kamu mau keluar ? (y/n) : "))

def pertanyaan(jawaban):
    if (jawaban == "iya" or jawaban == "Iya"):
        print ("Cieeeeee💖💖💖, dia nitip salam loh. Katanya I LOVE UUUUUU 🤞")
        jadian(input("Coba aku tes, kapan kalian jadian ? (DD/MM/YYYY) : "))
    else:
        print ("YAHH aku dibuat untuk pacarnya aladdin :(")
        jujur = input("Sekali lagi aku tanya, Kamu pacarnya aladdin AKA bang alif bukan ? (iya/bukan) : ")
        if (jujur =="iya" or jujur == "Iya" ):
            jadian((input("Coba aku tes, kapan kalian jadian ? (DD/MM/YYYY) : ")))
        else:
            exit()

def jadian(tanggal):
    if (tanggal == "30/08/2019"):
        kejutan(input("Kamu mau liat surprisenya ? (iya/tidak) :"))
    else:
        print("YAHH, kamu salah tanggal. aladdin bisa marah nih kalau tau")
        jadian((input("Coba inget-inget lagi, kapan kalian jadian ? (contoh : 01/01/2001) : ")))

def kejutan(answers):
    if (answers == "iya" or answers == "Iya"):
        url = ("https://i.ibb.co/27jFQJB/FARA.png")
        file_path = 'assets/kejutan/'
        file_name = 'Untuk pacarnya Aladdin'
        dl_img(url,file_path,file_name)
        Exit (input("Apakah kamu mau keluar ? (y/n) : "))
    else:
        kepastian = input("Sekali lagi aku tanya, Kamu mau tau surprisenya ? (iya/tidak) : ")
        if (kepastian =="iya" or kepastian == "Iya" ):
            url = ("https://i.ibb.co/27jFQJB/FARA.png")
            file_path = 'assets/kejutan/'
            file_name = 'Untuk pacarnya Aladdin'
            dl_img(url,file_path,file_name)
            Exit (input("Apakah kamu mau keluar ? (y/n) : "))
        else:
            exit()

def dl_img(url,file_path,file_name):
    full_path = file_path + file_name + '.png'
    urllib.request.urlretrieve(url,full_path)
    print("Sekarang kamu klik folder assets, lalu kamu klik folder kejutan 👍")

def Exit(x):
    if (x == "y" or x == "N"):
        exit()
    elif (x == "n" or x == "N"):
        verifikasi(input("Halo, dengan siapa ni ??? : ").capitalize())
    else:
        exit()

print("Halo👋 aku Jarvis")
verifikasi(input("Kalau kamu siapa ni ??? : ").capitalize())


