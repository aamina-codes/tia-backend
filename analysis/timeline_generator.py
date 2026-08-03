from datetime import datetime


class TimelineGenerator:

    def generate(self, reports):

        def get_date(report):

            processed_at = report.get("processed_at")

            if processed_at:

                try:
                    return datetime.fromisoformat(processed_at)
                except ValueError:
                    pass

            return datetime.min

        reports = sorted(
            reports,
            key=get_date
        )

        return reports