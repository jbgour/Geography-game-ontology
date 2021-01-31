class Question:

    def __init__(self, body):
        self.body = body


class QuestionDuo(Question):

    def __init__(self, body, answers):
        super().__init__(self, body=body)
        self.answer_0 = answers[0]
        self.answer_1 = answers[1]


class QuestionCarre(Question):
    def __init__(self, body, answers):
        super().__init__(self, body=body)
        self.answer_0 = answers[0]
        self.answer_1 = answers[1]
        self.answer_2 = answers[2]
        self.answer_3 = answers[3]


class QuestionCash(Question):
    def __init__(self, body):
        super().__init__(self, body=body)
