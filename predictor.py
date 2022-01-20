from random import randint

global new
global thread_value
global values
global dict_triad
global num
global money_left

thread_value = ['000', '001', '010', '011', '100', '101', '110', '111']
values = {0: 0, 1:0}
dict_triad = dict.fromkeys(thread_value, values)
num = 100
money_left = 1000


def count_set(sub_str, main_str):
    count = 0
    start = 0
    while start < len(main_str):
        pos = main_str.find(sub_str,start)
        if pos != -1:
            start = pos + 1
            count = count + 1
        else:
            break
    return count


def count_no(sub_str, main_str):
    values = {0: 0, 1: 0}
    new_string = str(sub_str) + '0'
    no_of_times = count_set(main_str=main_str, sub_str=new_string)
    values[0] = no_of_times
    new_string = str(sub_str) + '1'
    no_of_times = count_set(main_str=main_str, sub_str=new_string)
    values[1] = no_of_times

    return values


def random_generator(new, s0 = '0', s1 = '1'):
    total_zeroes = new.count(s0)
    total_ones = new.count(s1)
    if s1 > s0:
        return s0
    else:
        return s1

def predict_module(sub_str,traid_values):
    no_of_zeroes = traid_values[sub_str][0]
    no_of_ones = traid_values[sub_str][1]
    if no_of_ones > no_of_zeroes:
        return '1'
    elif no_of_ones < no_of_zeroes:
        return '0'
    else:
        return str(randint(0,1))


def preposseing_data():
    global new
    new = ""
    while len(new) < num:
        print("Current data length is "+str(len(new))+", "+str(num - len(new))+" symbols left")
        print("Print a random string containing 0 or 1: ")
        n = input()
        old_list = list(x for x in n)
        length = len(n)
        i = 0
        while i < length:
            if old_list[i] == '0' or old_list[i] == '1':
                new = new + old_list[i]
            i = i + 1
    print("Final data string:")
    print(new)

def training_model():
    global dict_triad, values, new, thread_value
    for i in range(len(thread_value)):
        values = count_no(sub_str=thread_value[i], main_str=new)
        dict_triad[thread_value[i]] = values

def calculate_score(correct_ans, total_ans):
    global money_left
    money_left = money_left - correct_ans
    total_ans = total_ans - correct_ans
    money_left = money_left + total_ans


def packaging_data(n):
    global new
    old_list = list(x for x in n)
    length = len(n)
    i = 0
    while i < length:
        if old_list[i] == '0' or old_list[i] == '1':
            new = new + old_list[i]
        i = i + 1
    training_model()


def testing_model(testing_value):
    global new, dict_triad
    result = random_generator(new=new)
    result = random_generator(new=new, s0=result+'0', s1=result+'1')
    result = random_generator(new=new,s0=result+'0', s1=result+'1')

    no_of_correct = 0

    i = 0
    j = 3
    while j < len(testing_value):
        result = result + str(predict_module(sub_str=testing_value[i:j], traid_values=dict_triad))
        if result[j] == testing_value[j]:
            no_of_correct = no_of_correct + 1
        i = i + 1
        j = j + 1

    print("prediction:")
    print(result)

    correct_percent = (no_of_correct / (len(testing_value) - 3)) * 100
    correct_percent = format(correct_percent)
    print("\nComputer guessed right", no_of_correct, "out of", (len(testing_value) - 3),"symbols", end=" ")
    print("( "+"{:.2s}".format(correct_percent)+" %)")
    calculate_score(correct_ans=no_of_correct,total_ans=(len(testing_value) - 3))
    print("Your balance is now $"+str(money_left))
    packaging_data(testing_value)


print("Please give AI some data to learn...")
preposseing_data()
training_model()
print("\nYou have $1000. Every time the system successfully predicts your next move, you lose $1.")
print("Otherwise, you earn $1, Print \"enough\" to leave the game")
print("Let's go")

print("Print a random string containing 0 or 1:")
test_input = input()
while(test_input != "enough" and money_left > 0):
    if (test_input.isdecimal() == True ):
        testing_model(testing_value=test_input)

    print("Print a random string containing 0 or 1:")
    test_input = input()
    test_input = test_input.lower()

print("Game over!")
