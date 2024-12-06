import requests
from bs4 import BeautifulSoup

# ASCII Art sederhana
ascii_art = r"""

________  .__               __________                         _________                     
\______ \ |__|__________    \______   \_____     ____   ____  /   _____/ ____ _____    ____  
 |    |  \|  \____ \__  \    |     ___/\__  \   / ___\_/ __ \ \_____  \_/ ___\\__  \  /    \ 
 |    `   \  |  |_> > __ \_  |    |     / __ \_/ /_/  >  ___/ /        \  \___ / __ \|   |  \
/_______  /__|   __(____  /  |____|    (____  /\___  / \___  >_______  /\___  >____  /___|  /
        \/   |__|       \/                  \//_____/      \/        \/     \/     \/     \/ 

"""
print(ascii_art)

def scan_page(url):
    
    try:
        print(f"\nMenganalisis URL: {url}...")
        # Mengirim permintaan GET ke URL
        response = requests.get(url)
        response.raise_for_status()  # Menimbulkan error jika status tidak 200
        
        # Menyaring isi HTML menggunakan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Menampilkan informasi dasar tentang halaman
        print(f"\n[INFO] Status Kode: {response.status_code}")
        print(f"[INFO] Judul Halaman: {soup.title.string if soup.title else 'Tidak ada judul'}")
        print(f"[INFO] Deskripsi Halaman: {soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else 'Tidak ada deskripsi.'}")
        
        # Menampilkan semua link di halaman
        print("\n[INFO] Daftar Link yang Ditemukan:")
        links = soup.find_all('a', href=True)
        for idx, link in enumerate(links, 1):
            print(f"{idx}. {link['href']}")

        # Menampilkan semua gambar di halaman
        print("\n[INFO] Gambar yang Ditemukan:")
        images = soup.find_all('img', src=True)
        for idx, img in enumerate(images, 1):
            print(f"{idx}. {img['src']}")
  
        print("\n[INFO] Heading yang Ditemukan:")
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings = soup.find_all(tag)
            for idx, heading in enumerate(headings, 1):
                print(f"{tag.upper()} {idx}: {heading.get_text(strip=True)}")
        
    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] Terjadi kesalahan saat mengakses halaman: {e}")

url = input("\nURL YANG INGIN KAMU TUJU (Jangan lupa gunakan https): ")
scan_page(url)
