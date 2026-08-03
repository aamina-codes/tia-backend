from ai.providers.provider_factory import ProviderFactory

provider = ProviderFactory.get_provider()

print(provider.generate("Say Hello"))