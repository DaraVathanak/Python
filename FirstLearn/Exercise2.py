num = int(input('How many students do you want to enter: '))
students = []

def get_valid_score(subject):
    while True:
        try:
            score = float(input(f'Enter the score of {subject}: '))
            if score < 0:
                print("⚠️Score can't be negative. Please input again.⚠️")
            elif score > 100:
                print("⚠️Score can't be over 100. Please input again.⚠️")
            else:
                return score
        except ValueError:
            print("⚠️Invalid input. Please enter a number.⚠️")

for i in range(num):
    print(f'\nEnter Details for Student #{i + 1}')
    name = input('Name: ')

    Ai = get_valid_score('Ai_for_Robotics')
    DC = get_valid_score('Data_Communication')
    DS = get_valid_score('Data_Structures')
    DB = get_valid_score('Data_Base_System')
    EN = get_valid_score('English')

    Total = Ai + DC + DS + DB + EN
    Average = Total / 5

    if Average >= 90:
        Grade = 'A'
    elif Average >= 80:
        Grade = 'B'
    elif Average >= 70:
        Grade = 'C'
    elif Average >= 60:
        Grade = 'D'
    else:
        Grade = 'F'

    student_data = [name, Ai, DC, DS, DB, EN, Total, Average, Grade]
    students.append(student_data)

print('\n-- All the Student Information --')
headers = ["Name", "AI", "DC", "DS", "DB", "EN", "Total", "Average", "Grade"]
print("{:<15} {:<6} {:<6} {:<6} {:<6} {:<6} {:<8} {:<8} {:<6}".format(*headers))

for s in students:
    print("{:<15} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<8.2f} {:<8.2f} {:<6}".format(*s))
