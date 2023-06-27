class Rectangle:

    """Инициализируем обьект, присваиваем атрибуты: левый угол, ширину, высоту"""
    def __init__(self, angle_1, angle_2):
        self.angle_UL = (min(angle_1[0], angle_2[0]), max(angle_1[1], angle_2[1]))
        self.width = round(abs(angle_1[0] + (-angle_2[0])), 2)
        self.height = round(abs(angle_1[1] + (-angle_2[1])), 2)

    """Вычисление периметра"""
    def perimeter(self):
        self.P = round((2 * self.width + 2 * self.height), 2)
        return self.P
    
    """Вычисление площади"""
    def area(self):
        self.S = round(self.width * self.height, 2)
        return self.S
    
    """Вычисление местонахождения (левого угла)"""
    def get_pos(self):
        return self.angle_UL
    
    """Вычисление размеров: ширины и высоты"""
    def get_size(self):
        return self.width, self.height
    
    """Перемещения прямоугольника (левого края)"""
    def move(self, dx, dy):
        self.angle_UL = (round(self.angle_UL[0] + dx, 2), round(self.angle_UL[1] + dy, 2))

    """Перезапись размеров"""
    def resize(self, width, height):
        self.width = width
        self.height = height
    
    """Поворот: находим центр, меняем ширину и высоту, находим левый верхний угол"""
    def turn(self):
        self.middle = self.angle_UL[0] + (self.width / 2), self.angle_UL[1] - (self.height / 2)
        self.width, self.height = self.height, self.width
        self.angle_UL = self.middle[0] - (self.width / 2), self.middle[1] + (self.height / 2)
            
    """Изменение размеров: находим центр, изменяем ширину и высоту в factor раз, находим ВЛУ"""
    def scale(self, factor):
        self.middle = self.angle_UL[0] + (self.width / 2), self.angle_UL[1] - (self.height / 2)
        self.width = round(factor * self.width, 2)
        self.height = round(factor * self.height, 2)
        self.angle_UL = self.middle[0] - (self.width / 2), self.middle[1] + (self.height / 2)