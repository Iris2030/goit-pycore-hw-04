def get_cats_info(path):
    try:
          with open(path, encoding='utf-8') as file:
                cats = []
                for line in file:
                    try:
                        cat_id, cats_name,cats_age = line.strip().split(',')
                        cats.append({"id": cat_id, "name": cats_name, "age": cats_age })
                        print(cats)
                    except ValueError:
                        print(f"Помилка обробки рядка: {line.strip()}")
                        continue
    except FileNotFoundError:
        # Обробка випадку, коли файл не знайдено
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        # Загальна обробка інших можливих помилок
        print(f"Сталася несподівана помилка: {e}")
        return None

get_cats_info('./cats_info.txt')