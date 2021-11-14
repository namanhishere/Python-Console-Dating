import os
import time
def _clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


code = open("code.txt", "r").read()
arr = code.split("\n")


input()
_clrscr()

for line in arr:
    if(line.startswith("[(fx)]")):
        func_code = line[6:len(line)]
        if(func_code == "clear"):
            print(func_code)
            _clrscr()
        elif(func_code.startswith("delay")):
            try:
                time.sleep(float(line[-1]))
            except: 
                print("Đã có lỗi xảy ra khi biên dịch code function")
        
    else:
        print(line)
        time.sleep(0.2)
    

input()
