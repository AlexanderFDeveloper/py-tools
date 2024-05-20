import base64
import argparse

def encode(string):
    try:
        # Codifica a string
        encoded_bytes = base64.b64encode(string.encode('utf-8'))
        # Converte os bytes codificados para uma string
        return encoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Erro ao codificar a string: {e}"

def decode(base64_string):
    try:
        # Decodifica a string Base64
        decoded_bytes = base64.b64decode(base64_string)
        # Converte os bytes decodificados para uma string
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Erro ao decodificar a string: {e}"

parser = argparse.ArgumentParser(description="Codificar ou decodificar strings em Base64.")
parser.add_argument('operation', choices=['encode', 'decode'], help="Operação a ser realizada: 'encode' para codificar, 'decode' para decodificar")
parser.add_argument('string', help="A string a ser codificada ou decodificada")

args = parser.parse_args()

if args.operation == 'encode':
    print(encode(args.string))
elif args.operation == 'decode':
    print(decode(args.string))
