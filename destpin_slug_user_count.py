import csv
def create_dictionary_for_user(file_path, user_id):
    user_data = {}

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['user_id'] != user_id:
                continue

            slug = row['slug']
            destpin = row['destpin']

            if slug not in user_data:
                user_data[slug] = {}

            if destpin not in user_data[slug]:
                user_data[slug][destpin] = 1
            else:
                user_data[slug][destpin] += 1

    return user_data
