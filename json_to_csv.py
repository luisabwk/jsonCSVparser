import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    
    csv_data = []

    
    for item in data:
        player_id = item.get("playerId", "")
        login = item.get("login", "")
        player_name = item.get("playerName", "")
        nick_name = item.get("nickName", "")
        email = item.get("email", "")
        status = item.get("status", "")

        
        group_ids = []
        group_names = []
        
        
        if "groups" in item:
            
            for group in item["groups"]:
                group_ids.append(group.get("groupId", ""))
                group_names.append(group.get("groupName", ""))

        
        group_ids_str = ", ".join(map(str, group_ids))
        group_names_str = ", ".join(group_names)

        
        csv_row = {
           
//CHANGE THE STRUCTURE BELO TO REFLECT YOUR FIELD NAMES: 
            "playerId": player_id,
            "login": login,
            "playerName": player_name,
            "nickName": nick_name,
            "email": email,
            "status": status,
            "groupIds": group_ids_str,
            "groupNames": group_names_str
        }
        csv_data.append(csv_row)

    
    headers = [//CHANGE THE STRUCTURE BELO TO REFLECT YOUR FIELD NAMES: 
"playerId", "login", "playerName", "nickName", "email", "status", "groupIds", "groupNames"]

    
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(csv_data)
    
    print(f"CSV File '{csv_file_path}' created.")


json_to_csv('YOUR-JSON-FILE.json', 'YOUR-OUTPUT-CSV-FILE.csv') 