import math

def calculate_partner_capacity(percentage_dict, total_packages):
    capacity_dict = {}

    for partner, percentage in percentage_dict.items():
        capacity = math.ceil((percentage / 100) * total_packages)
        capacity_dict[partner] = capacity

    return capacity_dict


