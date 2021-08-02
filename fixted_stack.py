#-*- coding: cp949 -*-
#-*- coding: utf-8 -*-

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum("Menu", ["푸시","팝","피크","검색","덤프","종료"])

def select_menu() -> Menu:
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep = "  " , end = "")
        n = int(input(":"))
        if 1 <=n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True:
    print(f"현재 데이터 개수: {len(s)}/{s.capacity}")
    menu = select_menu()

    if menu == Menu.푸시:
        x = int(input("데이터를 입력하세요:"))
        try:
            s.push(s)
        except FixedStack.Full:
            print("스택이 가득 차있습니다")
        
    elif menu == Menu.팝:
        try:
           x= s.pop()
        except FixedStack.Empty:
            print("스택이 비어있습니다")

    elif menu == Menu.피크:
        try:
            x=s.peek()
            print(f"피크한 데이터는 {x}입니다")
        except FixedStack.Empty:
            print("스택이 비어있습니다")
    
    elif menu == Menu.검색:
        x = int(input("검색할 값을 입력하세요"))
        if x in s:
            print(f"검색한값은 {s.count(x)}개 이고 처음 위치는 {s.find(x)}입니다")
        else:
            print("검색값을 찾을 수 없습니다")

    elif menu == Menu.덤프:
        s.dump()

    else:
        break
