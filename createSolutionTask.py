import pygame
import random

def create_solution_task3 (game_level):
    'Returns solveNum_Action, solveNum_1, solveNum_2, solveNum_Result, blind, answer'

    if 0 < game_level <= 3:
        pass
    else:
        game_level = 1

    blind = random.randint(1, 3)
    answer = 0

    # LEVEL 1
    if game_level == 1:
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 9)

        if num1 > num2:
            solveNum_Result = num1
            solveNum_1 = num2
        else:
            solveNum_Result = num2
            solveNum_1 = num1

        if solveNum_Result == 10:
            blind = random.randint(1, 2)
            if solveNum_1 == 0:
                solveNum_1 = 1

        solveNum_2 = solveNum_Result - solveNum_1
        solveNum_Action = "+"

    # LEVEL 2
    if game_level == 2:
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 9)

        if num1 > num2:
            solveNum_1 = num1
            solveNum_Result = num2
        else:
            solveNum_1 = num2
            solveNum_Result = num1

        if solveNum_1 == 10:
            blind = random.randint(2, 3)
            if solveNum_Result == 0:
                solveNum_Result = 1

        solveNum_2 = solveNum_1 - solveNum_Result
        solveNum_Action = "-"

    # LEVEL 3
    if game_level == 3:
        solveNum_Result = random.randint(0, 9)
        solveNum_1 = random.randint(0, 9)

        if solveNum_Result >= solveNum_1:
            solveNum_2 = solveNum_Result - solveNum_1
            solveNum_Action = "+"
        else:
            solveNum_2 = solveNum_1 - solveNum_Result
            solveNum_Action = "-"

    if blind == 1:
        answer = solveNum_1
    elif blind == 2:
        answer = solveNum_2
    else:
        answer = solveNum_Result

    return solveNum_Action, solveNum_1, solveNum_2, solveNum_Result, blind, answer
