bindings = dict(  # Создание переменной для хранения ссылок на функции
    on_start=lambda: None,  # Установка функции при запуске
    on_frame=lambda: None,  # Установка функции обновления
    on_background=lambda: None  # Обновление функции фоновой активности
)


# Создание декораторов
def on_start(function): bindings.update({'on_start': function}); return function
def on_tick(function): bindings.update({'on_tick': function}); return function
def on_background(function): bindings.update({'on_background': function}); return function
