# FastAPI endpoints for vision, speech, recipes — minimal implementations / stubs.
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from backend.ai_client import ask_ai, init_openai_client
import os

app = FastAPI(title="OmniMind Backend")
init_openai_client()

class RecipeRequest(BaseModel):
    goal: str = "general"
    diet: str = "any"
    pantry: list = []

@app.get("/health")
async def health():
    return {"status":"ok"}

@app.post("/recipes/generate")
async def gen_recipes(req: RecipeRequest):
    prompt = f"Generate 3 recipes for goal:{req.goal} diet:{req.diet} pantry:{','.join(req.pantry)}. Return concise recipes with kcal and steps."
    resp = await ask_ai(prompt, "en")
    return {"recipes_raw": resp}
