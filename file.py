salary = 6900
veg_sale = 0.7
cucumber = 90
tomato = 150
cookies = 140 + 140 
buy =(cucumber * 5+ tomato * 4) * veg_sale + cookies
left = salary - buy 
print(f" у таксиста Вани было {salary} рублей, после траты {buy} рублей у него осталось {left} рублей")

stock = 134.65
travel = 36


print(f"таксист Ваня сможет купить {left//stock} акций")
print(f"уВани останется {int(left% stock)} рублей,когда проезд стоит{travel} рублей")



number = int(input("видите число :"))
third = number % 10
first = number //100
second = number//10 % 10
print(f"сумма цифр{number} = {first + second + third}")


print("this is the end")
