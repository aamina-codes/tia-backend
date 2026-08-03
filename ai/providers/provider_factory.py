from ai.providers.gemini_provider import GeminiProvider


class ProviderFactory:

    @staticmethod
    def get_provider(provider_name="gemini"):

        if provider_name.lower() == "gemini":

            return GeminiProvider()

        raise ValueError(
            f"Unknown provider: {provider_name}"
        )