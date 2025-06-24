import streamlit as st
import speech_recognition as sr
import pyttsx3
import json
import os

TASK_FILE = "data/todo_db.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            return []  # If file is corrupted/empty, reset
    return []


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak now!")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        st.success(f"🗣️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        st.error("😕 Couldn't understand what you said.")
    except sr.RequestError:
        st.error("🚫 Speech recognition service is down.")
    return None

def run_voice_todo():
    st.subheader("🗣️ Voice-Controlled To-Do App")
    tasks = load_tasks()

    st.write("### 📝 Current Tasks")
    for i, task in enumerate(tasks, 1):
        st.write(f"{i}. {task}")

    if st.button("🎤 Speak to Add Task"):
        command = get_voice_command()
        if command:
            tasks.append(command)
            save_tasks(tasks)
            st.success("✅ Task added!")
            speak_text("Task added successfully.")

    if st.button("🗑️ Clear All Tasks"):
        tasks.clear()
        save_tasks(tasks)
        st.warning("⚠️ All tasks cleared!")
        speak_text("All tasks have been cleared.")
