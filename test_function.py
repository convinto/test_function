def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()     #функция test_function выводит функцию inner_function
inner_function()    #функиця не видна в глобальной области видимости - получаем ошибку
