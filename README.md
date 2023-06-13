# Alita

The goal of this project is to create a voice assistant, similar to [Neuro Sama](https://www.youtube.com/watch?v=KvRQoVcdY2s), capable of providing oral responses like an AI, while also performing basic actions like Google Assistant.

## Installation
Make you sur [Python](https://www.python.org/) 3.10 is installed on your computer (other version may work but I didn't test it).

Clone the repository:
```bash
git clone https://github.com/EnzoDeg40/Alita.git
```

Move to the project folder:
```bash
cd Alita
```

Change to develop branch if you want to contribute or test new features:
```bash
git checkout dev
```

Download any model on [alphacephei](https://alphacephei.com/vosk/models) to [models folder](models). I use `vosk-model-fr` for production and `vosk-model-small-fr` for development.

Install the requirements:
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Roadmap
- [x] Voice recognition
- [ ] Connect to an AI like [alpaca_lora](https://github.com/tloen/alpaca-lora)
- [ ] Possibility to use My AI (snapchat) to get faster response
- [ ] Improve text to speech