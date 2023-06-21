import random
import string

pass_length = int(input("Digite o tamanho da senha desejada: "))

chars = string.ascii_letters + string.digits + "çÇ!@#$%&*()-=+,.;:/?"

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(pass_length)))
