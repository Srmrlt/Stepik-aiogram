anonymous_filter = lambda x: x.lower().count('я') >= 23


if __name__ == '__main__':
    re = 'Я - последняя буква в алфавите!'  # False
    # re = 'яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'  # True
    print(anonymous_filter(re))
