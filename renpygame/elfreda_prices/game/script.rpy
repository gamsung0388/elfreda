
# 게임 만들기
# 장르 : 잡탕
# 

init:
    python:
        renpy.music.register_channel("music2", mixer="Sfx")

    #캐릭터
    define elf = Character("엘프레다" , color="#FF9E9B") # 엘프레다
    define graf = Character("포도버섯") # 포도버섯(매니저)
    define sare = Character("사레보그") # 사레보그(매니저)
    define gum = Character("굼벵이") # 광속굼벵이(잡탕)
    define star = Character("별선비") # 별선비(마요이)
    define maijju = Character("마이쮸") # 마이쮸()
    define gam = Character("감성") # 감성

    #배경    
    image bg broadcast = im.FactorScale("bg/broadcast.jpg", 1.16) # 방송화면
    # image bg prinsses = "" # 프린세스메이커
    # image bg space = "" # 여신 
    # image bg street = "" # 거리
    # image bg trial = "" # 재판 
    # image bg lol = "" # 소환사 협곡     

    #캐릭터
    # image elf = "" # 엘프레다
    # image graf = "" # 포도버섯
    # image sare = "" # 사레보그
    # image gum = "" # 굼벵이
    # image star = "" # 별선비
    # image maijju = "" # 마이쮸
    # image gam = "" # 감성

label start:

    scene bg broadcast with dissolve

    elf "오늘은 프린세스 메이커를 할거에요"

    
    





