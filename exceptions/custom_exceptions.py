"""
Custom exceptions used throughout the application.
"""


class PipelineException(Exception):
    """
    Base exception for the thyroid pipeline.
    """

    def __init__(self, message="Pipeline Error"):
        super().__init__(message)


class ExtractionException(PipelineException):
    """
    Raised when AI extraction fails.
    """

    def __init__(self, message="Failed to extract report data"):
        super().__init__(message)


class ValidationException(PipelineException):
    """
    Raised when parsing or validation fails.
    """

    def __init__(self, message="Validation failed"):
        super().__init__(message)


class AnalysisException(PipelineException):
    """
    Raised when report analysis fails.
    """

    def __init__(self, message="Analysis failed"):
        super().__init__(message)


class HistoryException(PipelineException):
    """
    Raised when history generation fails.
    """

    def __init__(self, message="History generation failed"):
        super().__init__(message)