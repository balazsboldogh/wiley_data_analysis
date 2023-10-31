def coffee_shop():

    size_prices = {"small":2,"medium":3,"large":4}
    type_prices = {"brewed":0,"espresso":0.5,"cold brew":1}
    flavoring_price = 0.5

    size = input("Would you like a small, medium or large cup?").lower()
    coffee_type = input("Would you like brewed, esperesso, or cold brew?").lower()
    flavoring = input ("Would you like some flavoring? (Yes/No)").lower()

    total_cost = size_prices.get(size, 0) + type_prices.get(coffee_type, 0)

    if flavoring == "yes":
        flavor = input("Do you want hazelnut, vanilla, or caramel? ").lower()
        if flavor in ["hazelnut", "vanilla", "caramel"]:
            total_cost += flavoring_price

    tip = 1.15
    total_with_tip = total_cost * tip

    print("You asked for a", size, "cup of", coffee_type, "coffee", end="")
    if flavoring == "yes":
        print(" with", flavor, "syrup.")
    else:
        print(".")
    print("Your cup of coffee costs", round(total_cost, 2))
    print("The price with a", round((tip - 1) * 100), "% tip is", round(total_with_tip, 2))

if __name__ == "__main__":
    coffee_shop()