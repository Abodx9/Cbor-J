
def _cbor_encode_text(s: str) -> bytes:
    b = s.encode('utf-8')
    n = len(b)
    if n < 24:
        return bytes([0x60 | n]) + b
    elif n < 256:
        return b'\x78' + bytes([n]) + b
    elif n < 65536:
        return b'\x79' + n.to_bytes(2, 'big') + b
    elif n < 4294967296:
        return b'\x7a' + n.to_bytes(4, 'big') + b
    else:
        return b'\x7b' + n.to_bytes(8, 'big') + b
