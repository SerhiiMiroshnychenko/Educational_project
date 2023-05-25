from functools import partial

class Controller:

    def __init__(self, model, view):
        self._model = model # func object
        self._view = view # class object

        self._connectSignal()

    def _calculareResult(self):
        result = self._model(expression=self._view._dicplayText())
        self._view._setText(result)

    def _buildExpression(self, sub_expr):
        if self._model._displayText() == 'Error':
            self._view._clearText()

        expression = self._model._displayText() + sub_expr
        self._view._setText(expression)

    def _connectSignal(self):
        for button_text, button in self._view.buttons.items():
            if button_text not in ('C', '='):
                button.clicked.connect(partial(self._buildExpression, button_text))

        self._view.buttons['C'].clicket.connect(self._view._clearText)
        self._view.buttons['='].clicket.connect(self.calculationResult)
        self._view.lineEdit.returnPressed.connect(self._calculateResult)
        self._view._clearText()
