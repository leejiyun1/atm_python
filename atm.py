balance = 3000


while True:
    num = input("사용하실 서비스 번호를 입력해주세요.(1.입금, 2.출금 3.영수증 보기 4.종료)")

    if num == "1":
        print("입금기능입니다.")  
        deposit_amount = input("입금하실 금액을 입력해주세요")
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            balance += int(deposit_amount)
            print(f"{deposit_amount}을 입금했고 잔액은 {balance}입니다.")

        else:
            print("정신차려 이 각박한 세상속에서!")

    if num == "2":
        withdraw_amount = input("출금하실 금액을 입력해주세요")
        if withdraw_amount.isdigit() and int(withdraw_amount) > 0:
            withdraw_amount = min(balance, int(withdraw_amount))
            balance -= int(withdraw_amount)
            print(f"{withdraw_amount}을 출금했고 잔액은 {balance}입니다.")

        else:
            print("정신차려 이 각박한 세상속에서!")

    if num == "3":
        pass

    if num == "4":
        print("종료합니다.")
        break

