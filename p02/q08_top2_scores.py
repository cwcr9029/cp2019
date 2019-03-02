'''Program that prompts the user to enter the number of students and 
each student's name and score, and finally displays the student with
 the highest score and the student with the second-highest score.
 
 Also works if there are more than 1 student that got highest/second
 highest score'''

student_num = int(input("Enter number of students to add into the system: "))

score_name_list = []
for i in range(student_num):
    name = input("Enter name of student {0}: ".format(i+1))
    score = int(input("Enter score of student {0}: ".format(i+1)))
    score_name_list.append((score,name))
score_name_list.sort(reverse=True)
highest = score_name_list[0][0]
for index, a in enumerate(score_name_list):
    if a[0] < highest:
        second_highest = a[0]
        second_index = index
        break
    elif index == len(score_name_list) - 1: #If all scores are the same, prevent next loop from running
        second_index = index + 1
        second_highest = None

for indx, b in enumerate(score_name_list[second_index:],second_index):
    if b[0] < second_highest:
        third_index = indx
        break
    elif indx == len(score_name_list) - 1:
        third_index = None

print("Highest scoring students (Highest score = {0}): "\
    .format(highest), end='')

for n in score_name_list[0:second_index]:
    print(n[1],end=' ')

if second_highest != None: 
    print("Second highest scoring students (Second highest score = {0}): "\
        .format(second_highest), end='')

    for s in score_name_list[second_index:third_index]:
        print(s[1],end=' ')