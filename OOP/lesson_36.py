class Meta(type):

    def create_local_attrs(self, *args, **kwargs):
        for key, val in self.class_attrs.items():
            self.__dict__[key] = val

    def __init__(cls, name, base, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = 'header'
    content = 'content'
    photo = 'path to photo'


w = Women()
print(w.__dict__)