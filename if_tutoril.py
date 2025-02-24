
n = input("Enter your number")
n = int(n)

if n%2 ==0: 
    print("The number is even")

else:
    print("The number is odd")
print("The number you entered is: ", n)


print(type(n))

class_name = ["web", "python", "java", "c++"]
course_check = input("Enter your course: ")

if course_check in class_name:
    print(f"The course is available {course_check}")
else:
    print("The course is not available")



pak = ["chai" , "orange", "naan"]
name = ["hassan" , "ali", "ahmed"]
dish = input("Enter your dish: ")

if dish in pak: 
    print("The dish is available")
elif dish in name:
    print(f"The dish is available {dish}")
else:    
    print("The dish is not available")






name1 = input("Enter your name: ")
cc = int(name1)
print( f" your name is {name1} " )




