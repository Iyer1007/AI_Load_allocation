def dest_prior(destpin_count,package):
  slug_prio_dict={}
  slug_mapped={}
  slug_count={}
  for slug in destpin_count.keys():
    prior=[]
    count_dict={}
    for pack in package.keys():
      try:
        if str(package[pack][1]) in destpin_count[slug].keys() and package[pack][1] not in count_dict.keys():
          count_dict[package[pack][1]]=destpin_count[slug][package[pack][1]]

      except:
          continue
    slug_count[slug]=count_dict
  for slug in slug_count.keys():
    slug_count[slug] = dict(sorted(slug_count[slug] .items(), key=lambda x: x[1], reverse=True))
  for slug in slug_count.keys():
    prior=[]
    pack_l=[]
    for pin in slug_count[slug].keys():
      #pin_l=[]
      for pack in package.keys():
        if package[pack][1]==pin:
          #pin_l.append([pack,package[pack]])
          prior.append([pack,package[pack]])
          pack_l.append(pack)
    slug_mapped[slug]=pack_l
    slug_prio_dict[slug]=prior
  first_digit_pin={}
  for slug in slug_mapped.keys():
    digit_freq_sum = {str(digit): 0 for digit in range(1, 10)}
    for pin, freq in destpin_count[slug].items():
      first_digit = pin[0]
      try:
        if first_digit.isdigit() and int(first_digit) in range(0, 10):
           digit_freq_sum[first_digit] += freq
        first_digit_pin[slug]=dict(sorted( digit_freq_sum .items(), key=lambda x: x[1], reverse=True))
      except:
        continue
  for slug in first_digit_pin.keys():
    for pin in first_digit_pin[slug].keys():
      for pack in package.keys():
        if pack not in slug_mapped[slug]:
          if package[pack][1][0]==pin:
            slug_prio_dict[slug].append([pack,package[pack]])
  return slug_prio_dict

