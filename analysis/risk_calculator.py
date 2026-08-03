class RiskCalculator:

    def calculate(self, analysis):

        tests = analysis.get("tests", {})

        score = 100

        deductions = {
            "Normal": 0,
            "Low": 10,
            "High": 10,
            "Unknown": 0
        }

        abnormal_tests = []

        for test, result in tests.items():

            status = result.get("status", "Unknown")

            score -= deductions.get(status, 0)

            if status != "Normal":
                abnormal_tests.append(test)

        score = max(score, 0)

        if score >= 85:
            risk_level = "Low"

        elif score >= 60:
            risk_level = "Moderate"

        else:
            risk_level = "High"

        return {

            "health_score": score,

            "risk_level": risk_level

        }