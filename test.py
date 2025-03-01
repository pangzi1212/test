import json

response = {
    "d": {
        "cargo_type": "cargo_type1",
    },
}

response_str = str(response)
print(response_str)

response_str1 = json.dumps(response)  # 使用json.dumps确保双引号不变成单引号
print(response_str1)

response_str2 = response_str1.replace(" ", "").replace("\n", "")
print(response_str2)
