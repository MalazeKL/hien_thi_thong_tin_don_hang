money = int(input("số tiền của bạn đã chi: "))
if money >= 150:
    print("nếu bạn chi ", money, "$ thì bạn chỉ trả", money-50, "$")
elif money >= 100:
    print("nếu bạn chi ", money, "$ thì bạn chỉ trả", money-25, "$")
elif money >= 75:
    print("nếu bạn chi ", money, "$ thì bạn chỉ trả", money-15, "$")
else:
    print("nếu bạn chi ", money, "bạn không được giảm. Tức bạn phải trả ", money)
