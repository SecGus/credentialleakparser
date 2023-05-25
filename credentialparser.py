import json, hashlib

def process_json(json_data):
    data = json.loads(json_data)
    dupe_check = []
    result = []
    for website in data:
        try:
            users = data[website]
            for user in users:
                dupe_check.append(hashlib.md5(str.encode(user['password'])).hexdigest())
            for user in users:
                email = user['email_address']
                password = user['password']
                if password not in dupe_check:
                    result.append(f"{email}:{password}")
                else:
                    print("Dupe removed "+password)
        except:
            continue
    return result

file_path = 'leak.json'  # Path to the JSON file
with open(file_path, 'r') as file:
    json_data = file.read()

formatted_data = process_json(json_data)
for item in formatted_data:
    print(item)
