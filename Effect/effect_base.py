import abc

class EffectBase:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def __call__(self, frame):
        raise NotImplementedError()
