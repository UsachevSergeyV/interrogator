#переконвертация первично загруженных данных

import json
for x in range(1,337):
    with open(f"../logs/data_{x}.json", 'r', encoding='utf-8') as f:
        fl = json.load(f)
        with open(f'../logs/data{x}.json', 'w', encoding='utf-8') as fileForSave:
            json.dump(fl, fileForSave, ensure_ascii=False)