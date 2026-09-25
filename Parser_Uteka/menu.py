import os


if __name__ == '__main__':
    flag = False
    print('Выберите дальнейшее действие: ')
    print('1. Ввести ссылку на препарат и получить результат')
    print('2. Изменить настройки программы')
    print('3. Закончить работу')
    while (x := input()) != '3':
        if x == '1':
            os.system('cls')
            input('Выполняется работа программы, нажмите enter...')

        if x == '2':
            os.system('cls')
            print('Выберите дальнейшее действие: ')
            print('1. Изменить браузер')
            print('2. Пройти новую авторизацию')
            print('3. Назад')

            while (y := input()) != '3':
                if y == '1':
                    os.system('cls')
                    print('Браузер изменён')
                    print()
                    print()
                    print('Выберите дальнейшее действие: ')
                    print('1. Назад')
                    print('2. В главное меню')

                    while (z := input()) != 3:
                        if z == '1':
                            break

                        if z == '2':
                            flag = True
                            break

                        os.system('cls')
                        print('Браузер изменён')
                        print()
                        print()
                        print('Выберите дальнейшее действие: ')
                        print('1. Назад')
                        print('2. В главное меню')

                if flag:
                    break
                os.system('cls')
                print('Выберите дальнейшее действие: ')
                print('1. Изменить браузер')
                print('2. Пройти новую авторизацию')
                print('3. Назад')

        flag = False
        os.system('cls')
        print('Выберите дальнейшее действие: ')
        print('1. Ввести ссылку на препарат и получить результат')
        print('2. Изменить настройки программы')
        print('3. Закончить работу')

