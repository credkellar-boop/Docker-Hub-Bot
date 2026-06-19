import os
from google import genai

class BrainInference:
    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def generate_environment(self, query):
        """Queries Gemini to construct highly optimized container configurations."""
        print(f"[*] Brain Module: Analyzing architecture requirements for: '{query}'")
        
        prompt = f"""
        You are a systems architecture bot. Search for the optimal official Docker image for '{query}'.
        Generate a robust configuration including:
        1. A 'Dockerfile' utilizing strict layer caching optimizations.
        2. A '.dockerignore'.
        3. A 'docker-compose.yml' file for secure orchestration.
        Output ONLY the raw file contents wrapped in tags like ---DOCKERFILE---, ---COMPOSE---.
        """
        response = self.model.generate_content(prompt)
        return response.text
