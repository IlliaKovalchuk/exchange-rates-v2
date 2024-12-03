def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates["rates"] or to_currency not in rates["rates"]:
        raise KeyError("Currency not found")
    from_rate = rates["rates"][from_currency]
    to_rate = rates["rates"][to_currency]
    return amount * (to_rate / from_rate)