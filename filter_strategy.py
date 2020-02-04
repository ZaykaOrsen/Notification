from provider import SendNotifyType, DocType


class FilterStrategy:
    def document_filter(self, documents):
        pass


class OverdueFilter(FilterStrategy):
    def document_filter(self, documents):
        return list(filter(lambda x: x.send_notify_type == SendNotifyType.OverdueDocument, documents))


class ChangeStatusActFilter(FilterStrategy):
    def document_filter(self, documents):
        return list(filter(lambda x: x.send_notify_type == SendNotifyType.ChangeStatusDocument
                           and x.document_type == DocType.Act, documents))


class ChangeStatusInvoiceFilter(FilterStrategy):
    def document_filter(self, documents):
        aa = 222
        return list(filter(lambda x: x.send_notify_type == SendNotifyType.ChangeStatusDocument
                           and x.document_type == DocType.Invoice, documents))
