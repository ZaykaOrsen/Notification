from filter_strategy import *
from format_column_strategy import *
from titles_strategy import *


class AbstractNotificationFactory:
    def create_filter(self):
        pass

    def create_column(self):
        pass

    def create_title(self):
        pass


class OverdueDocumentFactory(AbstractNotificationFactory):
    def create_filter(self):
        return OverdueFilter()

    def create_column(self):
        return OverdueDocumentFormatColumnStrategy()

    def create_title(self):
        return OverdueDocumentTitle()


class ChangeStatusActFactory(AbstractNotificationFactory):
    def create_filter(self):
        return ChangeStatusActFilter()

    def create_column(self):
        return ChangeStatusActFormatColumnStrategy()

    def create_title(self):
        return ChangeStatusActTitle()


class ChangeStatusInvoiceFactory(AbstractNotificationFactory):
    def create_filter(self):
        return ChangeStatusInvoiceFilter()

    def create_column(self):
        return ChangeStatusInvoiceFormatColumnStrategy()

    def create_title(self):
        return ChangeStatusInvoiceTitle()

