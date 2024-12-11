from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# Chave de 8 bytes (DES requer exatamente 8 bytes para a chave)
KEY = b'DedSec99'  # Escolha algo personalizado e misterioso

def encrypt(message):
    """
    Criptografa a mensagem usando DES.
    """
    cipher = DES.new(KEY, DES.MODE_ECB)  # Modo ECB (simplificado para este exemplo)
    padded_message = pad(message.encode(), DES.block_size)  # Ajusta o tamanho ao bloco
    encrypted_bytes = cipher.encrypt(padded_message)
    return base64.b64encode(encrypted_bytes).decode()  # Codifica como base64 para fácil leitura

def decrypt(encrypted_message):
    """
    Descriptografa a mensagem criptografada.
    """
    cipher = DES.new(KEY, DES.MODE_ECB)
    encrypted_bytes = base64.b64decode(encrypted_message)
    decrypted_message = unpad(cipher.decrypt(encrypted_bytes), DES.block_size)
    return decrypted_message.decode()

# Testando o DEScrypto
if __name__ == '__main__':
    print("DedSec DEScrypto System")
    
    original_message = input("Digite a mensagem secreta: ")
    encrypted = encrypt(original_message)
    print(f"Mensagem criptografada: {encrypted}")
    
    decrypted = decrypt(encrypted)
    print(f"Mensagem descriptografada: {decrypted}")
