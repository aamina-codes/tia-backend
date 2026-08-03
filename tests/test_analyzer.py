from analysis.analyzer import ThyroidAnalyzer

values = {
    "TSH": 6.8,
    "FT3": 3.4,
    "FT4": 1.1,
    "Anti_TPO": 250
}

analyzer = ThyroidAnalyzer()

result = analyzer.analyze(values)

print(result)