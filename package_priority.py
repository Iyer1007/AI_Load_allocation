import csv
import pandas as pd

class WeightPriority:
    def __init__(self, df):
        self.df = df

    def csv_to_dict_for_user(self, user_id):
        slug_weight_ranges = {}
        user_data = self.df[self.df['user_id'] == user_id]
        for _, row in user_data.iterrows():
            slug = row['slug']
            weight = float(row['entered_weight'])
            if slug in slug_weight_ranges:
                min_weight, max_weight = slug_weight_ranges[slug]
                if weight < min_weight:
                    min_weight = weight
                elif weight > max_weight:
                    max_weight = weight
                slug_weight_ranges[slug] = (min_weight, max_weight)
            else:
                slug_weight_ranges[slug] = (weight, weight)
        return slug_weight_ranges

    def csv_to_weight_dict_for_user(self, user_id):
        weight_dict = {}
        user_data = self.df[self.df['user_id'] == user_id]
        for _, row in user_data.iterrows():
            slug = row['slug']
            weight = float(row['entered_weight'])
            if slug in weight_dict:
                weight_dict[slug].append(weight)
            else:
                weight_dict[slug] = [weight]
        return weight_dict

    def weight_list(self, wrange, weight, slug_weights):
        ran = []
        priority_list = []
        for i in wrange.keys():
            ran.append(abs(wrange[i][0] - weight))
            ran.append(abs(wrange[i][1] - weight))
        ran = sorted(ran)
        i = 0
        while len(priority_list) != len(wrange.keys()):
            new_lower = max(weight - ran[i], 0)
            new_upper = weight + ran[i]
            slug_count = {}
            for j in slug_weights.keys():
                if j not in priority_list:
                    if j not in slug_count.keys():
                        slug_count[j] = 0
                    for k in slug_weights[j]:
                        if new_lower <= k <= new_upper:
                            slug_count[j] += 1
            sorted_weights = sorted(slug_count.items(), key=lambda x: x[1], reverse=True)
            ordered_list = [item[0] for item in sorted_weights]
            for m in ordered_list:
                if slug_count[m] != 0:
                    priority_list.append(m)
            i += 1
        return priority_list

    def calculate_priority_list(self, user_id, weights):
        slug_weight_ranges = self.csv_to_dict_for_user(user_id)
        slug_weights = self.csv_to_weight_dict_for_user(user_id)
        priority_lists = {}
        for weight_id, weight in weights.items():
            priority_list = self.weight_list(slug_weight_ranges, weight, slug_weights)
            priority_lists[weight_id] = priority_list
        return priority_lists
