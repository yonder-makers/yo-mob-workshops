import os


class CounterModel:
    def __init__(self):
        self.counterValue = 16


class CounterView:
    def __init__(self, view_model):
        self.age_label = 'no-text'
        self.description_label = 'no-text'
        self.view_model = view_model

        self.view_model.on_property_changed = lambda p, v: self._on_property_changed(
            p, v)

    def _on_property_changed(self, property: str, value: str):
        if property == "age":
            self.age_label = value
        elif property == "description":
            self.description_label = value

        self._render()

    def _render(self):
        print(f"""
            Age: {self.age_label} 
            Description: {self.description_label}
        """)

    def do_user_interaction(self):
        while True:
            action = input("Your input:")
            os.system("clear")
            self.view_model.notify(action)


class CounterViewModel:
    def __init__(self):
        self.model = CounterModel()
        self.on_property_changed = None

    def set_age(self, value):
        if self.model.counterValue == value:
            return

        old_description = self.get_description()

        self.model.counterValue = value
        self.on_property_changed("age", self.model.counterValue)

        new_description = self.get_description()

        if old_description != new_description:
            self.on_property_changed("description", new_description)

    def get_age(self):
        return self.model.counterValue

    def get_description(self):
        if self.get_age() >= 18:
            return "Adult"

        else:
            return "Minor"

    def notify(self, action: str):
        if action == "increment":
            self.set_age(self.get_age() + 1)

        elif action == "decrement":
            self.set_age(self.get_age() - 1)

        else:
            pass


class App():
    def run(self):
        viewModel = CounterViewModel()
        view = CounterView(viewModel)

        view.do_user_interaction()


app = App()
app.run()
