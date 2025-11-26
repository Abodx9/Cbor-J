
def _cbor_decode_text( bytes) -> tuple[str, int]:
    if not 
        raise ValueError("Empty input")
    first = data[0]
    if (first & 0xE0) != 0x60:
        raise ValueError("Not a CBOR text string (major type 3)")

    if first < 0x78:
        length = first & 0x1F
        header_len = 1
    elif first == 0x78:
        if len(data) < 2: raise ValueError("Truncated")
        length = data[1]; header_len = 2
    elif first == 0x79:
        if len(data) < 3: raise ValueError("Truncated")
        length = int.from_bytes(data[1:3], 'big'); header_len = 3
    elif first == 0x7A:
        if len(data) < 5: raise ValueError("Truncated")
        length = int.from_bytes(data[1:5], 'big'); header_len = 5
    elif first == 0x7B:
        if len(data) < 9: raise ValueError("Truncated")
        length = int.from_bytes(data[1:9], 'big'); header_len = 9
    else:
        raise ValueError("Invalid additional info")

    if len(data) < header_len + length:
        raise ValueError("Truncated text data")
    return data[header_len:header_len + length].decode('utf-8'), header_len + length
