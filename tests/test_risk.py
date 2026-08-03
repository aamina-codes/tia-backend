from analysis.analyzer import ThyroidAnalyzer
from analysis.risk_calculator import RiskCalculator

values = {

    "TSH": 6.8,

    "FT3": 3.4,

    "FT4": 1.1,

    "Anti_TPO": 250

}

analysis = ThyroidAnalyzer().analyze(values)

risk = RiskCalculator().calculate(analysis)

print("Analysis")
print(analysis)

print()

print("Risk")
print(risk)