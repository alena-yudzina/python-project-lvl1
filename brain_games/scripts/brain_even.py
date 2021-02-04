from ..cli import welcome_user
import random
import prompt


def is_right(answer, random_number):
    flag = True
    if answer == 'yes' and random_number % 2 != 0:
        flag = False
    if answer == 'no' and random_number % 2 == 0:
        flag = False
    if answer not in ['yes', 'no']:
        flag = False
    return flag


def correct_answer(random_number):
    if random_number % 2 != 0:
        return 'no'
    return 'yes'


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    result = f"Congratulations, {name}!"
    for i in range(3):
        random_number = random.randint(0, 100)
        answer = prompt.string(f"Question: {random_number}\nYour answer: ")
        if not (is_right(answer, random_number)):
            result = f"Let's try again, {name}!"
            print(f'"{answer}" is wrong answer ;(. Correct answer was '
                  f'"{correct_answer(random_number)}"')
            break
        else:
            print('Correct!')
    print(result)


if __name__ == "__main__":
    main()
