from analysis.timeline_generator import TimelineGenerator

reports = [

    {
        "processed_at": "2025-06-15T10:30:00",
        "thyroid_values": {
            "TSH": 7.8
        }
    },

    {
        "processed_at": "2025-04-01T08:00:00",
        "thyroid_values": {
            "TSH": 10.5
        }
    },

    {
        "processed_at": "2025-08-10T11:45:00",
        "thyroid_values": {
            "TSH": 5.1
        }
    }

]

timeline = TimelineGenerator().generate(reports)

for report in timeline:

    print(
        report["processed_at"],
        report["thyroid_values"]["TSH"]
    )