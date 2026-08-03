class TrendAnalyzer:

    TEST_MAPPING = {
        "THYROID STIMULATING HORMONE": "TSH",
        "TSH": "TSH",

        "FREE T3": "FT3",
        "FT3": "FT3",

        "FREE T4": "FT4",
        "FT4": "FT4",

        "TRI-IODO THYRONIN": "T3",
        "T3": "T3",

        "THYROXIN": "T4",
        "T4": "T4",

        "ANTI-TPO": "Anti_TPO",
        "ANTI TPO": "Anti_TPO",
        "ANTI_TPO": "Anti_TPO"
    }

    def analyze(self, reports):

        trends = {}

        if len(reports) < 2:
            return trends

        collected = {}

        for report in reports:

            tests = report.get(
                "thyroid_values",
                {}
            ).get(
                "tests",
                []
            )

            for test in tests:

                raw_name = test.get(
                    "name",
                    ""
                ).upper()

                value = test.get("value")

                standard_name = None

                for key in self.TEST_MAPPING:

                    if key in raw_name:

                        standard_name = self.TEST_MAPPING[key]

                        break

                if standard_name is None:

                    continue

                if value is None:

                    continue

                collected.setdefault(
                    standard_name,
                    []
                ).append(value)

        for test, values in collected.items():

            if len(values) < 2:
                continue

            first = values[0]
            latest = values[-1]

            if latest > first:

                trend = "Increasing"

            elif latest < first:

                trend = "Decreasing"

            else:

                trend = "Stable"

            trends[test] = {

                "first": first,

                "latest": latest,

                "trend": trend

            }

        return trends