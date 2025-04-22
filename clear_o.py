import json
def clear_json_file(filepath):
    with open(filepath, 'w') as file:
        json.dump({}, file)  # Write an empty dictionary to the file

clear_json_file('budget_data.json')