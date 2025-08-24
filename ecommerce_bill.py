def ecommerce(*args,**kwargs):
    total=0.00
    delivery_fee = 500.00
    
    platform_fee=200.00
    print("=========================================================")
    print("Your Orders")
    print("=========================================================")
    print(f"{'Food item':<20}{'Quantity':^20}{'Price per plate':^20}")
    for arg in args:
        print(f"{arg[0]:<20}{arg[1]:^20}{arg[2]:>15}")
        total+=(arg[1]*arg[2])
    print("=========================================================")
    print("Bill Summary")
    print("=========================================================")
    print(f"{'Item total:':<30} {total:>25}")
   
    if total>2000:
        delivery_fee=0.00
        print("(Congratulations you unlocked free delivery!)")
    print(f"{'Delivery fee:':<30} {delivery_fee:>25}")
    total+=delivery_fee

    print(f"{'Gst and restaurent charges:':<30} {(total*50)/100:>25}")
    total=(total+(total*50)/100)

    print(f"{'Platform fee:':<30} {platform_fee:>25}")
    total+=platform_fee

    if "payment_mode" in kwargs:
        print("--------------------------------------------------------")
        print(f"{'Payment mode:':<30} {kwargs.get('payment_mode'):>25}")
        if kwargs.get("payment_mode")=="card":
            total-=200
            print(f"{'Card payment discount:':<30} {200:>25}")
        elif kwargs.get("payment_mode")=="upi":
            total-=100
            print(f"{'UPI payment discount:':<30} {100:>25}")
    print("--------------------------------------------------------")
    print(f"{'Total Bill:':<30} {total:>25}")

ecommerce(("Vadapav",2,200.00),("Pavbhaji",2,500.00),("misal",1,100.00),payment_mode="card")