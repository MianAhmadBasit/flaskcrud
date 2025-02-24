def add(a,b):
    return a+b  # return is a keyword that returns the value of the function    
add(2,3)



def find_total(check):
    total = 0 
    for check in check:
     total += check
    return total





expensee_ahmad1 = [33,55,77]
expensee_ahmad3 = [31,525,277]
expensee_ahmad2 = [3,55,77]

total = find_total(expensee_ahmad1)
print("expensee ahmad 1" , expensee_ahmad1, '\n' ,  total)

total = find_total(expensee_ahmad3)
print("expensee ahmad 3" , expensee_ahmad3, '\n' ,  total)


total = find_total(expensee_ahmad2)
print("expensee ahmad 2" , expensee_ahmad2 , '\n' ,  total)
# total = 0 
# for check in expensee_ahmad1:
#     total += check

# print("ahmad total expense" , total)

# for check in expensee_ahmad2:
#     total += check

# print("ahmad2 total expense" , total)