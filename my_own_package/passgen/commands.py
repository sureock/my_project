import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Программа для генерации безопасного пароля"
        )
    parser.add_argument(
        "l",
        type=int,
        help="Длина пароля, рекомендуется = 12"
        )
    parser.add_argument(
        "-s", "--special",
        action="store_true",
        help="Добавляет специальные символы"
    )
    parser.add_argument(
        "-d", "--digits",
        action="store_true",
        help='Добавляет цифры в пароль'
    )
    parser.add_argument(
        "-u", "--upper",
        action="store_true",
        help="Добавляет прописные буквы в пароль"
    )
    parser.add_argument(
        "-hash", "--hasher",
        type=str, choices=["sha256", "md5", "blake2b"],
        help="Тип хэширования, базовое значение = sha256"
    )
    parser.add_argument(
        "-p", "--path",
        type=str,
        action='store',
        help="Путь сохранения пароля, если нет пути - пароль не сохраняется"
    )
    args = parser.parse_args()
    return (args.l, args.special, args.digits,
            args.upper, args.hasher, args.path)
