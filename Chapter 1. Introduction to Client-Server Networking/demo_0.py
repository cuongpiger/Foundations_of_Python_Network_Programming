from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = '227 Đ. Nguyễn Văn Cừ, Phường 4, Quận 5, Thành phố Hồ Chí Minh, Vietnam'
    user_agent = 'Manh Cuong'
    location = Nominatim(user_agent=user_agent).geocode(address)
    
    print(f"Địa chỉ {address} ở vĩ độ {location.latitude} - kinh độ {location.longitude}.")