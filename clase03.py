def run():
    print('clase 03')

    my_list_dict = {}

    for i in range(1, 11):
        if (i % 3 != 0):
            my_list_dict[i] = i

    print(my_list_dict)


if __name__ == '__main__':
    run()
