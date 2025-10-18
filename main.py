from passgen import *

args = commands.pass_parser()
generated = generator.generate(args[0],
                               args[1],
                               args[2],
                               args[3],
                               args[4]
                               )
print(f'Пароль: {generated[0]}, тип хэширования: {generated[1]}')
