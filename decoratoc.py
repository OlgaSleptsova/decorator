import datetime

def dec_log(pay_to_log):

    def decorator(old_faction):
        def new_faction(*args,**kwargs):
            resut = old_faction(*args,**kwargs)
            time = datetime.date.today()
            with open("text.txt", 'w', encoding='utf8') as f:
                f.writelines(f'Время и дата :{time}\n')
                f.writelines(f'Вызвана функция: {old_faction.__name__}\n')
                f.writelines(f'Аргументы функции:{args},{kwargs}\n')
                f.writelines(f'Возвращаемое значение:{resut}\n')
            return resut
        return new_faction
    return decorator
@dec_log(7)
def new_age(age):
    newage = age+10
    return newage
new_age(10)