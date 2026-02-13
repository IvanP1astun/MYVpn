import requests

class SimpleProxyManager:
    def __init__(self, host, port, proto='http'):
        self.proxy_url = f"{proto}://{host}:{port}"
        self.proxies = {
            "http": self.proxy_url,
            "https": self.proxy_url
        }
        self.session = requests.Session()

    def get_current_ip(self):
        try:
            # Сначала пробуем БЕЗ прокси
            r = requests.get('https://api.ipify.org?format=json', timeout=5)
            return r.json()['ip']
        except Exception as e:
            return f"Ошибка: {e}"

    def get_ip_with_proxy(self):
        try:
            # Используем сессию с прокси
            r = self.session.get('https://api.ipify.org?format=json', 
                                 proxies=self.proxies, timeout=10)
            return r.json()['ip']
        except Exception as e:
            return f"Ошибка прокси: {e}"

# --- ТЕСТ ---
proxy = SimpleProxyManager('203.189.154.20', '1080')

print(f"[*] Реальный IP: {proxy.get_current_ip()}")
print(f"[*] IP через прокси: {proxy.get_ip_with_proxy()}")

# Проверка на успех
real = proxy.get_current_ip()
fake = proxy.get_ip_with_proxy()

if real != fake and "Ошибка" not in fake:
    print("\n✅ Успешно! Прокси подменил ваш IP на:", fake)
else:
    print("\n❌ Не удалось подменить IP. Проверьте адрес прокси.")