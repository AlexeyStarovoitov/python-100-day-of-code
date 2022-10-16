def f():
    s = "Inside function f"
    print(s)
    
def print_price(name='bananas', count=6, price=1.74):
    print(f'{count:d} of {name:s} costs {price:.2f}')
    
def mutable_func(my_list = None):
    
    if my_list == None:
        my_list = []
    my_list.append('###')
    return my_list
    
def pass_arg_func(fx):
    #print(f'fx = {fx}\nid(fx): {id(fx)}')
    fx = 10
    print(f'fx = {fx}')
    #print(f'fx = {fx}\nid(fx): {id(fx)}')

def pass_arg_func2(fx):
    fx[0] = 10
 
def return_func():
    return dict(haha=1, baba=2, dada=3)

def tuple_return_func():
    return 'haha', 'baba', 'dada'
    
def null_return_func():
    return

def double_list(x):
    for i in range(len(x)):
        x[i] = x[i] * 2
        
def avg_func(*arg):
    return sum(arg)/len(arg)
    
def kw_func(**kwargs):
    for (key, val) in kwargs.items():
        print(f'{key}->{val}')

def all_pass_type_func(a, b, *args, d, **kwargs):
    
    print(f'a = {a}\nb = {b}')

    print('args arguments:')
    for i in args:
        print(f'{i}')
        
    print(f'd = {d}')

    print('kwargs arguments:')
    for (key, val) in kwargs.items():
        print(f'{key}->{val}')
    
if __name__=="__main__":
    
    print('\n')
    print("Basic experiments with functions:")
    print("Before function f")
    f()
    print("After function f\n")
    
    print("Calling print_price with positional arguments:")
    print_price('bananas', 6, 1.74)
    print("Calling print_price with keyword argumants:")
    print_price(count = 6, name = 'bananas', price = 1.74)
    print_price('bananas', 6, price = 1.74)
    
    print('\n')
    print('Experimenting with defualt arguments:')
    print_price()
    print_price('apples')
    print_price(count=10)
    print_price(price=5.4)
    
    print('\n')
    print('Experimenting with mutable objects:')
    print(f'{mutable_func()}\n')
    print(f'{mutable_func()}\n')
    print(f'{mutable_func()}\n')
    
    print('\n')
    print('Experimenting with argument passing:')
    x = 5
    print(f'x before pass_arg_func: {x}')
    print('Calling pass_arg_func:')
    pass_arg_func(x)
    print(f'x after pass_arg_func: {x}')
    
    for i in (10, "one", {1,2,3}, {'ha':1, 'haha':2}, [3,2,1]):
        pass_arg_func(i)
        print(f'i: {i}')
   
    print('\n')
    x = ['ha', 'ba', 'dvd', 'dsdd']
    print(f'x before pass_arg_func2: {x}')
    pass_arg_func2(x)
    print(f'x after pass_arg_func2: {x}')
    
    print('\n')
    print('Experimanting with return statement in functon')
    print(f'return_func result: {return_func()}')
    print(f'return_func()[\'dada\'] result: {return_func()["dada"]}')
    
    print('\n')
    print(f'Type of tuple_return_func: {type(tuple_return_func())}')
    print(f'Type of null_return_func: {type(null_return_func())}')
    
    print('\n')
    x = [1,2,3,4,5]
    print(f'x before double_list function: {x}')
    double_list(x)
    print(f'x after double_list function: {x}')
    
    
    print('\n')
    print('Experimenting with positional arguments passing')
    a = [1,2,3,4,5]
    print(f'average of {a} is {avg_func(1,2,3,4,5)}')
    print(f'average of {a} is {avg_func(*a)}')
    
    print('\n')
    print('Experimenting with keyword arguments passing')
    kw_func(**dict(haha=1, baba=2, data=3))
    
    print('\n')
    print('Experimenting with all arguments type passing:')
    all_pass_type_func('dfdf', 2, *['fff', 1, 'xvcxcv'], d = 45, **dict(aa=1, bb=2, cc=3))
    
   
    
    