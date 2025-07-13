# function with parameter
def my_function(name):
    print(f"Hello {name}")

my_function('Mehedi')


# function with default parameter
def my_function(name ='Aowlad'):
    print(f"Hello {name}")

my_function()


# function with number of parameter
def my_function(fname,lname):
    print(f"Full name:  {fname} {lname}")

my_function('Mehedi','Alam')

# function with number of default parameter
def my_function(fname,lname='Alam'):
    print(f"Full name:  {fname} {lname}")

my_function('Mehedi')


# function with number of sum default parameter
def my_function(a=0,b=0,c=0):
    print(f"Sum :  {a+b+c}")

my_function()
my_function(5)
my_function(5,8)
my_function(5,8,10)