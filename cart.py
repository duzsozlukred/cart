from bs4 import BeautifulSoup
import requests

def xss_scanner(url):
  """
  Verilen URL'yi tarar ve XSS açıklarını arar.

  Parametreler:
    url: Taranacak web sitesinin URL'si.

  Dönüş Değeri:
    Bulunan XSS açıklarının bir listesi.
  """

  # URL'yi BeautifulSoup ile ayrıştır
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  # Tüm linkleri bul
  links = soup.find_all("a")

  # Her linki tara
  xss_vulnerabilities = []
  for link in links:
    # Linkin href özelliğini al
    href = link.get("href")

    # XSS türlerini kontrol et
    if "javascript:" in href:
      xss_vulnerabilities.append("Reflected XSS")
    elif "<script>" in href:
      xss_vulnerabilities.append("Persistent XSS")

  return xss_vulnerabilities

# Kullanıcıdan URL girmesini iste
url = input("Taranacak web sitesinin URL'sini girin: ")

# XSS açıklarını tara
xss_vulnerabilities = xss_scanner(url)

# Sonuçları yazdır
if xss_vulnerabilities:
  print(f"Bulunan XSS açıkları: {xss_vulnerabilities}")
else:
  print("Herhangi bir XSS açığı bulunamadı.")
