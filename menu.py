# 랜덤으로 오늘의 점심메뉴를 추천해주는 프로그램
import random

# [] : 배열, 다수의 요소들을 한데 묶는 큰 틀과 같은 역할.
menu = ['새마을식당','초원삼겹살','멀캠20층','홍콩반점','Subway','순남시래기']

phone_book = {
    '새마을식당':'010-1234-1234',
    '초원삼겹살':'02-00-0000',
    '멀캠20층':'걸어가서확인하시오',
    '홍콩반점':'00-000-*0000', 
    'Subway':'0231-1564-4444',
    '순남시래기':'0235-645-1345'
}
print(phone_book['새마을식당'])
# menu의 요소 중 랜덤으로 골라서 lunch라고 하는 변수에 담아주세요.
# 랜덤으로 고른 식당과, 해당 식당의 전화번호를 같이 출력해주세요.
lunch = random.choice(menu)
print(lunch)
print(phone_book[lunch])
