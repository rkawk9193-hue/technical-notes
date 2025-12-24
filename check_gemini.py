import urllib.request
import json
import sys

API_KEY = sys.argv[1]
URL = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

print(f"Checking models with key ending in ...{API_KEY[-4:]}")

try:
    with urllib.request.urlopen(URL) as response:
        data = json.loads(response.read().decode('utf-8'))
        print("✅ Success! Available models:")
        for model in data.get('models', []):
            if 'generateContent' in model.get('supportedGenerationMethods', []):
                print(f" - {model['name']}")
except urllib.error.HTTPError as e:
    print(f"❌ HTTP Error: {e.code} {e.reason}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"❌ Error: {e}")
