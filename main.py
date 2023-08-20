import random
import math


def main():
    global records, recordFile, current, min_mult, max_mult, num_lines
    recordFile = open("workout-records.txt", "a+")
    recordFile.seek(0)
    if not (recordFile.read(1)):
        recordFile.write("Push-ups set: 0\nPush-ups total: 0\nPull-ups set: 0\nPull-ups total: 0\nChin-ups set: 0\n")
        recordFile.write("Chin-ups total: 0\nDips set: 0\nDips total: 0\n")
    num_lines = 0
    records = []
    recordFile.seek(0)
    for line in recordFile:
        num_lines += 1
        segment = line.split()
        name = ' '.join(segment[0:2]).replace(':', '')
        number = int(segment[-1])
        records.append([name, number])

    printStats(records)
    current = [[item[0], 0] for item in records]
    # print("For the following multipliers respond with a decimal. Ex: .25\n")
    # print("Minimum multiplier: ")
    min_mult = .25  # float(input())
    # print("Maximum multiplier: ")
    max_mult = 1.25  # float(input())
    printStats(current)
    num_lines = int(num_lines / 2)
    next_round()
    recordFile.close()


def writeToFile():
    global recordFile
    recordFile = open("workout-records.txt", "w")
    for item in records:
        recordFile.write(f"{item[0]}: {item[1]}\n")


def printStats(type):
    if type == records:
        print("Records")
    elif type == current:
        print("Current Session")
    w_per_line = 6
    for i in range(num_lines // w_per_line):
        print(type[i*w_per_line:i*w_per_line+w_per_line])
    typeMod = num_lines % w_per_line
    if typeMod != 0:
        print(type[-abs(typeMod):])


def next_round():
    global current
    selection = random.randint(1, num_lines) * 2 - 2

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
        writeToFile()


if __name__ == "__main__":
    main()

