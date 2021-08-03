import matplotlib.pyplot as plt


def viz_table(table):
    table2 = table.copy()
    table2[table2 != 0] = [char.color for char in table2[table2 != 0]]
    table2 = table2.astype(float)
    plt.imshow(table2)
    plt.show()
