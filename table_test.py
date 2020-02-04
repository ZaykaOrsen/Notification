from prettytable import PrettyTable
t = PrettyTable(['Name', 'Age'])
t.add_row(['Alice', 24])
t.add_row(['Bob', 19])
print(t)
x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
x.sortby = "Population"
x.reversesort = True
x.int_format["Area"] = "04d"
x.float_format = "6.1f"
x.align["City name"] = "l" # Left align city names
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])
print(x)

import termtables as tt

string = tt.to_string(
    [["Alice", 24], ["Bob", 19]],
    header=["Name", "Age"],
    style=tt.styles.ascii_thin_double,
    # alignment="ll",
    # padding=(0, 1),
)
print(string)