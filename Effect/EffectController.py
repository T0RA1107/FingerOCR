import cv2
import numpy as np
import sys
sys.path.append("./Effect")
from pumpkin import pumpkin
from thunder import thunder, thunder_capture

class EffectController:
    name2effect = {
        "pumpkin": { "call": pumpkin, "type": "sticker" },
        "thunder": { "call": thunder, "type": "movie", "capture": thunder_capture }
    }

    def __init__(self):
        self.effect_name = None
        self.effect_cap = None

    def effect(self, frame):
        if self.effect_name is None: return frame
        Effect = self.name2effect[self.effect_name]["call"]
        if self.name2effect[self.effect_name]["type"] == "sticker":
            return Effect(frame)
        elif self.name2effect[self.effect_name]["type"] == "movie":
            ret, effect_image = self.effect_cap.read()
            if not ret:
                self.reset()
                return frame
            else:
                Effect = self.name2effect[self.effect_name]["call"]
                return Effect(frame, effect_image)

    def reset(self):
        if self.name2effect[self.effect_name]["type"] == "movie":
            self.effect_cap = None
        self.effect_name = None

    def set_effect(self, effect_name):
        assert effect_name in self.name2effect, f"effect \"{effect_name}\" does not exist"
        self.effect_name = effect_name
        if self.name2effect[effect_name]["type"] == "movie":
            self.effect_cap = self.name2effect[effect_name]["capture"]()
