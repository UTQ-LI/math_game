import random, time, platform, os
from generate_problem import Generate_Problem
from control_problem import Control_Problem
from score import UserScore

UserScore = UserScore()
generate_problem = Generate_Problem()
control_problem = Control_Problem()

class Main:
    def clearConsole(self, platform):
        if platform == "Windows":
            os.system("cls")
        elif platform == "Linux" or platform == "Linux2" or platform == "Darwin":
            os.system("clear")
        else:
            print("[!] Bilinmeyen bir işletim sistemi!")
            exit()

    def addUser(self, user):
        UserScore.AddUser(user)

    def start_game(self):
        for user in UserScore.ListUsers():
            question_type = random.randint(1, 2)
            if question_type == 1:
                question = generate_problem.generate_equation()
            elif question_type == 2:
                question = generate_problem.generate_problem()
            else:
                print("Bir hata ile karşılaşıldı!")
                exit()

            print(f"{user} sorusu")
            time.sleep(1)
            print(f"Soru: {question}")

            user_input = input("Cevabınız: ")

            if user_input in ["exit", "quit", "e", "q"]:
                Main.clearConsole(platform)
                print("Çıkış yapılıyor...")
                time.sleep(1)
                exit()

            elif user_input in ["list_score", "score", "skor", "skoru listele", "list skor", "list score"]:
                Main.clearConsole(platform)
                print(UserScore.UserScoreLists())
                time.sleep(2)
                break

            else:
                user_input = float(user_input)
                controlProblem = control_problem.control(user_input, question, question_type)
                if controlProblem:
                    print(f"{user} doğru cevap verdi!")
                    UserScore.AddScoreUser(user, 1)
                else:
                    print(f"{user} yanlış cevap verdi!")
                    UserScore.DeleteScoreUser(user, 1)

Main = Main()


platform = platform.system()

Main.clearConsole(platform)
print("Matematik Oyununa Hoşgeldiniz!")
time.sleep(1)
while True:
    option = int(input("1: Kullanıcı ekle\n 2: Oyuna başla\nBir seçenek seçin: "))

    if option == 1:
        username = input("Lütfen eklenecek ismi giriniz (iptal için 'iptal' yazmanız yeterli!): ")
        if username == "iptal":
            print("İptal edildi!")
        else:
            Main.clearConsole(platform)
            Main.addUser(username)

    elif option == 2:
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        Main.clearConsole(platform)
        print("Oyun Başlıyor!")
        Main.clearConsole(platform)
        time.sleep(1)
        while True:
            Main.start_game()
    else:
        print("Geçersiz seçenek seçtiniz!")
        exit()

# kullanıcıların skorları kaybolmaması için bir text dosyayı ayarlanacak