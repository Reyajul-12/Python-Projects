
# 1. write a program to print multiplication table of a given number using for loop.
# n =int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{n} X {i} = {n * i}")



# 2. write a program to greet all the person names stored in a list 'l' and which starts with S.
# l = ["Reyajul","Islam","Rana","Raju","Raja"]

l = ["Reyajul","Islam","Rana","Raju","Raja"]

for name in l:
    if(name.startswith("R")):
        print(f"Hello {name}")

