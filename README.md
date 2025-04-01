![logo](/assets/imagem/cadeado.png)

# DEDSEC DEScrypto System 



Um sistema de criptografia, utilizando o algoritmo **DES(Data Encryption Standard)** para criptografar e descriptografar mensagens secretas.

---

## 📜 Descrição

Este sistema implementa um processo de criptografia e descriptografia baseado no algoritmo DES. Ele permite proteger mensagens com uma chave fixa, criptografando os dados em formato Base64 para fácil compartilhamento e armazenagem.

**Nota**: O DES é usado aqui para propósitos educacionais. Para sistemas reais, considere algoritmos mais modernos como AES.

---

## 🛠️ Funcionalidades

- Criptografar uma mensagem com uma chave fixa de 8 bytes.
- Descriptografar a mensagem criptografada para texto original.
- Codificação em Base64 para saída legível.

---

## ⚙️ Instalação

1. Certifique-se de ter o Python 3.6+ instalado.
2. Instale a dependência `pycryptodome`:
   ```bash
   pip install pycryptodome
   ´´´
3. Clone este respostitório ou copie o código `descrypto.py`:
    ```bash
    git clone 
    ´´´
---

## 🚀 Como Usar
1. Execute o script:
    ```bash
    python descrypto.py
    ´´´
2. Digite uma mensagem para criptografar.
3. O programa exibirá:

* A mensagem criptografada (Base64).
* A mensagem descriptografada.

---

## 📖 Exemplo de Uso

```plaintext
    DedSec DEScrypto System
    Digite a mensagem secreta: IN DEDSEC we trust
    Mensagem criptografada: A2vX1/w+LJ3wlGyHg70Dq2bdKnw=
    Menagem descriptografada:  IN DEDSEC we trust
```
---

## Estrutura do Código

### Funções 

* *Descrição*: Criptografa a mensagem de entrada usando DES.
* *Parâmetros*:
    * `message`: Uma string de texto que será criptografada.
* *Retorno*: O texto criptografado em Base64.
``decrypt(encrypt_message: str) -> str`
* *Descrição*: Descriptografa a mensagem criptografada.
* *Parâmetros*:
    * `encrypted_message`: Uma string em BAse64 representado o texto criptografado.
* *Retorno*: A mensagem descriptografada em texto simples.

---

## Constantes 

* `KEY`: Chave fixa de 8bvtes(`b'DedSec99'`). Essa chave é usada para criptografar e descriptografar mensagens.

---

## 🔒 Nota de Segurança

* Este projeto utiliza DES para desmonstração. DES é considerado inseguro apra uso em sistemas modernos.

* Evite usar uma chave fixa (`KEY`) em projetos em produção.

* Para segurança, prefira algoritmos mais avançados, como AES.

---

# Aviso ⚠️ 

A DEDSEC está revelando a verdade, faça dela oque quiser. Porém não somos responsáveis pelos seus atos.

---





