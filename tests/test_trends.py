from analysis.trend_analyzer import TrendAnalyzer

reports = [

    {
        "thyroid_values": {
            "TSH": 10.5,
            "FT4": 0.7
        }
    },

    {
        "thyroid_values": {
            "TSH": 7.2,
            "FT4": 0.9
        }
    },

    {
        "thyroid_values": {
            "TSH": 4.8,
            "FT4": 1.2
        }
    }

]

trend = TrendAnalyzer().analyze(reports)

print(trend)