class RecommendationEngine:

    def generate(
        self,
        thyroid_values,
        analysis,
        diseases
    ):

        recommendations = []

        tests = analysis.get("tests", {})
        
        tsh_status = tests.get("TSH", {}).get("status")
        
        anti_tpo_status = tests.get("Anti_TPO", {}).get("status")

        # -------------------------------------------------
        # TSH Recommendations
        # -------------------------------------------------

        if tsh_status == "High":

            recommendations.append(
                "Consult an endocrinologist regarding your elevated TSH level."
            )

        elif tsh_status == "Low":

            recommendations.append(
                "Your TSH is below the normal range. A clinical evaluation is recommended."
            )

        # -------------------------------------------------
        # Anti-TPO Recommendations
        # -------------------------------------------------

        if anti_tpo_status == "High":

            recommendations.append(
                "Elevated Anti-TPO antibodies may indicate autoimmune thyroid disease. Discuss these results with your doctor."
            )

        # -------------------------------------------------
        # Disease-based Recommendations
        # -------------------------------------------------

        for disease in diseases:

            condition = disease["condition"]

            if "Hypothyroidism" in condition:

                recommendations.append(
                    "Regular monitoring of thyroid hormone levels is recommended."
                )

            if "Hashimoto" in condition:

                recommendations.append(
                    "Periodic thyroid function testing may be beneficial."
                )

            if "Hyperthyroidism" in condition:

                recommendations.append(
                    "Your thyroid hormone levels may require further evaluation and appropriate treatment."
                )

        # -------------------------------------------------
        # Default Recommendation
        # -------------------------------------------------

        if not recommendations:

            recommendations.append(
                "No specific recommendations based on the current thyroid profile."
            )

        return list(dict.fromkeys(recommendations))