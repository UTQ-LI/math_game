class Control_Problem:
    def control_equation(self, user_answer, question):
        global cozum
        global cozum_
        parcalar = question.split()
        katsayi = int(parcalar[0].replace("x", ""))
        isaret = parcalar[1]
        sabit = int(parcalar[2])
        sonuc = int(parcalar[4])

        if isaret == "+":
            cozum = (sonuc - sabit) / katsayi
            cozum_ = round(cozum, 2)
        elif isaret == "-":
            cozum = (sonuc + sabit) / katsayi
            cozum_ = round(cozum, 2)
        elif isaret == "*":
            if katsayi != 0 and sabit != 0:
                cozum = sonuc / (katsayi * sabit)
                cozum_ = round(cozum, 2)
            else:
                return False
        elif isaret == "/":
            if sabit != 0:
                cozum = sonuc * (katsayi / sabit)
                cozum_ = round(cozum, 2)
            else:
                return False

        if user_answer == cozum or user_answer == cozum_:
            return True
        else:
            print(f"Doğru cevap: {cozum_}")
            return False

    def control_problem(self, user_answer, random_problem_question):
        correct_answer = eval(random_problem_question)
        correct_answer_ = round(correct_answer, 2)

        if user_answer == correct_answer or user_answer == correct_answer_:
            return True
        else:
            print(f"Doğru cevap: {correct_answer_}")
            return False

    def control(self, user_answer, question, type):
        if type == 1:
            return Control_Problem().control_equation(user_answer, question)
        elif type == 2:
            return Control_Problem().control_problem(user_answer, question)
        else:
            print("Bir hata ile karşılaşıldı!")