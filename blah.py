from package_priority import WeightPriority
from partner_priority import dest_prior
from percentage_cap_user_per_slug import calculate_percentage
from capacity_per_slug import get_shipment_counts_for_user
from destpin_slug_user_count import create_dictionary_for_user
from no_of_pacakges_per_slug import calculate_partner_capacity
from Matching import boston_mechanism_with_capacity
from data_consolidation import merge_csv_files
import csv
import pandas as pd

# Prompt the user to input user id
id = input("Enter user id: ")

# Prompt the user to input package information
print("Enter package information (package name, weight, destination pin):")
package_dict = {}
for i in range(1, 11):  # Assuming 10 packages
    package_name = input(f"Package {i} name: ")
    weight = float(input(f"Package {i} weight: "))
    destination_pin = input(f"Package {i} destination pin: ")
    package_dict[package_name] = (weight, destination_pin)

csv_file_path = 'D:\Eshipz\AI_LOAD_DATA\CODE\data.csv'
destpin_count_per_slug_per_user = create_dictionary_for_user(csv_file_path, id)

prior_list = dest_prior(destpin_count_per_slug_per_user, package_dict)
partner_pref = {}
for i in prior_list.keys():
    partner_pref[i] = [j[0] for j in prior_list[i]]
for i in package_dict.keys():
    for j in partner_pref.keys():
        if i not in partner_pref[j]:
            partner_pref[j].append(i)

package_weight = {}
for i in package_dict.keys():
    package_weight[i] = package_dict[i][0]

df = pd.read_csv(csv_file_path)
weight_priority = WeightPriority(df)
package_pref = weight_priority.calculate_priority_list(id, package_weight)

user_shipment_counts = get_shipment_counts_for_user('D:\Eshipz\AI_LOAD_DATA\CODE\data.csv', id)
capacity_percent = calculate_percentage(user_shipment_counts)
total_packages = len(package_dict.keys())
partner_capacity = calculate_partner_capacity(capacity_percent, total_packages)

matching = boston_mechanism_with_capacity(package_pref, partner_pref, partner_capacity)
print(matching)
