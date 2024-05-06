import time

class Log:
    def addLog(self, user, question, useranswer, controlProblem):
        if controlProblem:
            controlProblem = "Soruyu Doğru Yaptı"
        else:
            controlProblem = "Soruyu Yanlış Yaptı"

        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec

        with open("logs.txt", "a") as logFile:
            logFile.write(f"Saat: {hour} Dakika:{minute} Saniye:{second} '{user}' Soru: '{question}' Verilen Cevap: {useranswer} {controlProblem}\n")

        logFile.close()