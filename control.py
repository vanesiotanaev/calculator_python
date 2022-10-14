import view
import model

def button_click():
    expression = view.get_expression()
    model.init(expression)
    result = model.operation(expression)
    view.result_output(expression, result)