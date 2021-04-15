import requests

def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Manh Cuong'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    
    print(f"Địa chỉ {address} nằm ở tọa độ ({reply[0]['lat']},{reply[0]['lon']})")
    
if __name__ == '__main__':
    address = '227 Đ. Nguyễn Văn Cừ, Phường 4, Quận 5, Thành phố Hồ Chí Minh, Vietnam'
    geocode(address)