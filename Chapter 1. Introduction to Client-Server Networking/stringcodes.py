if __name__ == "__main__":
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
    input_characters = input_bytes.decode('utf-16')
    
    print(f"Giaỉ mã (decoding): {input_characters}")
    
    output_characters = 'Dương Mạnh Cường đẹp trai vô địch siêu cấp vũ trụ.\n'
    output_bytes = output_characters.encode('utf-8')
    
    print(f"Mã hóa (encoding): {output_bytes}")