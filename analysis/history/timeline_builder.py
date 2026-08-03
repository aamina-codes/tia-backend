"""
history/timeline_builder.py

Builds a chronological timeline of thyroid reports.
"""

from datetime import datetime


class TimelineBuilder:

    # Supported report date formats
    DATE_FORMATS = [

        "%d/%m/%Y",
        "%d/%m/%Y %H:%M",

        "%d-%m-%Y",
        "%d-%m-%Y %H:%M",

        "%Y-%m-%d",

        "%d/%b/%Y",
        "%d/%b/%Y %H:%M:%S",

        "%d-%b-%Y",

        "%b %d, %Y",

        "%d %b %Y",

        "%d/%m/%y",

        "%d-%m-%y"
    ]

    @classmethod
    def parse_date(cls, date_string):
        """
        Converts a report date into a datetime object.
        Returns None if parsing fails.
        """

        if not date_string:
            return None

        date_string = str(date_string).strip()

        for fmt in cls.DATE_FORMATS:

            try:
                return datetime.strptime(date_string, fmt)

            except ValueError:
                continue

        return None

    @classmethod
    def build(cls, reports):
        """
        Build chronological timeline.

        Parameters
        ----------
        reports : list

        Returns
        -------
        list
        """

        timeline = []

        for report in reports:

            report_info = report.get("report", {})

            patient = report.get("patient", {})

            thyroid_profile = report.get("thyroid_profile", {})

            report_date = report_info.get("report_date")

            parsed_date = cls.parse_date(report_date)

            timeline.append({

                "date": parsed_date,

                "report_date": report_date,

                "patient": patient,

                "report": report_info,

                "thyroid_profile": thyroid_profile,

                "analysis": report.get("analysis"),

                "risk": report.get("risk"),

                "summary": report.get("summary"),

                "processed_at": report.get("processed_at")

            })

        timeline.sort(
            key=lambda x: (
                x["date"] is None,
                x["date"]
            )
        )

        return timeline