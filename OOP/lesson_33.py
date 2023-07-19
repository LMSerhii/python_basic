class Women:
    title = "объект класса для поля title"
    foto = "объект класса для поля photo"
    ordering = "объект класс для поля  ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access


w = Women('root', '12345')
print(w.__dict__)
print(w.meta.__dict__)
