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
        load = True
        if load:
            threading.Thread(target=self.load, args=()).start()

    def load(self):
        print("start loading model")
        self.processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
        self.model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
        print("model loaded!!!")

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
            if hasattr(self.Effect, "SE"):
                threading.Thread(target=playsound, args=(self.Effect.SE,)).start()

    def is_effect(self, text):
        return text in self.name2effect

    def _recognize(self, image):
        pixel_values = self.processor(image, return_tensors="pt").pixel_values
        generated_ids = self.model.generate(pixel_values)

        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return generated_text

    def _pre_process(self, image):
        # 指文字をモデルが認識できる状態に修正する
        mask = np.where(np.any(image > 0, axis=2))
        ret = np.zeros_like(image, np.uint8)
        ret[mask[0], mask[1]] = 255
        return ret

    def _post_process(self, text):
        # ハミング距離などをもとに登録されたエフェクト名と近いものに修正できるなら修正する
        max_loss = 100
        pred = text
        for effect_name in self.name2effect.keys():
            loss = abs(len(effect_name) - len(text))
            for i in range(min(len(effect_name), len(text))):
                if effect_name[i] != text[i]:
                    loss += 1
            if loss < max_loss:
                max_loss = loss
                pred = effect_name
        if max_loss > 5:
            return text
        else:
            return pred

    def recognize_finger_writing(self, image):
        image = self._pre_process(image)
        text = self._recognize(image)
        print("raw prediction:", text)
        text = self._post_process(text)
        return text
