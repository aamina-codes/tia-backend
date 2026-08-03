from analysis.analyzer import ThyroidAnalyzer
from analysis.disease_detector import DiseaseDetector
from analysis.recommendation_engine import RecommendationEngine

values = {

    "TSH": 6.8,
    "FT3": 3.4,
    "FT4": 1.1,
    "Anti_TPO": 250

}

analysis = ThyroidAnalyzer().analyze(values)

diseases = DiseaseDetector().detect(analysis)

recommendations = RecommendationEngine().generate(
    analysis,
    diseases
)

for recommendation in recommendations:
    print("-", recommendation)