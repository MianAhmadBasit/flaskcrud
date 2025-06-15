

for i in range(0,10):
    print(i)


sallary  = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000] ; 

total_sallary = 0 

for sal in sallary:
    total_sallary += sal
print(f"you sallary is {total_sallary}")





expensess = [1000,2222,3333,4444]

total_expense = 0


for expens in expensess:
    total_expense = total_expense + expens
print(total_expense)  
#  check indent must



# total_expense = expensess[0] + expensess[1] +expensess[2] 
# print(total_expense)


for i in range (0,9):
    print(i)


sallary = [3000,7000,5444,8888]
total_sallary = 0

for i in range(len(sallary)):
    sal = sallary[i]
    print( f'Month {i+1}, sallry : {sal}')
    total_sallary += sal

print("total sallary is" , total_sallary) 

# enummartion

check = [2000,1000,3000]

for i, check in enumerate(check):
    if check>=2000:
        print(f"month {i+1}has check >= 2000" , [i] )
        break


# indentation must impt
n= 0

while n<=10:
    print(n)
    n +=2



