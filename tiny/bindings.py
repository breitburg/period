bindings: dict = dict(  # Setting bindings variable for storing
    on_start=lambda: None,  # Setting startup function
    on_frame=lambda: None,  # Setting frame-update function
    on_background=lambda: None  # Setting background function
)


# Setting decorators
def on_start(function): bindings.update({'on_start': function}); return function
def on_update(function): bindings.update({'on_update': function}); return function
def on_background(function): bindings.update({'on_background': function}); return function
