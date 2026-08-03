import os
from pathlib import Path

from ai.extractor import AIExtractor
from ai.prompts import THYROID_EXTRACTION_PROMPT
from ai.validator import OutputValidator

from services.report_analysis_service import ReportAnalysisService
from analysis.history.history_service import HistoryService

from services.response_builder import ResponseBuilder

from utils.logger import setup_logger


logger = setup_logger(__name__)


class ThyroidPipeline:
    """
    Main pipeline orchestrator for TIA.

    Flow:
    Report
      -> AI Extraction
      -> Validation
      -> Analysis
      -> History Tracking
      -> Response Formatting
    """

    def __init__(self):

        self.extractor = AIExtractor()

        self.validator = OutputValidator()

        self.report_analyzer = ReportAnalysisService()

        self.history_service = HistoryService()

        self.response_builder = ResponseBuilder()


    def process(self, file_path: str):

        try:
            logger.info(
                f"Starting thyroid pipeline for: {file_path}"
            )


            # -------------------------------------------------
            # 1. Extract thyroid values using AI
            # -------------------------------------------------

            logger.info(
                "Extracting thyroid parameters..."
            )

            raw_response = self.extractor.extract(
                file_path=file_path,
                prompt=THYROID_EXTRACTION_PROMPT
            )


            logger.info(
                "Extraction completed"
            )


            # -------------------------------------------------
            # 2. Parse AI JSON response
            # -------------------------------------------------

            logger.info(
                "Parsing extracted JSON..."
            )

            extracted_data = (
                self.validator.parse_json(
                    raw_response
                )
            )


            # -------------------------------------------------
            # 3. Normalize values
            # -------------------------------------------------

            logger.info(
                "Normalizing extracted values..."
            )

            validated_data = (
                self.validator.normalize_values(
                    extracted_data
                )
            )


            # -------------------------------------------------
            # 4. Analyze thyroid report
            # -------------------------------------------------

            logger.info(
                "Generating thyroid analysis..."
            )

            analysis = (
                self.report_analyzer.analyze(
                    validated_data
                )
            )


            # -------------------------------------------------
            # 5. Store report history
            # -------------------------------------------------

            logger.info(
                "Saving report history..."
            )

            history_record = (
                self.history_service.save_report(
                    report_data=validated_data,
                    analysis=analysis
                )
            )


            # -------------------------------------------------
            # 6. Build final response
            # -------------------------------------------------

            logger.info(
                "Building final response..."
            )

            response = (
                self.response_builder.build(
                    extracted_data=validated_data,
                    analysis=analysis,
                    history=history_record
                )
            )


            logger.info(
                "Pipeline completed successfully"
            )


            return response


        except Exception as e:

            logger.exception(
                "Thyroid pipeline failed"
            )


            return (
                self.response_builder.error(
                    message=str(e)
                )
            )