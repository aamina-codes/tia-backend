from analysis.analyzer import ThyroidAnalyzer
from analysis.risk_calculator import RiskCalculator
from analysis.disease_detector import DiseaseDetector
from analysis.summary_generator import SummaryGenerator

values = {

    "TSH": 6.8,
    "FT3": 3.4,
    "FT4": 1.1,
    "Anti_TPO": 250

}

analysis = ThyroidAnalyzer().analyze(values)

risk = RiskCalculator().calculate(analysis)

diseases = DiseaseDetector().detect(analysis)

summary = SummaryGenerator().generate(
    analysis,
    risk,
    diseases
)

print(summary)