from FormatMessages import *
from SendMassagesStrategy import *
from abstract_notification_factories import *


class NotificationDispatcher:
    def __init__(self, provider):
        self.provider = provider

    def send_notification(self):
        filter_format_list = [OverdueDocumentFactory(), ChangeStatusActFactory(), ChangeStatusInvoiceFactory()]

        dispatcher = SendMassageToShops(self.provider.get_documents(), self.provider.get_subscribers(),
                                        FormatStringMessages(), filter_format_list)
        dispatcher.send_notification()

        dispatcher = SendMassageToAccountant(self.provider.get_documents(), self.provider.get_subscribers(),
                                             FormatTableMessages(), filter_format_list)
        dispatcher.send_notification()
