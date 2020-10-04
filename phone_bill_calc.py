import math

class bill():

    def bill_calculator(self):
        min_free = 500

        cost_month = 300
        cost_per_min = 0.50
        taxes = 5

        min_used = int(input("how much mins was telephone used"))
        if min_used < min_free:
            taxes = cost_month * 5 / 100
            monthly_bill = cost_month + taxes

        else:
            extra_usage = min_used - min_free
            print(extra_usage)
            extra_cost = extra_usage * cost_per_min
            taxes = (cost_month + extra_cost) * 12.5 / 100
            monthly_bill = cost_month + extra_cost + taxes

        print("ur monthly bill is: ", monthly_bill)


bill.bill_calculator(0)
