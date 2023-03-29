학점1 = []
학점2 = []

def work():
    학점 = float(input('학점을 입력하세요:'))
    평점 = input('평점을 입력하세요:')
    학점1.append(학점)
    학점2.append(평점)

    print("입력되었습니다.")
    return

def calculate():

    총학점 = sum(학점1)
    제외학점 = 0
    i = 0
    a = 0

    for j in 학점2:
        if j == 'F':
            a += 1
            제외학점 += 학점1[i]
        i += 1

    제출용 = 총학점 - 제외학점
    열람용 = 총학점

    print('제출용: {}학점 (GPA: {:.2f})'.format(int(제출용), float(제출용/(i - a))))
    print('열람용: {}학점 (GPA: {:.2f})'.format(int(열람용), float(열람용/i)))
    return


def main():
    value = 0 #변수 선언후 초기화
    running = True
    while running:
        print("\n작업을 선택하세요.")
        print("1. 입력")
        print("2. 계산")

        value = int(input('해당 번호 입력:'))

        if value == 1:
            work()
        elif value == 2:
            calculate()
            running = False

if __name__ == '__main__': #메인함수 실행
    main()