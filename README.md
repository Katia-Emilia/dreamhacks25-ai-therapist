About the Project – Thea: Your AI Therapist

💡 Inspiration

A major gap in the market is making mental health support more accessible to people who find difficulties in cost, stigma, or availability. This is when we realized we needed to build an AI therapist which anyone and everyone could talk to, in a safe, private, and judgement-free space. Thea is an intelligent companion which allows users to text, voice, or video their thoughts in a supportive and safe digital environment.

As part of the team theme for this Web3 hackathon, we built Thea as a web app with privacy first, using Flask with plans to integrate decentralized identity and data handling in later iterations.

🌐 What We Built

Thea is a browser accessible AI therapy companion powered by Flask. The user interface includes:

An onboarding consent form clarifying Thea is not a licensed therapist.

Name input and mode selection:

✅ Text Chat

✅ Text Chat with Emotion Recognition

✅ Voice Chat

Different modes make use of different aspects of AI:

Text Chat: responses using NLP sentiment analysis (VADER).

Emotion Detection: webcam based mood detection performed in real-time by DeepFace + sentiment fusion.

Voice Chat: Speech based conversation using STT and TTS.

🔧 How It Works

Flask Backend: Controls session navigation, user input control, AI response management.

NLP (VADER): sentiment analysis of chat messages.

Computer Vision: Performs emotion detection via webcam using OpenCV and DeepFace.

Speech Handling: Natural interaction is facilitated through STT (speech recognition) and TTS (pyttsx3).

🔐 Web3 Relevance

At this moment, Thea is hosted on Flask. As part of the future roadmap:

Decentralized identity (DID): Enables users to safely control their session data.

Local-first processing: Strives to keep emotion analysis private on the client’s side.

Zero-knowledge interaction models: Provide support for the anonymized emotional assistance.

🚧 Challenges Faced

Designing a multi-modal responsive AI within a Flask application

Facilitating real-time voice and webcam input in-browser

Designing a safe and coherent interface, especially in relation to Thea’s identity as a non-human entity

Integrating multiple AI capabilities into a low footprint web service

✅ What We Learned

Integrating AI features into web applications using Flask

Real-time implementation of sentiment and facial emotion recognition models

User consent, app accessibility, and trust dynamics in mental health applications

Preliminary considerations for privacy-by-design Web3 enabled solutions
