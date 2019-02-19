# Binary
# from 0 to 255, 8bit

# bytes vs bytearray
# bytes : immutable, as tuple of byte
# bytearray : mutable, as list of byte

blist = [1, 2, 3, 255]

# bytes
a_bytes = bytes(blist)  # b'\x01\x02\x03\xff'
b_bytes = bytes(range(0, 255))

# bytearray
a_byte_array = bytearray(blist)
b_bytes = bytearray(range(0, 255))