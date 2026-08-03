import time

from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL
from ai.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt):

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text

    def generate_from_file(self, file_path, prompt):

        uploaded_file = self.client.files.upload(
            file=file_path
        )

        max_retries = 3

        for attempt in range(max_retries):

            try:

                response = self.client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=[
                        prompt,
                        uploaded_file
                    ]
                )

                return response.text

            except Exception as e:

                print(f"\nRetry {attempt + 1}/{max_retries}")
                print(f"Error: {e}")

                if attempt < max_retries - 1:
                    time.sleep(10)

        # This MUST be inside the function,
        # but OUTSIDE the for loop.
        raise Exception("Maximum retries exceeded.")