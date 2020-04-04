"""
Implement the modify_list function, which takes a list of integers as an argument.
This function should remove all odd numbers from the list, and divide even numbers by two. 
The function should not return anything, only modify the input list."
"""
def modify_list(a):
    for i in range(len(a)-1,0,-1):
        if a[i] % 2 != 0:
            del a[i]
        else:
            a[i] = int(a[i] / 2)
def modify_list2(a):
    b = [x // 2 for x in a if x % 2 == 0]
    a.clear()
    a.extend(b)

def modify_list3(a):
    a[:] = [x // 2 for x in a if x % 2 == 0]

def test_function():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a_id = id(a)

    modify_list(a)
    assert a == [0, 1, 2, 3, 4], "error" # True
    assert a_id == id(a), "error"  # True   
    print("pass")
