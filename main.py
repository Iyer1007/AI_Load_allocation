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
print("Enter user id:")
id=input()
package_dict=({
    "package1":(265.33,"110032"),
    "package2":(0.45,"712223"),
    "package3":(30000,"124103"),
    "package4":(6500,"121007"),
    "package5":(110.5,"248001"),
    "package6":(512,"560067"),
    "package7":(10.5,"244901"),
    "package8":(0.1,"122105"),
    "package9":(55,"380015"),
    "package10":(15000,"560041"),
},"2023-08-27")
csv_file_path='D:\Eshipz\AI_LOAD_DATA\CODE\data.csv'
destpin_count_per_slug_per_user = create_dictionary_for_user(csv_file_path, id)
#print(destpin_count_per_slug_per_user)
prior_list=dest_prior(destpin_count_per_slug_per_user,package_dict[0])
partner_pref={}
for i in prior_list.keys():
  partner_pref[i]=[j[0] for j in prior_list[i]]
for i in package_dict[0].keys():
  for j in partner_pref.keys():
      if i not in partner_pref[j]:
        partner_pref[j].append(i)   
package_weight={}
for i in package_dict[0].keys():
  package_weight[i]=package_dict[0][i][0]
df = pd.read_csv(csv_file_path)

weight_priority = WeightPriority(df)

# Calculate priority lists for each weight
package_pref = weight_priority.calculate_priority_list(id, package_weight)


# User ID for which you want to get shipment counts
#userid = "645ce57c0afce0216081e8d4"

# Call the function to get shipment counts for the specified user
user_shipment_counts = get_shipment_counts_for_user('D:\Eshipz\AI_LOAD_DATA\CODE\data.csv', id)
capacity_percent = calculate_percentage(user_shipment_counts)
# Total number of packages
total_packages = len(package_dict[0].keys())  # Example total number of packages

# Calculate partner capacity
partner_capacity = calculate_partner_capacity(capacity_percent, total_packages)
matching = boston_mechanism_with_capacity(package_pref, partner_pref, partner_capacity)
print(matching)