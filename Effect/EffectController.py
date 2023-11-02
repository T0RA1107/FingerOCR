import cv2
import numpy as np
import threading
from playsound import playsound
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import sys
sys.path.append("./Effect")
import BindEffect

class EffectController:
    name2effect = BindEffect.name2effect

    def __init__(self):
        self.Effect = None
        self.processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
        self.model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

    def effect(self, frame):
        if self.Effect is None: return frame
        ret, effected_image = self.Effect(frame)
        if not ret:
            self.reset()
        return effected_image

    def reset(self):
        self.Effect = None

    def set_effect(self, effect_name):
        assert effect_name in self.name2effect, f"effect \"{effect_name}\" does not exist"
        self.Effect = self.name2effect[effect_name]()  # インスタンス化
        if self.Effect.type == "movie":
            if self.Effect.SE is not None:
                threading.Thread(target=playsound, args=(self.Effect.SE,)).start()

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
