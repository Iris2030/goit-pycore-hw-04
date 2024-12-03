import sys
from pathlib import Path
from colorama import Fore

def print_directory_structure(path, indent_level=0):
    try:
        # Конвертуємо шлях у об'єкт Path
        dir_path = Path(path)
        
        if not dir_path.exists():
            print(f"{Fore.RED}Шлях не існує: {path}")
            return
        
        if not dir_path.is_dir():
            print(f"{Fore.RED}Це не директорія: {path}")
            return
        
        # Проходимо по всіх файлах та піддиректоріях
        for item in dir_path.iterdir():
            indent = ' ' * indent_level
            if item.is_dir():
                # Колір для директорій - зелений
                print(f"{indent}{Fore.GREEN}📂 {item.name}")
                # Рекурсивно обходимо піддиректорії
                print_directory_structure(item, indent_level + 4)
            else:
                # Колір для файлів - синій
                print(f"{indent}{Fore.CYAN}📜 {item.name}")
    
    except Exception as e:
        print(f"{Fore.RED}Сталася помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Будь ласка, вкажіть шлях до директорії.")
    else:
        directory_path = sys.argv[1]
        print_directory_structure(directory_path)