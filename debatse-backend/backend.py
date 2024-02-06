from openai import OpenAI
from flask import Flask
app = Flask(__name__)
GPTResponse = OpenAI().chat.completions.create

class AIActor:
    def __init__():
        pass
    def getResponse(self):

        return GPTResponse(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": (
                    f"{ROLE_DESCS.get(self.role)} \n\n"
                )}
            ]
        )


class Judge(AIActor):
    def __init__(self):
        self.role = "Judge"

class Debater(AIActor):
    def __init__(self, personas: dict):
        self.role = "Debater"
        self.personas = personas

def getGradePersona(grade: int) -> str:
    SUFFIXES = {
        1: "st",
        2: "nd",
        3: "rd"
    }
    suffix = SUFFIXES.get(grade, "th")

    return "You read at a {grade}{suffix} grade level."

ROLE_DESCS = {
    "judge": (
        "You are a judge in a debate. Determine who is winning the debate "
        "and provide a score from 0-1 (0: Player B is completely winning, 1: Player A is completely winning)"
    ),
    "debater": (
        "You are in a debate. Write exactly 2 paragraphs."
    ),
}

DEBATER_PERSONA = {
    "grade": getGradePersona,
    "furry": "You use extremely exaggerated UwU furry speak.",
    "disinformation": (
        "You don't actually know ANYTHING about the topic at hand, but you pretend you do. "
        "Try to make up stuff as you go and disregard actual facts."
    ),
    "antoine_fandango": "Respond in the style of Anthony Fantano, the Internet's Busiest Music Nerd doing a live YouTube video.",
    "iamverysmart": "Where applicable, try to mention that you have an IQ of 150 and/or that you're a member of MENSA.",
    "ad_hominem": "Try to attack your opponent's character as much as possible."
}

@app.route("/response")
def response():
    pass
