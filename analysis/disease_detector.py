class DiseaseDetector:

    def detect(self, analysis):

        diseases = []

        tests = analysis.get("tests", {})
        
        tsh = tests.get("TSH", {})
        ft3 = tests.get("FT3", {})
        ft4 = tests.get("FT4", {})
        anti_tpo = tests.get("Anti_TPO", {})

        tsh_status = tsh.get("status")
        ft3_status = ft3.get("status")
        ft4_status = ft4.get("status")
        anti_tpo_status = anti_tpo.get("status")

        # Primary Hypothyroidism
        if tsh_status == "High" and ft4_status == "Low":
            diseases.append({
                "condition": "Primary Hypothyroidism",
                "confidence": "High"
            })

        # Subclinical Hypothyroidism
        elif tsh_status == "High" and ft4_status == "Normal":
            diseases.append({
                "condition": "Subclinical Hypothyroidism",
                "confidence": "Moderate"
            })

        # Hyperthyroidism
        if tsh_status == "Low" and ft4_status == "High":
            diseases.append({
                "condition": "Hyperthyroidism",
                "confidence": "High"
            })

        # Hashimoto's Thyroiditis
        if anti_tpo_status == "High" and tsh_status == "High":
            diseases.append({
                "condition": "Possible Hashimoto's Thyroiditis",
                "confidence": "Moderate"
            })

        if not diseases:
            diseases.append({
                "condition": "No obvious thyroid disorder pattern detected",
                "confidence": "Low"
            })

        return diseases