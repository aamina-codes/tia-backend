"""
history/trend_analyzer.py

Analyzes historical thyroid trends.
"""

from statistics import mean

from analysis.history.unit_convertor import UnitConverter


class TrendAnalyzer:

    TESTS = [
        "TSH",
        "FT3",
        "FT4",
        "T3",
        "T4",
        "Anti_TPO"
    ]

    # ---------------------------------------------------------
    # Analyze All Trends
    # ---------------------------------------------------------

    @classmethod
    def analyze(cls, timeline):

        trends = {}

        for test in cls.TESTS:

            trends[test] = cls._analyze_test(
                timeline,
                test
            )

        return trends

    # ---------------------------------------------------------
    # Analyze One Test
    # ---------------------------------------------------------

    @classmethod
    def _analyze_test(
        cls,
        timeline,
        test_name
    ):

        values = []

        for report in timeline:

            profile = report.get(
                "thyroid_profile",
                {}
            )

            test = profile.get(test_name)

            if test is None:
                continue

            value = test.get("value")

            unit = test.get("unit")

            value, unit = UnitConverter.convert_test(
                test_name,
                value,
                unit
            )

            if value is not None:
                values.append(value)

        if len(values) == 0:

            return None

        first = values[0]

        latest = values[-1]

        minimum = min(values)

        maximum = max(values)

        average = round(
            mean(values),
            2
        )

        change = round(
            latest - first,
            2
        )

        percent_change = 0

        if first != 0:

            percent_change = round(
                (change / first) * 100,
                2
            )

        trend = cls._trend(change)

        status = cls._status(
            test_name,
            first,
            latest
        )

        return {

            "first": first,

            "latest": latest,

            "minimum": minimum,

            "maximum": maximum,

            "average": average,

            "change": change,

            "percent_change": percent_change,

            "trend": trend,

            "status": status,

            "total_reports": len(values)

        }

    # ---------------------------------------------------------
    # Trend Direction
    # ---------------------------------------------------------

    @staticmethod
    def _trend(change):

        if abs(change) < 0.001:
            return "Stable"

        if change > 0:
            return "Increasing"

        return "Decreasing"

    # ---------------------------------------------------------
    # Clinical Interpretation
    # ---------------------------------------------------------

    @staticmethod
    def _status(
        test,
        first,
        latest
    ):

        change = latest - first

        # -------------------------
        # TSH
        # -------------------------

        if test == "TSH":

            if change > 0.5:
                return "Worsening"

            if change < -0.5:
                return "Improving"

            return "Stable"

        # -------------------------
        # FT4 / FT3
        # Higher is usually better
        # -------------------------

        if test in ["FT3", "FT4"]:

            if change > 0.2:
                return "Improving"

            if change < -0.2:
                return "Worsening"

            return "Stable"

        # -------------------------
        # T3 / T4 / Anti TPO
        # -------------------------

        if abs(change) < 0.2:
            return "Stable"

        if change > 0:
            return "Increasing"

        return "Decreasing"