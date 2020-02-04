from prettytable import PrettyTable


class FormatMessagesStrategy:

    def prepare(self, documents, columns):
        pass


class FormatStringMessages(FormatMessagesStrategy):
    def prepare(self, documents, columns):
        text_delimiter = " "
        s = ""
        for doc in documents:
            heads_and_values = list(a[0] + a[1] for a in (zip(columns.get_headers(), columns.get_values(doc))))
            s += text_delimiter.join(heads_and_values)
            s += "\n"
        return s


class FormatTableMessages(FormatMessagesStrategy):
    def prepare(self, documents, columns):
        t = PrettyTable(columns.get_headers())
        for doc in documents:
            t.add_row(columns.get_values(doc))
        return str(t)






