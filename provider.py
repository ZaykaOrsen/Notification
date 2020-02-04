import datetime
from enum import Enum


class DocType(Enum):
    Act = "АР"
    Invoice = "PH"


class Role(Enum):
    Accountant = "accountant"
    Shop = "store"


class SendNotifyType(Enum):
    ChangeStatusDocument = 1
    OverdueDocument = 2


# subscribe_type_list: 1 - смена статуса 2 - не подписаны в срок


class Subscriber:
    def __init__(self, email, role, store_number, subscribe_type_list):
        self.email = email
        self.role = role
        self.store_number = store_number
        self.subscribe_type_list = subscribe_type_list

    def __repr__(self):
        return f"{self.email}, {self.role}, {self.store_number}, {self.subscribe_type_list}"


class Document:
    def __init__(self, store_number, document_number, document_date, document_type, parent_invoice_number,
                 parent_invoice_date, send_notify_type):
        self.store_number = store_number
        self.document_number = document_number
        self.document_date = document_date
        self.document_type = document_type
        self.parent_invoice_number = parent_invoice_number
        self.parent_invoice_date = parent_invoice_date
        self.send_notify_type = send_notify_type

    def __repr__(self):
        return f"{self.store_number}, {self.document_number}, {self.document_date}, {self.document_type}, {self.parent_invoice_number}, {self.parent_invoice_date}"


class DataProvider:

    @staticmethod
    def get_documents():
        return DataProvider._list_documents

    @staticmethod
    def get_subscribers():
        return DataProvider._list_subscribers

    _list_documents = [
        Document(
            2,
            2,
            datetime.date(2019, 11, 1),
            DocType.Act,
            1,
            datetime.date(2019, 10, 20),
            SendNotifyType.ChangeStatusDocument
        ),
        Document(
            1,
            1,
            datetime.date(2019, 12, 28),
            DocType.Invoice,
            1,
            datetime.date(2019, 12, 10),
            SendNotifyType.OverdueDocument
        ),
        Document(
            3,
            3,
            datetime.date(2019, 10, 12),
            DocType.Act,
            3,
            datetime.date(2019, 10, 11),
            SendNotifyType.OverdueDocument
        ),

    ]
    _list_subscribers = [
        Subscriber(
            "anatoliynn@gamil.com",
            Role.Accountant,
            1,
            [SendNotifyType.OverdueDocument]
        ),
        Subscriber(
            "store2@gmail.com",
            Role.Shop,
            1,
            [SendNotifyType.ChangeStatusDocument, SendNotifyType.OverdueDocument]
        ),
        Subscriber(
            "ivan@gamil.com",
            Role.Accountant,
            2,
            [SendNotifyType.ChangeStatusDocument]
        ),
        Subscriber(
            "store3@gmail.com",
            Role.Shop,
            3,
            [SendNotifyType.ChangeStatusDocument, SendNotifyType.OverdueDocument]
        ),
    ]


