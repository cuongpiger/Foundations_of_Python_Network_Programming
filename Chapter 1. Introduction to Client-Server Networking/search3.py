import http.client, json
from urllib.parse import quote_plus

base = '/search'

def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = 'Manh Cuong'
    header = {'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, header)
    reply = connection.getresponse().read()
    coordinate = json.loads(reply.decode('utf-8'))
    
    print(f"Địa chỉ {address} nằm ở tọa độ ({coordinate[0]['lat']},{coordinate[0]['lon']})")    
    
if __name__ == '__main__':
    address = '227 Đ. Nguyễn Văn Cừ, Phường 4, Quận 5, Thành phố Hồ Chí Minh, Vietnam'
    geocode(address)