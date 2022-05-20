def greet_multiple(*numbers, **students):
    num=1
    for number in numbers:
         num*=number
         print(num) 
    print(f"Hello {students}")