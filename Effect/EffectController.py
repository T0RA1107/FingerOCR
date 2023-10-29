import cv2
import numpy as np
import threading
from playsound import playsound
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import sys
sys.path.append("./Effect")
from pumpkin import pumpkin
from thunder import thunder, thunder_capture, thunder_SE

class EffectController:
    name2effect = {
        "pumpkin": { "call": pumpkin, "type": "sticker" },
        "thunder": { "call": thunder, "type": "movie", "capture": thunder_capture, "SE": thunder_SE }
    }

    def __init__(self):
        self.effect_name = None
        self.effect_cap = None
        self.processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
        self.model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

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
            if "SE" in self.name2effect[effect_name]:
                threading.Thread(target=playsound, args=(self.name2effect[effect_name]["SE"](),)).start()

    def _recognize(self, image):
        pixel_values = self.processor(image, return_tensors="pt").pixel_values
        generated_ids = self.model.generate(pixel_values)

        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return generated_text

    def _pre_process(self, image):
        # 指文字をモデルが認識できる状態に修正する
        return image

    def _post_process(self, text):
        # ハミング距離などをもとに登録されたエフェクト名と近いものに修正できるなら修正する
        return text

    def recognize_finger_writing(self, image):
        image = self._pre_process(image)
        text = self._recognize(image)
        text = self._post_process(text)
        return text
