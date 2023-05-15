import random

def classify_frame(frame: str) -> bool:
    """Classifies a frame as gameplay or non-gameplay"""
    return random.choice([True, False])