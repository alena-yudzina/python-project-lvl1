from ..game_logic import start_game
import random
import prompt


def randomize():
    operations = ['+', '-', '*']
    random_number_1 = random.randint(0, 100)
    random_number_2 = random.randint(0, 100)
    random_operation = random.choice(operations)
    params = {
        'num_1': random_number_1,
        'num_2': random_number_2,
        'operation': random_operation
    }
    return params


def game_task():
    return 'What is the result of the expression?'


def ask(params):
    return prompt.string(f"Question: {params['num_1']} {params['operation']}"
                         f" {params['num_2']}\nYour answer: ")


def correct_answer(params):
    expression = f"{params['num_1']} {params['operation']} {params['num_2']}"
    return str(eval(expression))


def main():
    start_game(randomize, game_task, ask, correct_answer)


if __name__ == "__main__":
    main()
