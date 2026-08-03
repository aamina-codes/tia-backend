"""
history/history_service.py

Coordinates the complete thyroid history pipeline.
"""

from history.history_loader import HistoryLoader
from history.timeline_builder import TimelineBuilder
from history.trend_analyzer import TrendAnalyzer
from history.history_insights import HistoryInsights


class HistoryService:

    def __init__(self):

        self.loader = HistoryLoader()

    def generate_history(self):
        """
        Builds complete patient history.
        """

        # -----------------------------------
        # Load all reports
        # -----------------------------------

        reports = self.loader.load_reports()

        # -----------------------------------
        # Build timeline
        # -----------------------------------

        timeline = TimelineBuilder.build(
            reports
        )

        # -----------------------------------
        # Analyze trends
        # -----------------------------------

        trends = TrendAnalyzer.analyze(
            timeline
        )

        # -----------------------------------
        # Generate insights
        # -----------------------------------

        insights = HistoryInsights.generate(
            trends
        )

        # -----------------------------------
        # Return History
        # -----------------------------------

        return {

            "total_reports": len(reports),

            "timeline": timeline,

            "trends": trends,

            "insights": insights

        }