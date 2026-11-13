# LifeEase:

**Live demo:** [lifeease.vercel.app](https://lifeease.vercel.app)

## The problem

Many elderly people live alone, struggle with typed interfaces, and need help that is both **personal** (their routine, family, preferences) and **safe** (health questions answered carefully, never invented). LifeEase lets them simply *talk*, in Hindi, to a companion that understands what kind of help they need and answers in a natural voice.

## How it works

```
 Voice (Hindi)
     │
     ▼
 Speech-to-text ──► Intent router (LLM + conversation context)
 (Sarvam saarika)        │
                         ├── internal  → personalized companion reply, grounded in the user's profile
                         ├── external  → live data: time (Google Time Zone API), weather (WeatherAPI),
                         │               general knowledge (Google Custom Search)
                         └── medical   → cautious, simple, empathetic health guidance
     │
     ▼
 Emotion detection on each utterance ──► shapes tone and proactive check-ins
     │
     ▼
 Text-to-speech (Sarvam bulbul) ──► spoken reply
```

Proactive triggers (APScheduler) let LifeEase start conversations, such as reminders or check-ins, instead of only waiting to be asked.

| Module | Role |
|---|---|
| `app.py` | Flask app and API routes (`/process-audio`, `/process-trigger-response`, `/process-location`) |
| `stt_service.py`, `tts_service.py` | Hindi speech-to-text and text-to-speech |
| `query_service.py` | Routes each query to internal, external or medical handling, using recent conversation history |
| `internal_query.py` | Personalized companion responses grounded in the user profile |
| `external_query.py` | Time, weather and general-knowledge lookups with location extraction |
| `medical_query.py` | Health questions, with input limits and a careful, simple response style |
| `emotion_service.py` | Classifies the emotional tone of each utterance |
| `trigger.py` | Scheduled, proactive check-ins |

## Why this approach

- **Route first, then answer.** A single prompt for everything mixes up tasks. Classifying intent first lets each handler use the right data source and the right level of caution. Medical questions get a stricter style than casual conversation.
- **Ground answers instead of trusting the LLM.** Time, weather and facts come from live APIs, and personal answers come from the user's profile, so the model has less room to make things up. In production, I extended this with a vector-retrieved healthcare knowledge base.
- **Voice-first, in the user's language.** For low-tech-literacy users, a spoken Hindi interface removes the biggest barrier to use.

## Results (production system)

The demo shows the architecture. These results come from the full production version at Boaient:

- Affective-state models built from speech and text **cut false caregiver alerts by 12% at 87.5% recall**.
- A/B and multivariate tests across **10,000+ user sessions** lifted average session time by **62%**.
- Onboarding funnel analysis showed stalled growth was an **activation** problem, not an acquisition one. The redesign raised activation from **57% to 76%**.
- API latency reduced by **28%**.
- Supports **48 languages** in production.

## Run it locally

```bash
git clone https://github.com/purvidalal/LifeEase_test.git
cd LifeEase_test
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then add your own API keys
python app.py
```

`data/sample_profile.xlsx` is a blank profile template. Fill it in with a fictional user to try personalized responses.

## Author

**Purvi Dalal**, MS in Data Science, Columbia University
