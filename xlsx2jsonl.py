import openpyxl
import json

def process_excel_to_json(input_file, output_file):
    # Load the workbook
    wb = openpyxl.load_workbook(input_file)

    # Select the "DrugQA" sheet
    sheet = wb["Sheet1"]

    # 重复次数
    n = 1
    
    # Initialize the output data structure
    output_data = []

    # Iterate through each row in column A and D
    for row in sheet.iter_rows(min_row=2, max_col=2, values_only=True):
        system_value = "你是一个专业的、有经验的进出口贸易助手.请尽量根据贸易便利化术语，回答进出口贸易问题。"

        # Create the conversation dictionary
        conversation = {
            "system": system_value,
            "input": row[0].replace(')','）').replace('(','（')+'是什么',
            "output": '根据贸易便利化术语，'+row[0].replace(')','）').replace('(','（')+'是'+row[1].replace(')','）').replace('(','（')
        }

        # Append the conversation to the output data
        for i in range(n):
            output_data.append({"conversation": [conversation]})

    # Write the output data to a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(output_data, json_file, indent=4, ensure_ascii=False)

    print(f"Conversion complete. Output written to {output_file}")

# Replace 'MedQA2019.xlsx' and 'output.jsonl' with your actual input and output file names
process_excel_to_json('贸易便利化术语.xlsx', 'trade20240124-train.jsonl')
