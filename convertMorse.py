import argparse

# Dicionário de mapeamento Morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Inverte o dicionário para decodificação
MORSE_CODE_DICT_REVERSED = {value: key for key, value in MORSE_CODE_DICT.items()}

def encode(message):
    try:
        return ' '.join(MORSE_CODE_DICT[char] for char in message.upper())
    except KeyError as e:
        return f"Caractere não suportado para codificação: {e.args[0]}"

def decode(morse_code):
    try:
        return ''.join(MORSE_CODE_DICT_REVERSED[code] for code in morse_code.split())
    except KeyError as e:
        return f"Sequência Morse inválida para decodificação: {e.args[0]}"

parser = argparse.ArgumentParser(description="Codificar ou decodificar mensagens em código Morse.")
parser.add_argument('operation', choices=['encode', 'decode'], help="Operação a ser realizada: 'encode' para codificar, 'decode' para decodificar")
parser.add_argument('string', help="A mensagem a ser codificada ou o código Morse a ser decodificado")

args = parser.parse_args()

if args.operation == 'encode':
    print(encode(args.string))
elif args.operation == 'decode':
    print(decode(args.string))
