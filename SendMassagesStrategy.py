from format_column_strategy import FormatColumnDecorator
from provider import *


class SendMassageStrategy:
    def __init__(self, documents, subscribers, horizontal_format_strategy, notification_factories):
        self.subscribers = subscribers
        self.documents = documents
        self.notification_factories = notification_factories
        self.horizontal_format_strategy = horizontal_format_strategy

    def send_notification(self):
        pass

    def internal_send_notification(self, documents, subscriber):
        for factory in self.notification_factories:
            filtered_documents = factory.create_filter().document_filter(documents)
            if not filtered_documents:
                return
            title = factory.create_title()
            print(subscriber.email +
                  "\n" +
                  title.get_subject() +
                  "\n" +
                  title.get_title() +
                  "\n" +
                  self.horizontal_format_strategy.prepare(filtered_documents, FormatColumnDecorator(factory.create_column())))


class SendMassageToShops(SendMassageStrategy):
    def send_notification(self):
        shops_list = list(filter(
            lambda x: x.role == Role.Shop, self.subscribers))
        for x in shops_list:
            documents = list(filter(lambda y: y.store_number == x.store_number, self.documents))
            self.internal_send_notification(documents, x)


class SendMassageToAccountant(SendMassageStrategy):
    def send_notification(self):
        accountants_list = list(filter(lambda x: x.role == Role.Accountant, self.subscribers))
        for x in accountants_list:
            documents = self.documents
            self.internal_send_notification(documents, x)
