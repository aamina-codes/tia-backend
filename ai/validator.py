import json


class OutputValidator:

    @staticmethod
    def clean_json(response):
        """
        Remove markdown formatting from Gemini responses.
        """

        if not response:
            return ""

        response = response.replace("```json", "")
        response = response.replace("```", "")

        return response.strip()

    @staticmethod
    def parse_json(response):
        """
        Convert Gemini response into a Python dictionary.
        """

        response = OutputValidator.clean_json(response)

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            return {}

    @staticmethod
    def normalize_values(data):
        """
        Converts Gemini output into one standardized format.

        Final structure:

        {
            "patient": {...},
            "report": {...},
            "TSH": {...},
            "FT3": {...},
            "FT4": {...},
            "T3": {...},
            "T4": {...},
            "Anti_TPO": {...}
        }
        """

        if not isinstance(data, dict):
            return {}

        # Handle Gemini wrapper
        thyroid = data.get("thyroid_values", data)

        patient = thyroid.get("patient", {})
        report = thyroid.get("report", {})
        tests = thyroid.get("tests", [])

        normalized = {
            "patient": patient,
            "report": report,
            "TSH": None,
            "FT3": None,
            "FT4": None,
            "T3": None,
            "T4": None,
            "Anti_TPO": None
        }

        mapping = {
            # TSH
            "THYROID STIMULATING HORMONE": "TSH",
            "TSH": "TSH",

            # FT3
            "FREE T3": "FT3",
            "FREE TRI-IODOTHYRONINE": "FT3",
            "FT3": "FT3",

            # FT4
            "FREE T4": "FT4",
            "FREE THYROXINE": "FT4",
            "FT4": "FT4",

            # T3
            "TRI-IODO THYRONIN": "T3",
            "TRIIODOTHYRONINE": "T3",
            "TRI-IODO THYRONIN (T3)": "T3",
            "T3": "T3",

            # T4
            "THYROXIN": "T4",
            "THYROXINE": "T4",
            "THYROXIN (T4)": "T4",
            "T4": "T4",

            # Anti TPO
            "ANTI TPO": "Anti_TPO",
            "ANTI-TPO": "Anti_TPO",
            "ANTI_TPO": "Anti_TPO",
            "ANTI THYROID PEROXIDASE": "Anti_TPO"
        }

        for test in tests:

            raw_name = str(test.get("name", "")).upper().strip()

            standard_name = None

            for keyword, mapped in mapping.items():
                if keyword in raw_name:
                    standard_name = mapped
                    break

            if standard_name is None:
                continue

            value = test.get("value")

            try:
                value = float(value)
            except (TypeError, ValueError):
                pass

            normalized[standard_name] = {
                "value": value,
                "unit": test.get("unit"),
                "reference_range": test.get("reference_range"),
                "status": test.get("status")
            }

        return normalized