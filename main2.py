import pwn

HOST = "143.198.215.203"
PORT = 8031

p = pwn.remote(HOST, PORT)

# 1. Dapatkan IV dan CT flag
p.sendlineafter(b">> ", b"3")
iv_flag = bytes.fromhex(p.recvline().strip().decode())
ct_flag = bytes.fromhex(p.recvline().strip().decode())

print(f"[*] IV Flag: {iv_flag.hex()}")
print(f"[*] CT Flag: {ct_flag.hex()}")

# 2. Kirim seluruh ciphertext flag sebagai plaintext ke Opsi 1 (Enkripsi)
print("[*] Mengirim CT Flag sebagai plaintext ke oracle enkripsi...")
p.sendlineafter(b">> ", b"1")
p.sendlineafter(b"Data (hex): ", ct_flag.hex().encode())

# 3. Terima hasilnya
result_hex = p.recvline().strip().decode()
result = bytes.fromhex(result_hex)

print(f"[*] Hasil yang diterima: {result.hex()}")

# 4. Lakukan XOR antara hasil dengan IV_flag
# Trik sebenarnya sering kali melibatkan XOR dengan IV asli
final_result = bytes(a ^ b for a, b in zip(result, iv_flag))

# Kita mungkin perlu melakukan XOR dengan blok ciphertext lain juga
# tapi mari kita mulai dengan yang paling sederhana
final_result_xor_c1 = bytes(a ^ b for a, b in zip(result, ct_flag[:16]))


print("\n--- Analisis Hasil ---")
print(f"[1] Hasil mentah: {result.decode('latin-1', errors='ignore')}")
print(f"[2] Hasil di-XOR dengan IV: {final_result.decode('latin-1', errors='ignore')}")
print(f"[3] Hasil di-XOR dengan C1: {final_result_xor_c1.decode('latin-1', errors='ignore')}")

p.close()