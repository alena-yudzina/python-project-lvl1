from ..game_logic import start_game
import random
import prompt


def randomize():
    random_number_1 = random.randint(0, 100)
    random_number_2 = random.randint(0, 100)
    params = {
        'num_1': random_number_1,
        'num_2': random_number_2,
    }
    return params


def game_task():
    return 'Find the greatest common divisor of given numbers.'


def ask(params):
    return prompt.string(f"Question: {params['num_1']} {params['num_2']}"
                         "\nYour answer: ")


def correct_answer(params):
    a = params['num_1']
    b = params['num_2']
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gcd = a + b
    return str(gcd)


def main():
    start_game(randomize, game_task, ask, correct_answer)


if __name__ == "__main__":
    main()
