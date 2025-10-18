import argparse


def pass_parser():
    parser = argparse.ArgumentParser(
        description="Программа для генерации безопасного пароля"
        )
    parser.add_argument(
        "L",
        type=int,
        help="Длина пароля, базовое значение = 12"
        )
    parser.add_argument(
        "--special", "-s",
        action="store_true",
        help="Добавляет специальные символы"
    )
    parser.add_argument(
        "--digits", "-d",
        action="store_true",
        help='Добавляет цифры в пароль'
    )
    parser.add_argument(
        "--upper", "-u",
        action="store_true",
        help="Добавляет прописные буквы в пароль"
    )
    parser.add_argument(
        "--hasher", "-h",
        type=str, choices=["sha256", "md5", "blake2b"],
        help="Тип хэширования, базовое значение = sha256"
    )
    args = parser.parse_args()
    return args
