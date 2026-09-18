import os
 
# Instantiate the OpenAI client
client = OpenAI()
 
def detect_emotion(sentence):
    # Send a request to GPT-4 for emotion detection
    completion = client.chat.completions.create(
        model="gpt-4",  # You can use "gpt-4-turbo" if you prefer
        messages=[
            {"role": "system", "content": "You are a Hindi emotion classifier. Classify the emotion as Happy, Calm, Sad, Celebration Preparation, or other relevant emotions."},
            {"role": "user", "content": f"Sentence: {sentence}"}
        ]
    )
    # Access the response content
    # Changed from completion.choices[0].message["content"] to completion.choices[0].message.content
    emotion = completion.choices[0].message.content.strip()
    return emotion
