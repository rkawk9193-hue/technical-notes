import os
import json
import shutil
import datetime
import urllib.request
import urllib.error

import sys

# Configuration
DRAFTS_DIR = r"c:\Users\한병헌\Desktop\internal\note\drafts"
PROCESSED_DIR = r"c:\Users\한병헌\Desktop\internal\note\drafts\processed"
OUTPUT_DIR = r"c:\Users\한병헌\Desktop\internal\note\tech-blog\data\blog"
# Using gemini-flash-latest for better quota
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

def get_api_key():
    """Get Gemini API Key from args or user input."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    print("\n" + "="*50)
    print("🤖 Auto Blog Poster with Gemini")
    print("="*50)
    return input("Please enter your Gemini API Key: ").strip()

def generate_blog_post(api_key, content, original_filename):
    """Call Gemini API to generate MDX content."""
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    prompt = f"""
    You are an expert technical blog writer using Next.js and MDX.
    The following text is a draft or a raw script (filename: {original_filename}).
    
    Start directly with the Frontmatter. Do not wrap the output in markdown code blocks (like ```markdown).
    
    Please rewrite this content into a standardized, high-quality technical blog post in Korean.
    
    Requirements:
    1. Frontmatter at the top (YAML format) with:
       - title: A catchy and professional title based on the content.
       - date: '{today}'
       - tags: List of relevant tags (e.g., ['Oracle', 'SQL', 'Monitoring']).
       - draft: false
       - summary: A concise summary of what this script/content does.
    2. Content should be formatted in standard Markdown/MDX.
    3. If it contains SQL or code, use code blocks with language identifiers.
    4. **Crucial**: Explain the code/content. If it's a monitoring script, explain what it monitors and why it's important.
    5. Modernize or add "Best Practices" if applicable.
    
    Input Content:
    {content[:30000]} 
    """
    # Limit content to 30k chars to be safe with token limits for this simple script
    
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    req = urllib.request.Request(
        f"{API_ENDPOINT}?key={api_key}",
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            candidate = result.get('candidates', [{}])[0]
            text = candidate.get('content', {}).get('parts', [{}])[0].get('text', '')
            return text
    except urllib.error.HTTPError as e:
        print(f"Error calling Gemini API: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    if not os.path.exists(PROCESSED_DIR):
        os.makedirs(PROCESSED_DIR)

    files = [f for f in os.listdir(DRAFTS_DIR) if os.path.isfile(os.path.join(DRAFTS_DIR, f))]
    
    if not files:
        print(f"No files found in {DRAFTS_DIR}")
        return

    print(f"Found {len(files)} files in drafts folder.")
    api_key = get_api_key()
    
    if not api_key:
        print("API Key is required.")
        return

    for filename in files:
        file_path = os.path.join(DRAFTS_DIR, filename)
        
        print(f"\nProcessing: {filename}...")
        
        try:
            # Try reading with utf-8, fallback to latin-1 for binary-like or weird encodings
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            
            if not content.strip():
                print("  Skipping empty file.")
                continue

            blog_content = generate_blog_post(api_key, content, filename)
            
            if blog_content:
                # Generate a clean filename for the valid MDX
                slug = filename.lower().replace(" ", "-").replace(".", "-") + ".mdx"
                output_path = os.path.join(OUTPUT_DIR, slug)
                
                # Check for duplicate frontmatter or markdown blocks
                blog_content = blog_content.replace("```markdown", "").replace("```", "").strip()
                if not blog_content.startswith("---"):
                    # Fallback if AI didn't format correctly
                    blog_content = "---\ntitle: Generated Post\ndate: 2025-01-01\n---\n" + blog_content

                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(blog_content)
                
                print(f"  ✅ Blog post created: {output_path}")
                
                # Move to processed
                shutil.move(file_path, os.path.join(PROCESSED_DIR, filename))
                print(f"  Moved original to processed folder.")
            else:
                print("  ❌ Failed to generate content.")
                
        except Exception as e:
            print(f"  Error processing file: {e}")

    print("\nAll done!")

if __name__ == "__main__":
    main()
