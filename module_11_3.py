def introspection_info(obj):
    sinfo = {}
    # Определяем тип объекта
    sinfo['type'] = type(obj).__name__
    # Определяем атрибуты объекта
    sinfo['attributes'] = dir(obj)
    # Определяем методы объекта
    sinfo['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    # Определяем модуль, к которому принадлежит объект
    sinfo['module'] = obj.__module__
    # Другие интересные свойства (например, если это класс, то его базовые классы)
    if isinstance(obj, type):
        sinfo['base_classes'] = [base.__name__ for base in obj.__bases__]
    return sinfo

    # Пример класса для тестирования
class SampleClass:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}!"

    # Создаем объект класса
sample_object = SampleClass("Alice")

    # Получаем информацию об объекте
sinfo =introspection_info(sample_object)

    # Выводим информацию
for key, value in sinfo.items():
    print(f"{key}: {value}\n")