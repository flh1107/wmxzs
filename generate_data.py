import json

# 重复次数
n = 100
 
# 读取 JSON 文件
with open('trade20240124-train-Copy1.jsonl', 'r') as f:
    data = json.load(f)
    #print (data)
    new_data=[]
    
    for item in data:
        for i in range(n):
            new_data.append(item)
            #print(item)
           

    with open('trade20240124-train.jsonl', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
