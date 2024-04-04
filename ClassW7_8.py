# my_list = [1, 2, 3]
# iterator = iter(my_list)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for elem in iterator:
#     print(elem)
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)
# for elem in count:
#     print(elem)
#
# print(count.__iter__())
# print(count.__iter__())
# def raise_to_the_degrees(numbre, max_degree):
#     i = 0
#     for _ in range(max_degree):
#         i += 1
#
# res = raise_to_the_degrees(122345, 500)
# print(res)
# for _ in res:
#     print(_)


# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"I will help you with your {self.work}. Afterwards I will help you with {work}"
# helper = Helper("homework")
# print(helper("cleaning"))
#
# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
#     return helper
#
# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))



# def checker(*exc_types):
#     def checker(function):
#         def checker(*args, **kwargs):
#             try:
#                 result = function(*args, **kwargs)
#             except (exc_types) as exc:
#                 print(f"We have problems {exc}")
#             else:
#                 print(f"No problems. Result - {result}")
#         return checker
#     return checker
# @checker(NameError, TypeError, SyntaxError)
# def calculate(expression):
#     return eval(expression)
# calculate("2[2")
# from logging import*
# basicConfi
#     level=INFO,
#     filename="logs1.log",
#     filemode="w")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.eror("eror")
# logging.critical("critical")
# try:
#     print()
# if 2+2 == 4:
#     print("In fact, 2 + 2 equals 4")
#     assert 2 + 2 == 5 , 'wrong assert'
# """
# >>> 2+2
# 5
# """
# if __name__ =="__main__":
#     import doctest
#     doctest.testmod()
# def adder(*args, **kwargs):
#     result = 0
#     for _ in args:
#         result += _
#     for _ in kwargs.values():
#         result += _
#     return result