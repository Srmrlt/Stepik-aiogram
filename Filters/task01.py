def custom_filter(some_list: list) -> bool:
    int_list = [num for num in some_list if isinstance(num, int) if not (num % 7)]
    return sum(int_list) <= 83


if __name__ == '__main__':
    # ls = [7, 14, 28, 32, 32, 56]  # False
    ls = [7, 14, 28, 32, 32, '56']  # True
    print(custom_filter(ls))
