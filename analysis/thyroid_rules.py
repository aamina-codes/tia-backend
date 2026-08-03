THYROID_RULES = {

    "TSH": {
        "low": 0.4,
        "high": 4.5,
        "unit": "mIU/L",
        "name": "Thyroid Stimulating Hormone"
    },

    "FT3": {
        "low": 2.0,
        "high": 4.4,
        "unit": "pg/mL",
        "name": "Free T3"
    },

    "FT4": {
        "low": 0.8,
        "high": 1.8,
        "unit": "ng/dL",
        "name": "Free T4"
    },

    "T3": {
        "low": 80,
        "high": 200,
        "unit": "ng/dL",
        "name": "Total T3"
    },

    "T4": {
        "low": 5.0,
        "high": 12.0,
        "unit": "µg/dL",
        "name": "Total T4"
    },

    "Anti_TPO": {
        "low": 0,
        "high": 35,
        "unit": "IU/mL",
        "name": "Anti Thyroid Peroxidase Antibody"
    }

}


def evaluate_test(test_name, value):
    """
    Evaluate whether a thyroid test result is
    Low, Normal or High.
    """

    if value is None:
        return "Unknown"

    rules = THYROID_RULES.get(test_name)

    if rules is None:
        return "Unknown"

    if value < rules["low"]:
        return "Low"

    if value > rules["high"]:
        return "High"

    return "Normal"