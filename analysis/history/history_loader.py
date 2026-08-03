import json
import os


class HistoryLoader:

    def __init__(self):

        self.history_file = os.path.join(
            "storage",
            "history.json"
        )

    def load_reports(self):

        """
        Load all historical thyroid reports.

        Returns
        -------
        list
            List of processed reports.
        """

        if not os.path.exists(self.history_file):
            return []

        try:

            with open(
                self.history_file,
                "r",
                encoding="utf-8"
            ) as f:

                reports = json.load(f)

            if isinstance(reports, list):
                return reports

            return []

        except Exception as e:

            print(f"[HistoryLoader] {e}")

            return []
    
    def save_report(self, report):
        reports = self.load_reports()
        reports.append(report)
        
        with open(
        self.history_file,
        "w",
        encoding="utf-8"
    ) as f:
            
            json.dump(
            reports,
            f,
            indent=4,
            ensure_ascii=False
        )