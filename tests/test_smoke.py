
import importlib, os

from dotenv import load_dotenv

def test_package_import():
    assert importlib.import_module("ai_90") is not None

def test_api_key_is_configured():
    load_dotenv()
    key = os.getenv("ANTHROPIC_API_KEY", "")
    assert key.startswith("sk-"), "Put your key in .env (never commit it)"
