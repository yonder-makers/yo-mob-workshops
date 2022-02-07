class CounterModel:
    def __init__(self):
        self.counterValue = 0


class CounterView:
    def __init__(self, controller):
        self.controller = controller

    def render(self, model: CounterModel):
        print(f"Counter value: {model.counterValue}")

        action = input("Your input:")
        self.controller.sendAction(action)


class CounterService:
    def increment(self, model: CounterModel):
        model.counterValue += 1

    def decrement(self, model: CounterModel):
        model.counterValue -= 1


class CounterController:
    def __init__(self):
        self.model = CounterModel()
        self.service = CounterService()
        self.view = CounterView()

    def sendAction(self, action: str):
        if action == "increment":
            self.service.increment(self.model)

        elif action == "decrement":
            self.service.decrement(self.model)

        else:
            pass

        self.view.render(self.model)


# class DrawingFramework:
#     def __init__(self):
#         self.content = "Nothing to render"

#     def set_content_to_render(self, content):
#         self.content = content

#     def get_user_interaction(self, content):


class App():
    def run(self):
        controller = CounterController()
        while True:
            action = input("Your input:")
            controller.sendAction(action)


app = App()
app.run()
