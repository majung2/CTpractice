# 상담타입
import json

def get_summary(data,target_value):
    json_data = json.loads(data)
    summary = []
    
    for Type in json_data:
        if Type["value"] == target_value:
            pk = Type["pk"]
						
    for _ in range(3):
        for Type in json_data:
            if Type["pk"] == pk:
                if Type["is_active"]:
                    summary.insert(0,Type["value"])
                    pk = Type["parent"]
                    break
                else:
                    return "INACTIVE"
        if not pk:
            break
    while(pk):
        for Type in json_data:
            if Type["pk"] == pk:
                if not Type["is_active"]:
                    return "INACTIVE"
                else:
                    pk = Type["parent"]

            
    return '>'.join(summary)
    
data, target_value = map(str,input().split('/'))
print(get_summary(data,target_value))