# Robust OpenAI wrapper supporting new & legacy SDK shapes.
import os, logging, asyncio
log = logging.getLogger("ai_client")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_client = None
client_type = None

def init_openai_client():
    global openai_client, client_type
    if not OPENAI_API_KEY:
        log.info("OPENAI_API_KEY not set; AI disabled")
        return
    try:
        # new-style client
        from openai import OpenAI
        openai_client = OpenAI(api_key=OPENAI_API_KEY)
        client_type = "new"
        log.info("Initialized new OpenAI client")
        return
    except Exception as e:
        log.debug("New OpenAI client init failed: %s", e)
    try:
        import openai as legacy
        legacy.api_key = OPENAI_API_KEY
        openai_client = legacy
        client_type = "legacy"
        log.info("Initialized legacy OpenAI module")
        return
    except Exception as e:
        log.debug("Legacy OpenAI init failed: %s", e)
    log.warning("OpenAI client could not be initialized; check openai package version")

async def ask_ai(prompt: str, lang: str = "en"):
    """Async wrapper: run sync call in thread to avoid blocking."""
    return await asyncio.to_thread(ask_ai_sync, prompt, lang)

def ask_ai_sync(prompt: str, lang: str = "en"):
    if not openai_client:
        return "(demo) AI not configured. Set OPENAI_API_KEY to enable real responses."
    try:
        if client_type == "new":
            resp = openai_client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}], temperature=0.4, max_tokens=300)
            return resp.choices[0].message["content"].strip()
        else:
            # legacy module path
            try:
                resp = openai_client.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":prompt}], temperature=0.4, max_tokens=300)
                choice = resp.choices[0]
                if isinstance(choice, dict) and "message" in choice:
                    return choice["message"]["content"].strip()
                elif hasattr(choice, "message"):
                    return choice.message["content"].strip()
            except Exception:
                resp = openai_client.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=200, temperature=0.4)
                return resp.choices[0].text.strip()
    except Exception as e:
        log.exception("OpenAI call failed: %s", e)
        return "(AI error) OpenAI request failed."
