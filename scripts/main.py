import requests
from bs4 import BeautifulSoup
import time
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_user_data(username):
    base_url = f"https://www.reddit.com/user/{username}"
    urls = [f"{base_url}/comments/", f"{base_url}/submitted/"]
    results = []

    for url in urls:
        try:
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.text, 'html.parser')
            posts = soup.find_all("div", class_="md")

            for post in posts:
                text = post.get_text().strip()
                if len(text) > 30:
                    results.append(text)
        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")
        time.sleep(1)

    return results[:20]

def generate_prompt(username, texts):
    combined = "\n\n".join(texts)
    prompt = f"""
You are a UX researcher. Based on the following Reddit activity, create a detailed user persona in this format:

- Age
- Occupation
- Location
- Behaviour & Habits (cite data)
- Frustrations (cite data)
- Motivations (cite data)
- Goals & Needs (cite data)
- Personality (MBTI-style + examples)

Reddit User: u/{username}

User’s Reddit Activity:
{combined}
"""
    return prompt

def generate_persona(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a UX research expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error generating persona: {e}"

def save_to_file(username, content):
    os.makedirs("output", exist_ok=True)
    filename = f"output/{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Persona saved to: {filename}")

if __name__ == "__main__":
    username = input("🔹 Enter Reddit username (e.g. kojied): ").strip()
    data = scrape_user_data(username)

    if not data:
        print("⚠️ Not enough data found. Try another user.")
    else:
        prompt = generate_prompt(username, data)
        persona = generate_persona(prompt)
        save_to_file(username, persona)
