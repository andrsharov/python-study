from include.my_module import get_lucky_number, DataProvider


def first_function():
    number = get_lucky_number()
    return number


def second_function():
    provider = DataProvider()
    data = provider.get_data()
    return data


if __name__=="__main__":
    print("Вызываем первую функцию...")
    print(first_function())
    print("Вызываем вторую функцию...")
    print(second_function())
