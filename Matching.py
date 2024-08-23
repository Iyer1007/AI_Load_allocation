def boston_mechanism_with_capacity(package_prefs, partner_prefs, partner_capacity):
    # Initialize assignment dictionaries
    assi_package = {package: 0 for package in package_prefs.keys()}
    assignment_list_partner = {partner: [] for partner in partner_prefs.keys()}

    # Iterate through package preferences
    while any(value==0 for value in assi_package.values()):
      for package, partners in package_prefs.items():
          if assi_package[package]==0:
            for partner in partners:
            # Check if the partner has available capacity
              if partner_capacity[partner] > 0:
                # Assign the package to the partner
                assi_package[package] = partner
                assignment_list_partner[partner].append(package)
                partner_capacity[partner] -= 1
                break
              else:
                max_rank=0
                least_prior=None
                for pac in assignment_list_partner[partner]:
                  if  partner_prefs[partner].index(pac)+1>max_rank:
                    max_rank=partner_prefs[partner].index(pac)+1
                    least_prior=pac
                if partner_prefs[partner].index(package)+1<max_rank:
                  assi_package[package]=partner
                  assi_package[least_prior]=0
                  assignment_list_partner[partner][assignment_list_partner[partner].index(least_prior)]=package
                #print(assignment_list_partner)
                #print(assi_package)
                if assi_package[package]!=0:
                  break

    return assignment_list_partner