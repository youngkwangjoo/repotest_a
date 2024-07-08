import os
import psutil

# 현재 파이썬 프로그램의 PID 가져오기
current_pid = os.getpid()


for i in psutil.process_iter(attrs = ["pid","name"]):
    info = i.info
    if info["pid"] == current_pid:
        print(info["name"])
        break