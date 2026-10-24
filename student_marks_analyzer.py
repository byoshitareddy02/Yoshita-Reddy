
def calculate_grade(average):
    if average>=90:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=40:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter student name : ")

    marks = []

    for i in range(1,4):
        while True:
            try:
                mark = float(input(f"Enter marks of subject {i}(1-100) : "))

                if 0<= mark <=100:
                    marks.append(mark)
                    break
                else:
                    print("Number must be between 1 to 100")

            except ValueError:
                print("Please enter a valid number")

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    result = "Pass" if all(m>=35 for m in marks) else "Fail"

    print("\n----Student Report")
    print("Name : ",name)
    print("Total : ",total,"/300")
    print("Average : ",round(average,2))
    print("Grade : ",grade)
    print("Result : ",result)

if __name__ == "__main__":
    main()

