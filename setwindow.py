


class SetWindow:
    def __init__(self, root, width: int, height: int, name="Новое окно"):
        self.__root = root
        self.__checkSize(width)
        self.__checkSize(height)
        self.__width = width   # !ширина окна
        self.__height = height   # !высота окна
        root.title(name)   # !заголовок
        root.resizable(False, False)   # !разрешение на изменения размера окна
        self.__wx = root.winfo_screenwidth()  # !ширина экрана монитора
        self.__wy = root.winfo_screenheight()  # !высота экрана монитора
        self.__x = int(self.__wx / 2 - self.__width / 2)  # !координата левой верхней точки окна
        self.__y = int(self.__wy / 2 - self.__height / 2)  # !координата левой верхней точки окна
        root.geometry(f"{self.__width}x{self.__height}+{self.__x}+{self.__y}")  # !размер и расположение окна

    def __checkSize(self, size):
        if not isinstance(size, int) or size < 200:
            raise TypeError("Размер окна должен быть целым числом, не меньше 200 pxl")

    def run(self):
        self.__root.mainloop()
