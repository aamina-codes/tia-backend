class SummaryGenerator:

    def generate(
        self,
        thyroid_values,
        analysis,
        risk,
        diseases,
        recommendations
    ):

        lines = []

        # ==========================================
        # Heading
        # ==========================================

        lines.append("Thyroid Analysis Summary")
        lines.append("")

        # ==========================================
        # Overall Interpretation
        # ==========================================

        interpretation = analysis.get(
            "interpretation",
            "No interpretation available."
        )

        lines.append(interpretation)
        lines.append("")

        # ==========================================
        # Overall Health
        # ==========================================

        lines.append(
            f"Health Score: {risk.get('health_score', 'N/A')}/100"
        )

        lines.append(
            f"Risk Level: {risk.get('risk_level', 'Unknown')}"
        )

        lines.append("")

        # ==========================================
        # Abnormal Findings
        # ==========================================

        abnormal = analysis.get(
            "abnormal_tests",
            []
        )

        if abnormal:

            lines.append("Abnormal Findings:")

            for test in abnormal:

                test_data = thyroid_values.get(test)

                if test_data:

                    value = test_data.get("value")
                    unit = test_data.get("unit", "")

                    status = test_data.get("status", "")

                    lines.append(
                        f"• {test}: {value} {unit} ({status})"
                    )

            lines.append("")

        # ==========================================
        # Possible Conditions
        # ==========================================

        if diseases:

            lines.append("Possible Conditions:")

            for disease in diseases:

                lines.append(
                    f"• {disease['condition']} ({disease['confidence']} confidence)"
                )

            lines.append("")

        # ==========================================
        # Recommendations
        # ==========================================

        if recommendations:

            lines.append("Recommendations:")

            for recommendation in recommendations:

                lines.append(
                    f"• {recommendation}"
                )

        return "\n".join(lines)