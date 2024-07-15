import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Gerekli kütüphaneler
packages = ["colorama", "pyfiglet"]

for package in packages:
    try:
        install(package)
        print(f"{package} başarıyla yüklendi.")
    except subprocess.CalledProcessError:
        print(f"{package} yüklenirken bir hata oluştu.")

print("Tüm gerekli kütüphaneler yüklendi.")
