class Fraction():

    """Инициализируем поля (атрибуты):
       Для двух переданных чисел,
       Затем для переданной строки"""
    def __init__(self, *args, _znak_drobi=True):
        if isinstance(args[0], int):
            if args[0] < 0 and args[1] < 0 or args[0] > 0 and args[1] > 0:
                self._znak_drobi = True
            else:
                self._znak_drobi = False
            if _znak_drobi:
                pass
            else:
                self._znak_drobi = not self._znak_drobi
            self._x_1 = abs(args[0])
            self._y_1 = abs(args[1])
            while self._x_1 != self._y_1:
                if self._x_1 > self._y_1:
                    self._x_1 -= self._y_1
                else:
                    self._y_1 -= self._x_1
            self.ch = int(abs(args[0]) / self._x_1)
            self.zn = int(abs(args[1]) / self._x_1)

        else:
            if (int(args[0].split('/')[0]) < 0 and int(args[0].split('/')[1]) < 0 
               or int(args[0].split('/')[0]) > 0 and int(args[0].split('/')[1]) > 0):
                self._znak_drobi = True
            else:
                self._znak_drobi = False
            if _znak_drobi is False:
                self._znak_drobi = not self._znak_drobi
            else:
                pass
            self._x_1 = abs(int(args[0].split('/')[0]))
            self._y_1 = abs(int(args[0].split('/')[1]))
            while self._x_1 != self._y_1:
                if self._x_1 > self._y_1:
                    self._x_1 -= self._y_1
                else:
                    self._y_1 -= self._x_1
            self.ch = int(abs(int(args[0].split('/')[0])) / self._x_1)
            self.zn = int(abs(int(args[0].split('/')[1])) / self._x_1)
    
    """Изменение числителя"""
    def numerator(self, other=None):
        if isinstance(other, type(None)):
            return self.ch
        else:
            if other > 0:
                pass
            else:
                self._znak_drobi = not self._znak_drobi
            self._x_1 = abs(other)
            self._y_1 = self.zn
            while self._x_1 != self._y_1:
                if self._x_1 > self._y_1:
                    self._x_1 -= self._y_1
                else:
                    self._y_1 -= self._x_1
        self.ch = int(abs(other) / self._x_1)
        self.zn = int(self.zn / self._x_1)
        return self.ch, self.zn
    
    """Изменение знаменателя"""
    def denominator(self, other=None):
        if isinstance(other, type(None)):
            return self.zn
        else:
            if other > 0:
                pass
            else:
                self._znak_drobi = not self._znak_drobi
            self._x_1 = self.ch
            self._y_1 = abs(other)
            while self._x_1 != self._y_1:
                if self._x_1 > self._y_1:
                    self._x_1 -= self._y_1
                else:
                    self._y_1 -= self._x_1
        self.ch = int(self.ch / self._x_1)
        self.zn = int(abs(other) / self._x_1)
        return self.ch, self.zn
    
    """Унарный минус"""
    def __neg__(self):
        _neg_self = Fraction(self.ch, self.zn, not self._znak_drobi)
        return _neg_self

    """Строчный вывод"""
    def __str__(self):
        if self._znak_drobi:
            return f'{self.ch}/{self.zn}'
        else:
            return f'-{self.ch}/{self.zn}'

    """Репрезентация"""
    def __repr__(self):
        if self._znak_drobi:
            return f"Fraction('{self.ch}/{self.zn}')"
        else:
            return f"Fraction('-{self.ch}/{self.zn}')"
        
    """Создание новой дроби из суммы двух переданных"""    
    def __add__(self, other):
        _new_ch_S = abs(self.ch * other.zn)
        _new_ch_O = abs(other.ch * self.zn)
        _new_zn = abs(self.zn * other.zn)
        if self._znak_drobi:
            if other._znak_drobi:
                _new_drob = Fraction(_new_ch_S + _new_ch_O, _new_zn)              # = x + y
            else:
                if _new_ch_S > _new_ch_O:
                    _new_drob = Fraction(_new_ch_S - _new_ch_O, _new_zn)          # = X + -y
                else:
                    _new_drob = Fraction(_new_ch_O - _new_ch_S, _new_zn,
                                         _znak_drobi=False)                      # = x + -Y
        else:
            if other._znak_drobi:
                if _new_ch_S > _new_ch_O:
                    _new_drob = Fraction(_new_ch_S - _new_ch_O, _new_zn,
                                         _znak_drobi=False)                      # = -X + y
                else:
                    _new_drob = Fraction(_new_ch_O - _new_ch_S, _new_zn)         # = -x + Y
            else:
                _new_drob = Fraction(_new_ch_S + _new_ch_O, _new_zn,
                                     _znak_drobi=False)                          # = -x + -y
        return _new_drob
    
    """Создание новой дроби из разницы двух переданных"""   
    def __sub__(self, other):
        _new_ch_S = abs(self.ch * other.zn)
        _new_ch_O = abs(other.ch * self.zn)
        _new_zn = abs(self.zn * other.zn)
        if self._znak_drobi:
            if other._znak_drobi:
                if _new_ch_S > _new_ch_O:
                    _new_drob = Fraction(_new_ch_S - _new_ch_O, 
                                         _new_zn)                       # = x - y, x > y
                else:
                    _new_drob = Fraction(_new_ch_O - _new_ch_S, 
                                         _new_zn, _znak_drobi=False)    # = x - y, x < y
            else:
                _new_drob = Fraction(_new_ch_S + _new_ch_O, _new_zn)    # = x - -y
        else:
            if other._znak_drobi:
                _new_drob = Fraction(_new_ch_S + _new_ch_O, _new_zn, 
                                     _znak_drobi=False)                 # = -x - y
            else:
                if _new_ch_S > _new_ch_O:
                    _new_drob = Fraction(_new_ch_S - _new_ch_O, _new_zn, 
                                         _znak_drobi=False)             # = -x - -y, x > y
                else:
                    _new_drob = Fraction(_new_ch_O - _new_ch_S, 
                                         _new_zn)                       # = -x - -y, x < y 
        return _new_drob
    
    """Замена старой дроби путем суммирования с другой"""
    def __iadd__(self, other):
        _new_ch_S = abs(self.ch * other.zn)
        _new_ch_O = abs(other.ch * self.zn)
        _new_zn = abs(self.zn * other.zn)
        if self._znak_drobi:
            if other._znak_drobi:
                self.ch = _new_ch_S + _new_ch_O
                self.zn = _new_zn                     # x += y
            else:
                if _new_ch_S > _new_ch_O:
                    self.ch = _new_ch_S - _new_ch_O
                    self.zn = _new_zn                 # X += -y
                else:
                    self.ch = _new_ch_O - _new_ch_S
                    self.zn = _new_zn
                    self._znak_drobi = False          # x += -Y
        else:
            if other._znak_drobi:
                if _new_ch_S > _new_ch_O:             # -X += y
                    self.ch = _new_ch_S - _new_ch_O
                    self.zn = _new_zn        
                else:
                    self.ch = _new_ch_O - _new_ch_S
                    self.zn = _new_zn
                    self._znak_drobi = True                 # -x +=  Y
            else:
                self.ch = _new_ch_S + _new_ch_O
                self.zn = _new_zn
                self._znak_drobi = False              # -x += -y
        # Сокращение        
        self._x_1 = self.ch
        self._y_1 = self.zn
        while self._x_1 != self._y_1:
            if self._x_1 > self._y_1:
                self._x_1 -= self._y_1
            else:
                self._y_1 -= self._x_1
        self.ch = int(self.ch / self._x_1)
        self.zn = int(self.zn / self._x_1)
        return self
    
    """Замена старой дроби путем вычитания из нее другой"""
    def __isub__(self, other):
        _new_ch_S = abs(self.ch * other.zn)
        _new_ch_O = abs(other.ch * self.zn)
        _new_zn = abs(self.zn * other.zn)
        if self._znak_drobi:
            if other._znak_drobi:
                if _new_ch_S > _new_ch_O:                # X -= y
                    self.ch = _new_ch_S - _new_ch_O 
                    self.zn = _new_zn
                else:                                    # x -= Y
                    self.ch = _new_ch_O - _new_ch_S
                    self.zn = _new_zn
                    self._znak_drobi = False
            else:                                        # x -= -y
                self.ch = _new_ch_S + _new_ch_O
                self.zn = _new_zn
        else:
            if other._znak_drobi:                        # -x -= y
                self.ch = _new_ch_S + _new_ch_O
                self.zn = _new_zn
            else:                                         
                if _new_ch_S > _new_ch_O:                # -X -= -y
                    self.ch = _new_ch_S - _new_ch_O
                    self.zn = _new_zn
                else:                                    # -x -= -Y
                    self.ch = _new_ch_O - _new_ch_S
                    self.zn = _new_zn
                    self._znak_drobi = True
        # Сокращение
        self._x_1 = self.ch
        self._y_1 = self.zn
        while self._x_1 != self._y_1:
            if self._x_1 > self._y_1:
                self._x_1 -= self._y_1
            else:
                self._y_1 -= self._x_1
        self.ch = int(self.ch / self._x_1)
        self.zn = int(self.zn / self._x_1)
        return self