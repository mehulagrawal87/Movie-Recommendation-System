import requests

url = "https://api.tmdb.org/3/movie/11?api_key=b6481393eb186a1e7c69e1af4562ad7b"

try:
    r = requests.get(url, timeout=10)
    print("Status:", r.status_code)
    print("Response preview:", r.text[:100])
except Exception as e:
    print("Failed:", e)


