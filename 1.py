"""1) Создать переменную типа String"""
a = "Hello World!"
print(a, type(a))
"""2) Создать переменную типа Integer"""
b = 8
print(b, type(b))
"""3) Создать переменную типа Float"""
c = 8.0
print(c, type(c))
"""4) Создать переменную типа Bytes"""
d = bytes(8)
print(d, type(d))
"""5) Создать переменную типа List"""
e = ["Hello World!", 8]
print(e, type(e))
"""6) Создать переменную типа Tuple"""
f = ("Hello World!", 8)
print(f, type(f))
"""7) Создать переменную типа Set"""
k = set("Hello World!")
print(k, type(k))
"""8. Создать переменную типа Frozen set"""
l = frozenset("Hello World!")
print(l, type(l))
"""9) Создать переменную типа Dict"""
m = {"a": 1, "b": 2}
print(m, type(m))
"""10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных."""

"""11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль."""
first = "Hello "
second = "World!"
finish = first + second
print(finish)
"""12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)"""
print(a, str(b))
"""13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)"""
print(a + " " + str(b))
