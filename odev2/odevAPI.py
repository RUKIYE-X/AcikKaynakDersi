import requests

url = "https://emojihub.yurace.pro/api/random"

try:
    response = requests.get(url)
    response.raise_for_status()  # Bu satır, HTTP isteğiyle ilgili hataları kontrol eder.
    data = response.json()
    print(data)
except requests.exceptions.RequestException as error:
    print(f"Hata oluştu: {error}")
