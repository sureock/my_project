from passgen import *


args = commands.get_args()
generated = generator.get_generated_password(args[0],
                                             args[1],
                                             args[2],
                                             args[3],
                                             args[4]
                                             )
print(f'Пароль: {generated[0]}, тип хэширования: {generated[1]}')
print(storage.save_hash_in_file(generated[0], generated[1]))
