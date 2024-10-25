# Fundamentação teórica:
""" 
    Há 3 critérios que dados dummy em um processo de one-time pad devem obedecer
    para gerar um produto de criptografia inquebrável, tais quais:
    1. Devem ser do mesmo tamanho dos dados originais.
    2. Devem ser aleatórios e não podem ser repetidos.
    3. Devem ser totalmente secretos.
"""

"""
    A operação lógica XOR é utilizada para realizar a criptografia no one-time pad.
    XOR opera em nível de bits, e o que torna tão conveniente usá-la é o fato de que
    podemos obter o valor de um terceiro operando somando os valores de um operando e
    do produto:
    A + B = C
    B + C = A
    C + A = B
"""

from secrets import token_bytes
from typing import Tuple

# Gerando a chave aleatória para ser usada como dados dummy:
def random_key(length: int) -> int:
    # gera length bytes aleatórios
    tb: bytes = token_bytes(length)
    # converte esses bytes para int, em uma cadeia de bits e a devolve
    return int.from_bytes(tb, 'big') # retorna um int preenchido com length bytes aleatórios.
    


# Criptografando usando o XOR:
def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode('utf-8') 
    dummy: int = random_key(len(original_bytes)) # Chave aleatória
    original_key: int = int.from_bytes(original_bytes, 'big')
    encrypted: int = original_key ^ dummy #XOR
    return dummy, encrypted



# Decriptografando usando o XOR:
def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^key2 # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big') # Converte o int para bytes
    return temp.decode('utf-8') # Converte bytes para string

if __name__ == "__main__":
    key1, key2 = encrypt('One Time Pad!')
    result: str = decrypt(key1, key2)
    print(result)