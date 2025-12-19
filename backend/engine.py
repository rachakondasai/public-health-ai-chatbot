import re
from datetime import datetime

DISCLAIMER = (
    "⚠️ I’m a public-health awareness bot, not a doctor. "
    "I provide general info, prevention tips, and guidance on when to seek care."
)

EMERGENCY_FLAGS = [
    r"chest pain", r"trouble breathing", r"severe bleeding",
    r"unconscious", r"seizure", r"stroke", r"suicid", r"self harm"
]

TOPICS = {
    "dengue": {
        "about": "Dengue is a viral disease spread by Aedes mosquitoes.",
        "symptoms": ["High fever", "Headache", "Joint pain", "Rash"],
        "prevention": ["Avoid stagnant water", "Use mosquito nets", "Apply repellent"],
        "seek": ["Bleeding", "Severe abdominal pain", "Persistent vomiting"]
    },
    "malaria": {
        "about": "Malaria is caused by parasites spread by mosquitoes.",
        "symptoms": ["Fever with chills", "Sweating", "Headache"],
        "prevention": ["Mosquito nets", "Repellents", "Indoor spraying"],
        "seek": ["High fever", "Confusion", "Weakness"]
    },
    "covid": {
        "about": "COVID-19 is a respiratory illness caused by coronavirus.",
        "symptoms": ["Fever", "Cough", "Loss of smell", "Breathing difficulty"],
        "prevention": ["Vaccination", "Masks", "Ventilation"],
        "seek": ["Breathing difficulty", "Chest pain"]
    }
}

def build_response(text: str):
    t = text.lower()
    for f in EMERGENCY_FLAGS:
        if re.search(f, t):
            return {
                "reply": DISCLAIMER + "\n\n🚨 Possible emergency detected. Seek medical help immediately.",
                "topic": "emergency",
                "safety": "high",
                "timestamp": datetime.now().isoformat(timespec="seconds")
            }

    for k, v in TOPICS.items():
        if k in t:
            return {
                "reply": (
                    DISCLAIMER + f"\n\n{k.upper()}\n"
                    f"About: {v['about']}\n"
                    f"Symptoms: {', '.join(v['symptoms'])}\n"
                    f"Prevention: {', '.join(v['prevention'])}\n"
                    f"When to seek care: {', '.join(v['seek'])}"
                ),
                "topic": k,
                "safety": "normal",
                "timestamp": datetime.now().isoformat(timespec="seconds")
            }

    return {
        "reply": DISCLAIMER + "\n\nAsk about dengue, malaria, or covid.",
        "topic": None,
        "safety": "normal",
        "timestamp": datetime.now().isoformat(timespec="seconds")
    }
