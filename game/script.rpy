
# 게임 만들기
# 장르 : 잡탕
# 

init:
    python:
        renpy.music.register_channel("music2", mixer="Sfx")

    # -----------날짜---------------

    define year = 100
    define month = 1
    define day = 1

    #-----------------------------
    define level = 1
    define title = "어린이"

    define date_who = ""

    # ----------능력-----------------
    #체력
    define phy = 10
    #힘
    define string = 5
    #지능
    define itl = 5
    #기품
    define grace = 0
    #매력
    define fashion = 0
    #도덕성
    define ethics = 0 
    #신앙
    define religion = 0
    #업보
    define karma = 0
    #감수성
    define sens = 0

    # -------------신체/나이/돈/스트레스----------------

    define height = 160
    define weight = 50
    define age = 8
    define money = 500
    define stress = 0

    define chance = 0

    define test = 0

    define speed = 0    

    #캐릭터
    define elf = Character("엘프레다" , color="#FF9E9B") # 엘프레다
    define graf = Character("포도버섯") # 포도버섯(매니저)
    define sare = Character("사레보그") # 사레보그(매니저)
    define gum = Character("굼벵이") # 광속굼벵이(잡탕)
    define star = Character("별선비") # 별선비(마요이)
    define maijju = Character("마이쮸") # 마이쮸()
    define gam = Character("감성") # 감성

    define king = Character("국왕" , color="#FF9E9B") # 국왕

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

screen set_name(title, init_name):
    frame: 
        xpadding 50 
        ypadding 50 
        xalign 0.5  yalign 0.5 
        vbox: 
            spacing 20 
            text title xalign 0.5 
            input default init_name xalign 0.5

screen set_age(title, init_age):
    frame: 
        xpadding 50 
        ypadding 50 
        xalign 0.5  yalign 0.5 
        vbox: 
            spacing 20 
            text title xalign 0.5 
            input default init_age xalign 0.5            



label start:

    scene bg broadcast with dissolve

    elf "오늘은 프린세스 메이커를 할거에요"

    elf "오늘도 트수 넣어서 시작할거니깐 그렇게 아세요"

    "엘프레다 방송."

    "노래면 노래 애교면 애교"

    "만만치 않은 매력을 소유한 스트리머다."

    "노래컨텐츠도 게임 컨텐츠도 하는 종합 스트리머라고 할 수 잇엇다."

    elf "그럼 게임 시작할게요"

    "왕국력 13세기"

    "왕국은 부유하고 거대해졌지만 하늘의 제사를 지내지 않자"

    "분노한 천제는 마왕에게 명령을 내려 왕국은 전쟁에 휘말리게 됬다"

    "평화에 길들여진 왕국은 멸망의 위기에 닥치게 되는데.."

    "그 때 용사가 마왕군을 몰살 시키며 등장한다."

    "결국엔 마왕을 물리치는데 성공하고 전쟁을 끝을 낸다."

    "용사여.. 짐과 함께 왕국을 재건하지 않겟는가.."

    

    #캐릭터 이름 입력받을꺼야 
    $ player_name = renpy.call_screen("set_name",title=" 딸의 이름은? ", init_name="") 
    $ p = Character(player_name, color="#7300a0")

    p "이름 : [player_name]"

    #캐릭터 이름 입력받을꺼야 
    $ player_age = renpy.call_screen("set_age",title=" 딸의 나이는? ", init_age="") 
    
    p "나이 : [player_age]"
    
    "(소곤소곤) 절대 개발자가 달력 만들기 귀찮아서 나이로 처리하는 거 아님."

    ""    



