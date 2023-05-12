#!/usr/bin/env python3

with open('output.txt', 'r') as f:
    out = f.read()

out = bytes.fromhex(out)

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

def recurse_init(text, result, in_strs, ibndex, identity, identity_list):
    for i in range(5):
        recurse(text, result, in_strs, i, chr(ord('a') + i), identity_list)

def recurse(text, result, in_strs, index, identity, identity_list):    
    decrypted = b''
    for i in range(len(text)):
        a = text[i]
        b = random_strs[index][i % len(random_strs[index])]
        decrypted += bytes([a ^ b])

    result.append(decrypted)
    identity_list.append(identity)
    
    for i in range(index + 1, 5):
        recurse(decrypted, result, in_strs, i, identity + chr(ord('a') + i), identity_list)
    # print(identity)

result = []
identity_list = []
recurse_init(out, result, random_strs, 0, "", identity_list)
result_xor = []
for i in range(len(result)):
    decrypted = b''
    for ii in range(len(result[i])):
        a = result[i][ii]
        b = b'picoCTF'[ii % len("picoCTF")]
        decrypted += bytes([a ^ b])
    result_xor.append(decrypted.decode())

# for i in range(len(result_xor)):
    # print(str(i) + ": " + result_xor[i])

correct = result_xor[26]
print(correct)
print(identity_list[26])

# print(len(result))

def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

print(encrypt(result[26], b'Africa!').decode())