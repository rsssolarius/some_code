def result_accumulator(input_func, spisok=None):
    if spisok is None:
        spisok = []
        
    def output_func(*args, **kvargs):
        if "drop" in kvargs.values():
            spisok.append(input_func(*args))
            x = spisok.copy()
            spisok.clear()
            return x
        else:
            spisok.append(input_func(*args))
            return None
    
    return output_func