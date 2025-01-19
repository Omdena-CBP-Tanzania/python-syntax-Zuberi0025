def format_string(name, age):
    name='Zuberi'
    age=30
    print(f'My Name is {name}, am {age} years old')
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    

def conditional_check(number):
    x=5
    if x>10:
        print('x is greater')
    elif x<10:
        print('x is less')
    else:
        print('is equal to 10')
    
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    

def loop_sum(n):
    n=int(2)
    sum=0
    for i in range(1,n+1):
        sum+=i
      
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    
def list_operations(numbers):
    list=[1,2,3,5,6,7,8,11,21,8,9,41,6]
    print(sum(list))
    print(max(list))
    print(min(list))
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    

def dict_operations(students_dict):
    dict_by_func = dict(Jonah = 65,
                    Siwema = 70,
                    Chris= 77,
                    Zuberi = 80,
                    Abdallah= 97, 
                    Grace= 100)
    print(dict_by_func['Zuberi','Abdallah','Grace']) 
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    

def set_operations(list1, list2):
    list1=[1,2,3,"a","z",85]
    list2=["c",2,5,6,8,"a","t"] #Common element can be found in sets by  intersection operation
    
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    

def arithmetic_ops(a, b):
    a=7
    b=9
    c=a+b
    d=a-b
    e=a*b
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    

def logical_ops(x, y):
    x = 3
    y = 7

    if x > 0 and y > 0:
        print("Both x and y are positive.")
    else:
        print("At least one is not positive.")

    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    

def bitwise_ops(a, b):
    number = 0
    if number & 1:  
        print("Odd")
    else:
        print("Even")

    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
