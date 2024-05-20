import argparse

def encode(string):
    try:
        return ' '.join(str(ord(char)) for char in string)
    except Exception as e:
        return f"Erro ao codificar a string: {e}"

def decode(ascii_string):
    try:
        return ''.join(chr(int(num)) for num in ascii_string.split())
    except Exception as e:
        return f"Erro ao decodificar a string ASCII: {e}"
      
parser = argparse.ArgumentParser(description="Codificar ou decodificar strings em ASCII.")
parser.add_argument('operation', choices=['encode', 'decode'], help="Operação a ser realizada: 'encode' para codificar, 'decode' para decodificar")
parser.add_argument('string', help="A string a ser codificada ou decodificada")

args = parser.parse_args()

if args.operation == 'encode':
    print(encode(args.string))
elif args.operation == 'decode':
    print(decode(args.string))
