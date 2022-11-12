import random


with open('Test_find_1.csv', 'w') as f:
    line_number = 0

    def check(num_check):
        if num % 50 == 0:
            f.write("\n")
        else:
            pass


    text = random.randint(1, 9998)
    num = 0

    for i in range(1, 10001):
        if num == text:
            f.write("2")
            num += 1
        else:
            f.write("1")
            num += 1
        check(num)



with open('Test_find_1.csv', 'r') as f2:




    for num, line in enumerate(f2, 1):
        r = 0
        if "2" in line:
            for l in line:
                if l == "2":
                    break
                else:
                    r += 1

            print(f'found at line: {num} and Row {r + 1}')


