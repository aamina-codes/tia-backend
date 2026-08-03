from ai.extractor import AIExtractor

extractor = AIExtractor()

response = extractor.extract_from_text("""

Patient Name : ABC

TSH : 7.82

FT3 : 3.25

FT4 : 1.18

Vitamin D : 24

HbA1c : 5.4

""")

print(response)