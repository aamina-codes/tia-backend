import glob
import json
import os
import traceback
from datetime import datetime
from ai.prompts import THYROID_EXTRACTION_PROMPT
from services.report_analysis_service import ReportAnalysisService

from ai.extractor import AIExtractor
from ai.validator import OutputValidator


class DocumentProcessor:

    def __init__(self):
        self.extractor = AIExtractor()
        self.analysis_service = ReportAnalysisService()

    def process(self, report_path):

        print(f"\n📄 Processing: {os.path.basename(report_path)}")

        # Extract using Gemini
        response = self.extractor.extract(
    report_path,
    THYROID_EXTRACTION_PROMPT
)

        # Parse JSON
        parsed = OutputValidator.parse_json(response)

        # Normalize values
        cleaned = OutputValidator.normalize_values(parsed)
        analysis_result = self.analysis_service.analyze(
    cleaned
)

        # Create output folder
        os.makedirs("extracted_json", exist_ok=True)

        output_path = os.path.join(
            "extracted_json",
            os.path.splitext(os.path.basename(report_path))[0] + ".json"
        )

        # Final JSON structure
        output = {
    "file_name": os.path.basename(report_path),
    "provider": "Gemini",
    "model": "gemini-2.5-flash",
    "processed_at": datetime.now().isoformat(),
    "status": "success",

    "thyroid_values": cleaned,

    "analysis": analysis_result
}

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4)

        print(f"✅ Saved: {output_path}")

        return output

    def process_folder(self, folder_path):

        supported_extensions = (
            "*.pdf",
            "*.png",
            "*.jpg",
            "*.jpeg"
        )

        reports = []

        for extension in supported_extensions:
            reports.extend(
                glob.glob(
                    os.path.join(folder_path, extension)
                )
            )

        print(f"\nFound {len(reports)} reports.\n")

        if not reports:
            print("No reports found.")
            return

        successful = 0
        failed = 0

        for index, report in enumerate(reports, start=1):

            print("=" * 70)
            print(f"[{index}/{len(reports)}] {os.path.basename(report)}")
            print("=" * 70)

            try:

                self.process(report)
                successful += 1

            except Exception as e:

                failed += 1

                print("❌ Failed")
                print(f"File : {report}")
                print(f"Error Type : {type(e).__name__}")
                print(f"Message : {e}")

                traceback.print_exc()

                print("-" * 70)

        print("\n" + "=" * 70)
        print("PROCESS COMPLETE")
        print("=" * 70)
        print(f"Successful : {successful}")
        print(f"Failed     : {failed}")
        print(f"Total      : {len(reports)}")