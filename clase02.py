def run():

    my_list = []

    my_list = [i for i in range(1, 100) if i % 3 != 0]

    print(my_list)

    my_list_02 = []
    for i in range(1, 101):
        if i % 3 != 0:
            my_list_02.append(i**2)
    print(my_list_02)


if __name__ == "__main__":
    run()
