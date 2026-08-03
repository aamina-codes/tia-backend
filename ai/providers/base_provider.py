from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Base class for all AI providers.
    """

    @abstractmethod
    def generate(self, prompt: str):
        """
        Generate a response from the AI model.
        """
        pass

    @abstractmethod
    def generate_from_file(self, file_path: str, prompt: str):
        """
        Generate a response using an uploaded image/PDF.
        """
        pass