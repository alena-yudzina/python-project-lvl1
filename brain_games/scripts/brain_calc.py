from ..cli import welcome_user
import random
import prompt


def is_right(answer, random_number_1, random_number_2, random_operation):
    flag = True
    expression = f"{random_number_1} {random_operation} {random_number_2}"
    if answer != str(eval(expression)):
        flag = False
    return flag


def correct_answer(random_number_1, random_number_2, random_operation):
    expression = f"{random_number_1} {random_operation} {random_number_2}"
    return str(eval(expression))


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    result = f"Congratulations, {name}!"
    operations = ['+', '-', '*']
    for i in range(3):
        random_number_1 = random.randint(0, 100)
        random_number_2 = random.randint(0, 100)
        random_operation = random.choice(operations)
        answer = prompt.string(f"Question: {random_number_1} {random_operation}"
                               f" {random_number_2}\nYour answer: ")
        if not (is_right(answer, random_number_1,
                         random_number_2, random_operation)):
            result = f"Let's try again, {name}!"
            correct_ans = correct_answer(random_number_1,
                                         random_number_2, random_operation)
            print(f'"{answer}" is wrong answer ;(. Correct answer was '
                  f'"{correct_ans}"')
            break
        else:
            print('Correct!')
    print(result)


if __name__ == "__main__":
    main()
