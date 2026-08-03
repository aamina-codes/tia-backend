from analysis.thyroid_rules import evaluate_test


class ThyroidAnalyzer:

    def analyze(self, thyroid_values):

        analysis = {}

        abnormal_tests = []

        interpretation = []

        # -----------------------------------
        # Evaluate each thyroid test
        # -----------------------------------

        for test, data in thyroid_values.items():

            # Skip patient/report sections
            if test in ["patient", "report"]:
                continue

            if data is None:
                continue

            value = data.get("value")

            status = evaluate_test(test, value)

            analysis[test] = {
                "status": status
            }

            if status != "Normal":
                abnormal_tests.append(test)

        # -----------------------------------
        # Overall Status
        # -----------------------------------

        if not abnormal_tests:

            overall_status = "Normal"

            interpretation.append(
                "All available thyroid markers are within their reference ranges."
            )

        else:

            overall_status = "Abnormal"

            # Simple rule-based interpretation

            tsh = analysis.get("TSH", {}).get("status")
            ft4 = analysis.get("FT4", {}).get("status")
            ft3 = analysis.get("FT3", {}).get("status")

            if tsh == "High" and ft4 == "Low":

                interpretation.append(
                    "Pattern is suggestive of primary hypothyroidism."
                )

            elif tsh == "High" and ft4 == "Normal":

                interpretation.append(
                    "Pattern may indicate subclinical hypothyroidism."
                )

            elif tsh == "Low" and ft4 == "High":

                interpretation.append(
                    "Pattern is suggestive of hyperthyroidism."
                )

            else:

                interpretation.append(
                    "Some thyroid markers are outside the normal range and should be clinically correlated."
                )

        return {

            "overall_status": overall_status,

            "abnormal_tests": abnormal_tests,

            "interpretation": " ".join(interpretation)

        }