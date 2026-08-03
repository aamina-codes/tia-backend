"""
Handles the complete thyroid report analysis workflow.

This service coordinates all analysis-related modules and returns
a single structured report containing:
- Analysis
- Risk
- Possible Conditions
- Recommendations
- Red Flags
- Summary
"""

from analysis.analyzer import ThyroidAnalyzer
from analysis.risk_calculator import RiskCalculator
from analysis.disease_detector import DiseaseDetector
from analysis.recommendation_engine import RecommendationEngine
from analysis.red_flag_detector import RedFlagDetector
from analysis.summary_generator import SummaryGenerator


class ReportAnalysisService:

    def __init__(self):

        self.analyzer = ThyroidAnalyzer()
        self.risk_calculator = RiskCalculator()
        self.disease_detector = DiseaseDetector()
        self.recommendation_engine = RecommendationEngine()
        self.red_flag_detector = RedFlagDetector()
        self.summary_generator = SummaryGenerator()
        
        
    def analyze(self, thyroid_values):
        """
        Runs the complete thyroid analysis pipeline.

        Parameters
        ----------
        thyroid_values : dict

        Returns
        -------
        dict
        """

        # ---------------------------------------
        # Analyze thyroid values
        # ---------------------------------------

        analysis = self.analyzer.analyze(
            thyroid_values
        )

        # ---------------------------------------
        # Calculate health risk
        # ---------------------------------------

        risk = self.risk_calculator.calculate(
            analysis
        )

        # ---------------------------------------
        # Detect possible thyroid conditions
        # ---------------------------------------

        diseases = self.disease_detector.detect(
            analysis
        )

        # ---------------------------------------
        # Generate recommendations
        # ---------------------------------------

        recommendations = (
            self.recommendation_engine.generate(
                thyroid_values,
                analysis,
                diseases
            )
        )

        # ---------------------------------------
        # Detect emergency findings
        # ---------------------------------------

        red_flags = self.red_flag_detector.generate(
            analysis
        )

        # ---------------------------------------
        # Generate patient summary
        # ---------------------------------------

        summary = self.summary_generator.generate(
            thyroid_values,
            analysis,
            risk,
            diseases,
            recommendations
        )

        # ---------------------------------------
        # Return complete report
        # ---------------------------------------

        return {

            "analysis": analysis,

            "risk": risk,

            "possible_conditions": diseases,

            "recommendations": recommendations,

            "red_flags": red_flags,

            "summary": summary

        }