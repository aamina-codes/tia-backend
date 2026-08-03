from analysis.analyzer import ThyroidAnalyzer
from analysis.disease_detector import DiseaseDetector

values = {

    "TSH": 6.8,
    "FT3": 3.4,
    "FT4": 1.1,
    "Anti_TPO": 250

}

analysis = ThyroidAnalyzer().analyze(values)

detector = DiseaseDetector()

diseases = detector.detect(analysis)

print("Analysis")
print(analysis)

print()

print("Possible Conditions")
print(diseases)