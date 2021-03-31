def get_code_dict(items):
    return {item.get("code") : True for item in items}

def get_intersection(item_dict1, item_dict2):
    itersection = 0
    for code in item_dict1.keys():
        if (code in item_dict2):
            itersection += 1
            
    return itersection