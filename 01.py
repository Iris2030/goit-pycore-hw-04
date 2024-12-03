def total_salary(path):
    try:
        with open(path) as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Помилка обробки рядка: {line.strip()}")
                    continue

            # Перевіряємо, чи є оброблені зарплати
            if not salaries:
                print("Файл не містить коректних даних для обчислення.")
                return None

            # Обчислюємо загальну та середню зарплату
            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError:
        # Обробка випадку, коли файл не знайдено
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        # Загальна обробка інших можливих помилок
        print(f"Сталася несподівана помилка: {e}")
        return None