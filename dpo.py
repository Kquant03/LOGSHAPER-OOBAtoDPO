import json
import os

def convert_to_jsonl(input_folder, output_file):
    with open(output_file, 'w') as jsonl_file:
        for filename in os.listdir(input_folder):
            if filename.endswith('.json'):
                with open(os.path.join(input_folder, filename), 'r') as json_file:
                    data = json.load(json_file)
                    internal_data = data.get('internal', [])
                    if len(internal_data) >= 2:
                        question = internal_data[0][0]
                        rejected = internal_data[0][1]
                        jsonl_data = {
                            "system": "",
                            "question": question,
                            "chosen": "",
                            "rejected": rejected
                        }
                        jsonl_file.write(json.dumps(jsonl_data) + '\n')

# Example usage:
input_folder = '/home/REDACTED/Desktop/text-generation-webui/logs/chat/Assistant'
output_file = 'pneumadpo.jsonl'
convert_to_jsonl(input_folder, output_file)
