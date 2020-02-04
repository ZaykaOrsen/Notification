class TitleStrategy:
    def get_subject(self):
        pass

    def get_title(self):
        pass


class OverdueDocumentTitle(TitleStrategy):
    def get_subject(self):
        return "Превышен срок выполнения по документам"

    def get_title(self):
        return "Документы не переданы в учетную систему и превышает отведенный срок работ" \
               " по документам в течении 10-ти дней согласно регламента по учету вторсырья."


class ChangeStatusActTitle(TitleStrategy):
    def get_subject(self):
        return "Изменилось состояние Актов расхождений"

    def get_title(self):
        return "Изменились статусы следующих Актов расхождений:"


class ChangeStatusInvoiceTitle(TitleStrategy):
    def get_subject(self):
        return "Изменилось состояние Расходных накладных"

    def get_title(self):
        return "Изменились статусы следующих Расходных накладных:"


