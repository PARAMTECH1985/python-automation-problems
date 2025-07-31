from requests import get

def detect_my_public_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip