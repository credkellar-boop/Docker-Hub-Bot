import os
import logging
from google import genai

logger = logging.getLogger(__name__)

class BrainInference:
    def __init__(self):
        # Fetch the key from environment variables
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.client = None
        
        # BYPASS: If key is missing, log a warning instead of raising an error and crashing
        if not self.api_key:
            logger.warning("GEMINI_API_KEY environment variable is missing. Brain Module will run in bypass mode.")
            self.model_ready = False
        else:
            try:
                # Correct initialization syntax for the modern google-genai library
                self.client = genai.Client(api_key=self.api_key)
                self.model_ready = True
            except Exception as e:
                logger.error(f"Failed to initialize Gemini Client: {e}")
                self.model_ready = False

    def generate_environment(self, query):
        """Queries Gemini to construct highly optimized container configurations."""
        print(f"[*] Brain Module: Analyzing architecture requirements for: '{query}'")
        
        # Cleanly skip if the user doesn't have a plugged-in key
        if not self.model_ready or not self.client:
            print("[!] Gemini feature skipped: No operational API key detected.")
            return "---DOCKERFILE---\n# AI Generation bypassed. Set GEMINI_API_KEY to activate.\n"

        prompt = f"""
        You are a systems architecture bot. Search for the optimal official Docker image for '{query}'.

        Generate a robust configuration including:
        1. A 'Dockerfile' utilizing strict layer caching optimizations.
        2. A '.dockerignore' to prevent unnecessary payload bloat.
        3. A 'docker-compose.yml' file to securely orchestrate the environment.
        OUTPUT ONLY the raw file contents wrapped in tags like ---DOCKERFILE---, ---COMPOSE---.
        """

        try:
            # Modern generation execution syntax
            response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            return response.text
        except Exception as e:
            logger.error(f"Failed to communicate with Gemini API: {e}")
            return f"# Error during AI generation loop: {e}"
