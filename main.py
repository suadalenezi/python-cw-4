def my_name():
    print("my name is suad")

my_name()



def my_meal(food,drink):
    print("I like to eat {sushi} and while drinking {pepsi}")
    
my_meal("sushi","pepsi")


def cube(number):
    return (number**3)


def by_three(number):
    if number%3==0:
       return cube(number)
    else:
       return False

print(by_three(9))
