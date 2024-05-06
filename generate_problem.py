import random

class Generate_Problem:
    def __init__(self):
        self.operators = ["+", "-", "*", "/"]
        self.question = []

    def generate_problem(self):
        self.question.clear()
        for i in range(4):
            random_number = random.randint(5, 20)
            self.question.append(str(random_number))
            random_operator = random.choice(self.operators)
            self.question.append(random_operator)

        if self.question[-1] in self.operators:
            self.question.pop()

        new_question = ' '.join(map(str, self.question))

        return new_question

    def generate_equation(self):
        operators = ["+", "-", "*", "/"]
        random_operators = random.choice(operators)
        katsayi = random.randint(-10, 10)
        sabit = random.randint(-10, 10)
        sonuc = random.randint(-10, 10)

        denklem = f"{katsayi}x {random_operators} {sabit} = {sonuc}"

        return denklem