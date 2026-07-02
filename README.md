<p align="center">
  <h3 align="center">Amigo - Voice Assistant</h3>

  <p align="center">
    A Python-based console application that helps automate your daily tasks using voice commands.
  </p>
</p>

---

## About the Project

**Amigo** is a Python-based voice assistant that performs various daily tasks through voice commands. It uses speech recognition and text-to-speech technology to interact with the user and execute different operations.

### Features

* Search information on Wikipedia.
* Open YouTube, Spotify, and WhatsApp (if installed).
* Open websites directly from voice commands.
* Open local disk drives.
* Respond using voice feedback.
* Easily extend the assistant by adding your own custom commands.

---

## Built With

* Python 3
* pyttsx3
* SpeechRecognition
* Wikipedia
* Webbrowser
* OS Module

---

## Usage

1. Install all the required Python libraries.
2. Run the `amigo.py` file.
3. Speak a supported voice command when prompted.
4. The assistant will recognize your voice and perform the requested action.
5. You need to good internet connection for running this project.

To add your own custom command, include another `elif` block inside the main command handler:

```python
elif 'YOUR VOICE COMMAND' in query:
    speak("YOUR COMMAND")
    # Your Code Here
```

---

## Contributing

Contributions are always welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch to GitHub.
5. Open a Pull Request.

---

## Acknowledgements

* Python 3
* pyttsx3
* SpeechRecognition
* Wikipedia Library
* Webbrowser Module
* OS Module


## Author
- Shaily

## Internship ID
- SMI85485