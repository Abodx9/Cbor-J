# Cbor-J
Lightweight pure-Python library to encode/decode JSON strings to/from CBOR — with optional zlib compression.

Perfect for reducing storage size of large JSON files.

## Features

- Pure Python, no dependencies
- Simple API: `encode(json_str, compress=False) → bytes`, `decode(bytes, compress=False) → str`
- Optional zlib compression (like EU Digital COVID Certificate format, *without* signing/Base45)

