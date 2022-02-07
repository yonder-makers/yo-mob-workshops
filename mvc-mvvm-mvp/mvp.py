class CounterModel:
    def __init__(self):
        self.counterValue = 16


class ICounterView:
    def set_age_label_text(self, value: str):
        raise NotImplementedError()

    def set_description_label_text(self, value: str):
        raise NotImplementedError()


class CounterView:
    def __init__(self, presenter):
        self.age_label = 'no-text'
        self.description_label = 'no-text'
        self.presenter = presenter
        self._render()

    def set_age_label_text(self, value: str):
        self.age_label = value
        self._render()

    def set_description_label_text(self, value: str):
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
            self.presenter.notify(action)


class CounterService:
    def increment(self, model: CounterModel):
        model.counterValue += 1

    def decrement(self, model: CounterModel):
        model.counterValue -= 1


class CounterPresenter:
    def __init__(self):
        self.model = CounterModel()
        self.service = CounterService()
        self.view = None

    def notify(self, action: str):
        if action == "increment":
            self.service.increment(self.model)

        elif action == "decrement":
            self.service.decrement(self.model)

        else:
            pass

        self.view.set_age_label_text(str(self.model.counterValue))
        if self.model.counterValue >= 18:
            self.view.set_description_label_text("Adult")
        else:
            self.view.set_description_label_text("Minor")


class App():
    def run(self):
        controller = CounterPresenter()
        view = CounterView(controller)
        controller.view = view

        view.do_user_interaction()


app = App()
app.run()
