from ai.validator import OutputValidator

response = """
```json
{
    "TSH":"5.21 mIU/L",
    "FT3":"3.5 pg/ml",
    "FT4":"1.18 ng/dL",
    "Anti_TPO":"35 IU/ml",
    "T3":null,
    "T4":null
}"""

parsed = OutputValidator.parse_json(response)

cleaned = OutputValidator.normalize_values(parsed)

print(cleaned)