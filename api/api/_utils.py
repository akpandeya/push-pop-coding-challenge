def get_code_dict(items : list[dict]) -> dict:
    return {item.get("code") : True for item in items}

def get_intersection(item_dict1 : dict, item_dict2 : dict) -> int:
    itersection = 0
    for code in item_dict1.keys():
        if (code in item_dict2):
            itersection += 1
            
    return itersection