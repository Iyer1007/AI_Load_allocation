def calculate_percentage(shipment_counts):
    total_shipments = shipment_counts['shipment_count'].sum()
    percentage_dict = {}

    for index, row in shipment_counts.iterrows():
        slug = row['slug']
        count = row['shipment_count']
        percentage = round((count / total_shipments) * 100)
        percentage_dict[slug] = percentage

    return percentage_dict


