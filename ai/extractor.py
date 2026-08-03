from ai.providers.provider_factory import ProviderFactory


class AIExtractor:

    def __init__(self):
        self.provider = ProviderFactory.get_provider()

    def extract(self, file_path, prompt):
        """
        Generic AI extractor.
        Accepts any prompt.
        """

        return self.provider.generate_from_file(
            file_path,
            prompt
        )