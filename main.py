import os
import requests

def enable_vpn(proxy_host='186.137.21.165', proxy_port=6881):
    """Включение HTTP/HTTPS прокси через переменные окружения"""
    # Для HTTP прокси используется http://, а не socks5
    os.environ['HTTP_PROXY'] = f'http://{proxy_host}:{proxy_port}'
    os.environ['HTTPS_PROXY'] = f'http://{proxy_host}:{proxy_port}'
    print(f"✅ VPN включен (HTTP прокси {proxy_host}:{proxy_port})")

def disable_vpn():
    os.environ.pop('HTTP_PROXY', None)
    os.environ.pop('HTTPS_PROXY', None)
    print("✅ VPN отключен")

def run_request():
    try:
        response = requests.get('https://httpbin.org/ip', timeout=60)
        print(f"IP: {response.json()['origin']}")
        return response.json()['origin']
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


print("Без VPN:")
ip1 = run_request()

print("\nВключаем VPN...")
enable_vpn()
print("С VPN:")
ip2 = run_request()

print("\nВыключаем VPN...")
disable_vpn()
print("После отключения:")
ip3 = run_request()