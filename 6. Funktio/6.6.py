def pizza_calculator(d, price):
    d = float(d) / 100
    n = float(d) * 2
    total = float(price) / n
    return total

pizza1d = input("Anna pizzan halkaisija senttimetreinä")
pizza1price = input("Anna pizzan hinta")

pizza2d = input("Anna toisen pizzan halkaisija senttimetreinä")
pizza2price = input("Anna toisen pizzan hinta")

a = pizza_calculator(pizza1d, pizza1price)
b = pizza_calculator(pizza2d, pizza2price)
print(f"Ensimmäisen pizzan hinta per neliömetri on {round(a,2)} euroa \nToisen pizzan hinta per neliömetri on {round(b,2)} euroa")