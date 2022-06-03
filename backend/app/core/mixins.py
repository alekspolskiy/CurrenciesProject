class ClassShortMixin:
    def __str__(self):
        """
        for errors better understanding
        :return:
        """
        return self.__class__.__name__.lower()


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class IterMixin(object):
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value
