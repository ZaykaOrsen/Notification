class FormatColumnStrategy:
    def get_headers(self):
        pass

    def get_values(self, document):
        pass


class FormatColumnDecorator(FormatColumnStrategy):
    def __init__(self, formatColumn):
        self.formatColumn = formatColumn
        self.line_num = 0

    def get_headers(self):
        return ["# ПП"] + self.formatColumn.get_headers()

    def get_values(self, document):
        self.line_num += 1
        return [str(self.line_num)] + self.formatColumn.get_values(document)


class ChangeStatusInvoiceFormatColumnStrategy(FormatColumnStrategy):

    def get_headers(self):
        return ["Магазин #", "Документ #", "Дата документа "]

    def get_values(self, document):
        return [str(document.store_number), str(document.document_number), str(document.document_date)]


class ChangeStatusActFormatColumnStrategy(FormatColumnStrategy):

    def get_headers(self):
        return ["Магазин #", "Документ #", "Дата документа ", "Накладная #", "Дата накладной "]

    def get_values(self, document):
        return [str(document.store_number), str(document.document_number), str(document.document_date),
                str(document.parent_invoice_number), str(document.parent_invoice_date)]


class OverdueDocumentFormatColumnStrategy(FormatColumnStrategy):

    def get_headers(self):
        return ["Тип документа ", "Магазин #", "Документ #", "Дата документа "]

    def get_values(self, document):
        return [str(document.document_type), str(document.store_number), str(document.document_number),
                str(document.document_date)]
