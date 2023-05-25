from functools import partial


class CalculatorController:

    def __init__(self, model, view):
        self._model = model # function to calculate result
        self._view = view # class

        self._connectSignals()

    def _calculateResult(self):
        result = self._model(expression=self._view._displayText())
        self._view._setText(result)

    def _buildExpression(self, sub_exp):
        if self._view._displayText() == 'ERROR':
            self._view._clearText()

        print(sub_exp)
        expression = self._view._displayText() + sub_exp
        self._view._setText(expression)

    def _connectSignals(self):
        for button_text, button in self._view.buttons.items():
            if button_text not in {'=', 'C'}:
                button.clicked.connect(partial(self._buildExpression, button_text))

        self._view.buttons["="].clicked.connect(self._calculateResult)
        self._view.lineEdit.returnPressed.connect(self._calculateResult)
        self._view.buttons["C"].clicked.connect(self._view._clearText)
