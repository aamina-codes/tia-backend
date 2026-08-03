"""
history/history_insights.py

Generates AI-friendly insights from historical thyroid trends.
"""


class HistoryInsights:

    @classmethod
    def generate(cls, trends):

        insights = []

        if not trends:
            return insights

        # ----------------------------------------------------
        # TSH
        # ----------------------------------------------------

        tsh = trends.get("TSH")

        if tsh:

            if tsh["status"] == "Worsening":

                insights.append(
                    "TSH has shown a consistent upward trend across your reports."
                )

            elif tsh["status"] == "Improving":

                insights.append(
                    "TSH levels have gradually improved over time."
                )

            elif tsh["trend"] == "Stable":

                insights.append(
                    "TSH has remained stable across previous reports."
                )

        # ----------------------------------------------------
        # FT4
        # ----------------------------------------------------

        ft4 = trends.get("FT4")

        if ft4:

            if ft4["status"] == "Improving":

                insights.append(
                    "Free T4 has improved compared to previous reports."
                )

            elif ft4["status"] == "Worsening":

                insights.append(
                    "Free T4 has gradually decreased over time."
                )

        # ----------------------------------------------------
        # FT3
        # ----------------------------------------------------

        ft3 = trends.get("FT3")

        if ft3:

            if ft3["status"] == "Improving":

                insights.append(
                    "Free T3 levels have shown improvement."
                )

            elif ft3["status"] == "Worsening":

                insights.append(
                    "Free T3 levels have been declining."
                )

        # ----------------------------------------------------
        # Anti TPO
        # ----------------------------------------------------

        anti = trends.get("Anti_TPO")

        if anti:

            if anti["trend"] == "Increasing":

                insights.append(
                    "Anti-TPO antibodies are increasing, which may indicate increasing autoimmune thyroid activity."
                )

            elif anti["trend"] == "Decreasing":

                insights.append(
                    "Anti-TPO antibodies have decreased over time."
                )

        # ----------------------------------------------------
        # Overall Trend
        # ----------------------------------------------------

        worsening = 0
        improving = 0

        for trend in trends.values():

            if trend is None:
                continue

            if trend["status"] == "Worsening":
                worsening += 1

            elif trend["status"] == "Improving":
                improving += 1

        if worsening >= 2:

            insights.append(
                "Multiple thyroid markers have worsened over time. A follow-up with your healthcare provider is recommended."
            )

        elif improving >= 2:

            insights.append(
                "Overall thyroid profile appears to be improving across successive reports."
            )

        elif worsening == 0 and improving == 0:

            insights.append(
                "Your thyroid profile has remained relatively stable over time."
            )

        return insights