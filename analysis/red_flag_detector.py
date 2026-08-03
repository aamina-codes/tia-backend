class RedFlagDetector:

    def generate(self, analysis):

        red_flags = []

        # -------------------------
        # TSH
        # -------------------------

        tests = analysis.get("tests", {})
        
        tsh = tests.get("TSH", {})
        ft4 = tests.get("FT4", {})
        ft3 = tests.get("FT3", {})
        
        if tsh is not None:
            value = tsh.get("value")

            if value is not None:

                if value > 10:
                    red_flags.append({
                        "title": "TSH is significantly elevated",
                        "message": "Your TSH level is above 10 mIU/L. Please consult an endocrinologist soon.",
                        "urgency": "high"
                    })

                elif value > 5:
                    red_flags.append({
                        "title": "TSH is above the normal range",
                        "message": "Your TSH is mildly elevated. Follow up with your doctor.",
                        "urgency": "moderate"
                    })

                elif value < 0.1:
                    red_flags.append({
                        "title": "TSH is very low",
                        "message": "Your TSH is extremely low. Medical evaluation is recommended.",
                        "urgency": "high"
                    })

                elif value < 0.4:
                    red_flags.append({
                        "title": "TSH is below the normal range",
                        "message": "Your TSH is slightly low. Discuss this with your healthcare provider.",
                        "urgency": "moderate"
                    })

        # -------------------------
        # FT4
        # -------------------------


        if ft4:

            value = ft4.get("value")

            if value is not None:

                if value < 0.6:

                    red_flags.append({

                        "title": "Very Low FT4",

                        "message": "FT4 is significantly below normal.",

                        "urgency": "high"

                    })

                elif value > 2.0:

                    red_flags.append({

                        "title": "Very High FT4",

                        "message": "FT4 is significantly above normal.",

                        "urgency": "high"

                    })

        # -------------------------
        # FT3
        # -------------------------


        if ft3:

            value = ft3.get("value")

            if value is not None:

                if value < 1.5:

                    red_flags.append({

                        "title": "Very Low FT3",

                        "message": "FT3 is significantly below normal.",

                        "urgency": "high"

                    })

                elif value > 6:

                    red_flags.append({

                        "title": "Very High FT3",

                        "message": "FT3 is significantly above normal.",

                        "urgency": "high"

                    })

        return red_flags