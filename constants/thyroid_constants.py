"""
Constants used throughout the Thyroid Intelligent Assistant.
"""

# ==========================================================
# Test Names
# ==========================================================

TEST_TSH = "TSH"

TEST_FT3 = "FT3"

TEST_FT4 = "FT4"

TEST_T3 = "T3"

TEST_T4 = "T4"

TEST_ANTI_TPO = "Anti_TPO"

THYROID_TESTS = [
    TEST_TSH,
    TEST_FT3,
    TEST_FT4,
    TEST_T3,
    TEST_T4,
    TEST_ANTI_TPO
]

# ==========================================================
# Test Status
# ==========================================================

STATUS_LOW = "Low"

STATUS_NORMAL = "Normal"

STATUS_HIGH = "High"

STATUS_BORDERLINE = "Borderline"

STATUS_UNKNOWN = "Unknown"

# ==========================================================
# Risk Levels
# ==========================================================

RISK_LOW = "Low"

RISK_MODERATE = "Moderate"

RISK_HIGH = "High"

# ==========================================================
# Overall Report Status
# ==========================================================

OVERALL_NORMAL = "Normal"

OVERALL_ABNORMAL = "Abnormal"

# ==========================================================
# Possible Conditions
# ==========================================================

CONDITION_NORMAL = "No obvious thyroid disorder pattern detected"

CONDITION_PRIMARY_HYPOTHYROIDISM = "Primary Hypothyroidism"

CONDITION_SUBCLINICAL_HYPOTHYROIDISM = "Subclinical Hypothyroidism"

CONDITION_PRIMARY_HYPERTHYROIDISM = "Primary Hyperthyroidism"

CONDITION_SUBCLINICAL_HYPERTHYROIDISM = "Subclinical Hyperthyroidism"

CONDITION_HASHIMOTOS = "Hashimoto's Thyroiditis"

CONDITION_GRAVES = "Graves' Disease"

CONDITION_CENTRAL_HYPOTHYROIDISM = "Central Hypothyroidism"

# ==========================================================
# Confidence Levels
# ==========================================================

CONFIDENCE_LOW = "Low"

CONFIDENCE_MEDIUM = "Medium"

CONFIDENCE_HIGH = "High"

# ==========================================================
# Gender
# ==========================================================

GENDER_MALE = "Male"

GENDER_FEMALE = "Female"

GENDER_OTHER = "Other"

# ==========================================================
# API Response
# ==========================================================

SUCCESS = "success"

FAILED = "failed"

SUCCESS_MESSAGE = "Report analyzed successfully."

ERROR_MESSAGE = "Failed to analyze report."

# ==========================================================
# Units
# ==========================================================

UNIT_MIU_L = "mIU/L"

UNIT_UIU_ML = "µIU/mL"

UNIT_NG_DL = "ng/dL"

UNIT_NG_ML = "ng/mL"

UNIT_PG_ML = "pg/mL"

UNIT_UG_DL = "µg/dL"

UNIT_IU_ML = "IU/mL"

UNIT_PMO_L = "pmol/L"

# ==========================================================
# Trend Labels
# ==========================================================

TREND_INCREASING = "Increasing"

TREND_DECREASING = "Decreasing"

TREND_STABLE = "Stable"

TREND_UNKNOWN = "Unknown"