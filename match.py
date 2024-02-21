salary = float(input("enter the salary : "))
match salary:
    case salary if salary <= 50000:
        print("low income tax is to be paid")
    case salary if salary > 50000 and salary <=100000:
        tax=salary*0.28
        print("medium income tax is to be paid",round(tax,2))
    case _:
        tax=(salary-50001)*0.3+579
        print("high income tax is to be paid ",round(tax,2))
    
