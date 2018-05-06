hex_str = str(input("Enter the hex string: "))
if not hex_str.startswith('0x'):
	hex_str = '0x' + hex_str

ascii_str = ''.join(chr(int(hex_str[i:i+2], 16)) for i in range(2, len(hex_str), 2))

print(ascii_str)

