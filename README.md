# 🧠 Reddit User Persona Generator using Groq LLaMA3

This tool takes a Reddit username, scrapes their public posts and comments, and uses Groq’s blazing-fast LLaMA3 API to generate a structured **User Persona** — like those used in UX research.

---

## 📸 Sample Output

Age: 25–30
Occupation: Remote Software Engineer
Location: UK
Behaviour & Habits: Frequently discusses health-conscious food options and productivity tools (e.g., “I hate when apps don't show healthy options.”)
Frustrations: Lack of accessible healthy eating choices
Motivations: Improve lifestyle and productivity balance
Goals & Needs: Stay healthy while working remotely
Personality: Likely INTJ — goal-oriented, analytical, wellness-focused

---

## 🚀 Features

✅ Scrapes Reddit user activity (posts + comments)  
✅ Summarizes into a complete user persona  
✅ Uses **Groq’s LLaMA3-70B** model (faster than GPT)  
✅ Output saved as `.txt` in `output/` folder  
✅ Minimal setup, clean architecture

---

## 📁 Project Structure

reddit_second/
├── scripts/
│ └── main.py # Main Python script
├── output/ # Auto-created: Stores persona outputs
└── README.md # You're reading it!

---

## ⚙️ Requirements

```bash
pip install requests beautifulsoup4 groq

## 🔐 API Key Setup
You need a Groq API key

Edit this line in main.py:

python
client = Groq(api_key="your_groq_api_key_here")

Then in main.py:

python
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

How to Run
cd reddit-second/scripts
python main.py
Then enter any Reddit username when prompted:
🔹 Enter Reddit username:xxx

---

🙋‍♀️ Author
Built with ❤️ by Vaishnavi Singh

---
```
