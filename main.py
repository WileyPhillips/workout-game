import random
import math
#TODO m

def next_round():
    selection = random.randint(1, 4) * 2 - 2
    print(selection)
    exercise = current[selection][0].split(" ")[0]
    rep_mult = random.randint(min_mult*100, max_mult*100)/100
    print(rep_mult)
    if rep_mult > 1:
        print("Set record attempt\n")
    reps = rep_mult * records[selection][1]
    if reps <= 1:
        print("Set record attempt\n")
        reps = random.randint(1, 5)
    reps = math.ceil(reps)
    valid_input = False
    print(exercise + " " + str(reps) + " reps")
    while valid_input == False:
        print("Type 'y' if you completed the set, type 'n' if you didn't")
        complete = str(input())
        if complete == "y" or complete == "n":
            valid_input = True
    if complete == "y":
        current[selection + 1][1] += reps
        if reps > current[selection][1]:
            current[selection][1] = reps
            if current[selection][1] > records[selection][1]:
                records[selection][1] = current[selection][1]
        if current[selection + 1][1] > records[selection + 1][1]:
            records[selection + 1][1] = current[selection + 1][1]
        print(records)
        print(current)
        next_round()
    else:
        recordFile = open("workout-records.txt", "w")
        for item in records:
            recordFile.write(f"{item[0]}: {item[1]}\n")

recordFile = open("workout-records.txt", "a+")
recordFile.seek(0)
if not (recordFile.read(1)):
    recordFile.write("Push-ups set: 0\nPush-ups total: 0\nPull-ups set: 0\nPull-ups total: 0\nChin-ups set: 0\n")
    recordFile.write("Chin-ups total: 0\nDips set: 0\nDips total: 0\n")
records = []
recordFile.seek(0)
for line in recordFile:
    segment = line.split()
    name = ' '.join(segment[0:2]).replace(':', '')
    number = int(segment[-1])
    records.append([name, number])
print(records)
current = [[item[0], 0] for item in records]
#print("For the following multipliers respond with a decimal. Ex: .25\n")
#print("Minimum multiplier: ")
min_mult = .25 #float(input())
#print("Maximum multiplier: ")
max_mult = 1.25 #float(input())
print(current)
next_round()

recordFile.close()

