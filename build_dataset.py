import json
import glob
import os

dataset = []

json_files = glob.glob("extracted_json/*.json")

for file in json_files:

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    dataset.append(data)

os.makedirs("dataset", exist_ok=True)

with open(
    "dataset/thyroid_dataset.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        dataset,
        f,
        indent=4
    )

print(f"Dataset created with {len(dataset)} reports.")