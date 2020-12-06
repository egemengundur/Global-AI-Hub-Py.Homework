name="Egemen"
surname="Gundur"

name1= input("Enter your name: ")
surname1= input("Enter your surname: ")
count=0
def average_calculator():
    midterm_grade=int(input("Enter your Mid Term grade:"))
    final_grade=int(input("Enter your Final grade:"))
    project_grade=int(input("Enter your Project grade:"))
    grades={"Midterm:": midterm_grade,"Final:":final_grade,"Project:":project_grade}
    print(grades)
    last_grade=(midterm_grade*0.3 + final_grade*0.5 + project_grade*0.2)
    print(last_grade)
    if last_grade>90:
        print("Your letter grade: AA")
    elif last_grade>70:
        print("Your letter grade: BB")
    elif last_grade>50:
        print("Your letter grade: CC")
    elif last_grade>30:
        print("Your letter grade: DD")
    else:
        print("Your letter grade: FF")
        print("YOU HAVE FAILED")

def course_selection():
    courses=[]
    course_name= input("Enter your course name (Q to quit): ")
    courses.append(course_name.capitalize())
    count=0
    while count<4:
        count +=1 
        course_name= input("Enter your course name: ")
        courses.append(course_name.capitalize())
        if count<=2 and course_name=="q":
            print("You failed in class")
            break
        elif count>=3 and course_name=="q":
            print("Your courses has been saved!")
            courses.pop()
            print(courses)
            break
        elif count==4:
            print("Your courses has been saved!")
            print(courses)
            break   

if name==name1.capitalize() and surname==surname1.capitalize():
    print("Welcome",name1.capitalize(),surname1.capitalize())
    course_selection()
    average_calculator()
else:
    while name!=name1 and surname!= surname1:
        count+=1
        if name!=name1 and surname!= surname1 and count!=3:
            print("Incorrect name/surname.")
            name1= input("Enter your name: ")
            surname1= input("Enter your surname: ")
        if name==name1 and surname==surname1 and count==3:
            print("Welcome",name1.capitalize(),surname1.capitilize())
            course_selection()
            average_calculator()
            break
        elif count==3:
            print("Please try again later!")
            break

        
            
            
        
