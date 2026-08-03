"""
history/unit_converter.py

Utility class for normalizing thyroid test units across reports.
"""

from typing import Optional, Tuple


class UnitConverter:
    """
    Converts thyroid test values into standardized units.

    Standard Units
    --------------
    TSH      -> mIU/L
    FT3      -> pg/mL
    FT4      -> ng/dL
    T3       -> ng/mL
    T4       -> µg/dL
    Anti_TPO -> IU/mL
    """

    # ---------------------------------------------------------
    # Standard Units
    # ---------------------------------------------------------

    STANDARD_UNITS = {
        "TSH": "mIU/L",
        "FT3": "pg/mL",
        "FT4": "ng/dL",
        "T3": "ng/mL",
        "T4": "µg/dL",
        "Anti_TPO": "IU/mL"
    }

    # ---------------------------------------------------------
    # Unit Aliases
    # ---------------------------------------------------------

    UNIT_ALIASES = {

        # ---------- TSH ----------
        "uiu/ml": "mIU/L",
        "µiu/ml": "mIU/L",
        "μiu/ml": "mIU/L",
        "miu/l": "mIU/L",
        "microu/ml": "mIU/L",

        # ---------- T3 ----------
        "ng/ml": "ng/mL",
        "ng/dl": "ng/dL",

        # ---------- FT3 ----------
        "pg/ml": "pg/mL",
        "pmol/l": "pmol/L",

        # ---------- FT4 ----------
        "ug/dl": "µg/dL",
        "µg/dl": "µg/dL",

        # ---------- Anti TPO ----------
        "iu/ml": "IU/mL"
    }

    # ---------------------------------------------------------
    # Conversion Factors
    # ---------------------------------------------------------

    CONVERSION_FACTORS = {

        # -----------------------------
        # Total T3
        # -----------------------------
        ("ng/dL", "ng/mL"): 0.01,
        ("ng/mL", "ng/dL"): 100,

        # -----------------------------
        # FT4
        # 1 pmol/L = 0.0777 ng/dL
        # -----------------------------
        ("pmol/L", "ng/dL"): 0.0777,
        ("ng/dL", "pmol/L"): 12.87,

        # -----------------------------
        # TSH
        # µIU/mL == mIU/L
        # -----------------------------
        ("mIU/L", "mIU/L"): 1.0,

        # -----------------------------
        # T4
        # Same unit
        # -----------------------------
        ("µg/dL", "µg/dL"): 1.0,

        # -----------------------------
        # FT3
        # Same unit
        # -----------------------------
        ("pg/mL", "pg/mL"): 1.0,

        # -----------------------------
        # Anti TPO
        # -----------------------------
        ("IU/mL", "IU/mL"): 1.0
    }

    # =========================================================
    # Normalize Unit Name
    # =========================================================

    @classmethod
    def normalize_unit(cls, unit: Optional[str]) -> Optional[str]:

        if unit is None:
            return None

        unit = unit.strip().lower()

        return cls.UNIT_ALIASES.get(unit, unit)

    # =========================================================
    # Convert Numeric Value
    # =========================================================

    @classmethod
    def convert_value(
        cls,
        value: Optional[float],
        from_unit: Optional[str],
        to_unit: Optional[str]
    ) -> Optional[float]:

        if value is None:
            return None

        if from_unit is None or to_unit is None:
            return value

        from_unit = cls.normalize_unit(from_unit)
        to_unit = cls.normalize_unit(to_unit)

        if from_unit == to_unit:
            return round(value, 3)

        factor = cls.CONVERSION_FACTORS.get(
            (from_unit, to_unit)
        )

        if factor is None:
            return round(value, 3)

        return round(value * factor, 3)

    # =========================================================
    # Convert Single Thyroid Test
    # =========================================================

    @classmethod
    def convert_test(
        cls,
        test_name: str,
        value: Optional[float],
        unit: Optional[str]
    ) -> Tuple[Optional[float], Optional[str]]:

        standard_unit = cls.STANDARD_UNITS.get(test_name)

        if standard_unit is None:
            return value, unit

        converted_value = cls.convert_value(
            value,
            unit,
            standard_unit
        )

        return converted_value, standard_unit

    # =========================================================
    # Normalize Thyroid Profile
    # =========================================================

    @classmethod
    def normalize_profile(cls, thyroid_profile: dict) -> dict:
        """
        Converts every thyroid marker in a report
        into the project's standard units.
        """

        normalized = {}

        for test_name, details in thyroid_profile.items():

            if details is None:
                normalized[test_name] = None
                continue

            value = details.get("value")
            unit = details.get("unit")

            value, unit = cls.convert_test(
                test_name,
                value,
                unit
            )

            normalized[test_name] = {
                **details,
                "value": value,
                "unit": unit
            }

        return normalized