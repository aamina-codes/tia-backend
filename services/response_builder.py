"""
Builds the final API response.

Keeping the response generation in one place makes it easy to:
- maintain
- extend
- keep every endpoint consistent
"""


class ResponseBuilder:

    @staticmethod
    def build(
        thyroid_values,
        report_analysis,
        history
    ):
        """
        Build the final API response.

        Parameters
        ----------
        thyroid_values : dict
            Extracted patient/report/test values.

        report_analysis : dict
            Output from ReportAnalysisService.

        history : dict
            Patient history and trends.

        Returns
        -------
        dict
        """

        return {

            "success": True,

            "message": "Report analyzed successfully.",

            "report": {

                "patient": thyroid_values.get(
                    "patient",
                    {}
                ),

                "report": thyroid_values.get(
                    "report",
                    {}
                ),

                "thyroid_profile": thyroid_values.get(
                    "thyroid_profile",
                    {}
                ),

                "analysis": report_analysis.get(
                    "analysis",
                    {}
                ),

                "risk": report_analysis.get(
                    "risk",
                    {}
                ),

                "possible_conditions": report_analysis.get(
                    "possible_conditions",
                    []
                ),

                "recommendations": report_analysis.get(
                    "recommendations",
                    []
                ),

                "red_flags": report_analysis.get(
                    "red_flags",
                    []
                ),

                "summary": report_analysis.get(
                    "summary",
                    ""
                )

            },

            "history": history

        }

    @staticmethod
    def success(message="Success", data=None):
        """
        Generic success response.
        """

        return {

            "success": True,

            "message": message,

            "data": data or {}

        }

    @staticmethod
    def error(message="Something went wrong", errors=None):
        """
        Generic error response.
        """

        return {

            "success": False,

            "message": message,

            "errors": errors or []

        }