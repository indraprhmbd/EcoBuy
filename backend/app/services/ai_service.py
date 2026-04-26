import json
import httpx
from app.core.config import settings

class AIService:
    def __init__(self):
        self.hf_api_key = getattr(settings, "HUGGINGFACE_API_KEY", None)
        self.hf_model_id = getattr(settings, "HF_MODEL_ID", "google/vit-base-patch16-224")
        self.gemini_api_key = getattr(settings, "GEMINI_API_KEY", None)

    async def analyze_waste(self, image_data: bytes) -> dict:
        # 1. Try Hugging Face if configured (Best for specific fine-tuned models)
        if self.hf_api_key:
            try:
                headers = {"Authorization": f"Bearer {self.hf_api_key}"}
                api_url = f"https://api-inference.huggingface.co/models/{self.hf_model_id}"
                
                async with httpx.AsyncClient() as client:
                    response = await client.post(api_url, headers=headers, content=image_data)
                    
                if response.status_code == 200:
                    results = response.json()
                    # Map HF Image Classification results to our schema
                    if isinstance(results, list) and len(results) > 0:
                        top_label = results[0]['label']
                        confidence = results[0]['score']
                        
                        return {
                            "type": top_label,
                            "estimated_weight": 1.0, # Placeholder weight
                            "grade": "A" if confidence > 0.8 else "B",
                            "confidence": confidence
                        }
            except Exception as e:
                print(f"HF Analysis Error: {e}")

        # 2. Try Gemini (Powerful Zero-Shot Vision)
        if self.gemini_api_key:
            try:
                import google.generativeai as genai
                from PIL import Image
                import io
                
                genai.configure(api_key=self.gemini_api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                img = Image.open(io.BytesIO(image_data))
                prompt = """
                Analyze this image of waste. Return a JSON object with:
                - type: The category (e.g. 'Kertas', 'Plastik', 'Logam')
                - estimated_weight: Float in kg
                - grade: 'A', 'B', or 'C'
                - confidence: Float 0-1
                Return ONLY JSON.
                """
                response = model.generate_content([prompt, img])
                text = response.text.strip()
                if "```json" in text:
                    text = text.split("```json")[1].split("```")[0].strip()
                return json.loads(text)
            except Exception as e:
                print(f"Gemini Analysis Error: {e}")

        # 3. Fallback
        return {
            "type": "Kertas (Kardus)",
            "estimated_weight": 5.0,
            "grade": "A",
            "confidence": 0.95
        }

