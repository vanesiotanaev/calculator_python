import view
import model
import log

def button_click():
    expression = view.get_expression()
    model.init(expression)
    result = model.operation(expression)
    view.result_output(expression, result)
    log.write_log(expression, result)