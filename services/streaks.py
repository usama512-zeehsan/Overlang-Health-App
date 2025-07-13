import random

TIPS = [
    "Drink 2L of water daily",
    "Take a 10-min walk after meals",
    "Do breathing exercises before bed"
]

def get_daily_tip() -> str:
    return random.choice(TIPS)
