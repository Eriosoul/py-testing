citizens = [('Steve', 10), ('Mark', 6), ('Chris', 5)]


def tax(citizens):
    name = citizens[0]
    taxed_balce = citizens[1]*0.93
    return (name, taxed_balce)


taxed_citizones = []
for citizen in citizens:
    taxed_citizen = tax(citizen)
    taxed_citizones.append(taxed_citizen)

print(taxed_citizones)


# now using map
citizens = [('Steve', 10), ('Mark', 6), ('Chris', 5)]


def tax(citizens):
    name = citizens[0]
    taxed_balce = citizens[1]*0.93
    return (name, taxed_balce)


taxed_citizones = list(map(tax, citizens))

print(taxed_citizones)