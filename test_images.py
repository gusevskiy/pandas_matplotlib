import matplotlib.pyplot as plt

x1 = [-29, -15, -2, -6, -2, -2, -1, -9, -2, -2, -4, -2, -1, -1, -2, -1, -1, -2, -2, -2, -6, -1, -1, -2, -2, -2, -2, -4, -5, -3, -3, -1, -2, -2, -2, -2, -3, -2, -1, -1, -6, -2, -2, -2, -2, -2, -1, -1, -2, -2, -3, -2, -4, -1, -1, -1, -1, -1, -2, -3, -2, -2, -1, -1, -1, -2, -2, -6, -2, -1, -1, -1, -1, -3, -3, -2, -25, -1, -1, -1, -1, -3, -2, -2, -63, -2, -1, -1, -1, -2, -2, -5, -10, -3, -6, -9, -2, -1, -1, -1, -1, -2, -1, -1, -1, -3, -2, -1, -3, -15, -1, -2, -1, -1, -2, -1, -1, -1, -1, -1, -2, -3, -1, -1, -4, -3, -2, -6, -1, -1, -2, -2, -2, -3, -8, -2, -4, -1, -1, -1]
x2 = [-25, -2, -2, -6, -1, -1, -3, -4, -11, -2, -1, -3, -5, -3, -2, -2, -2, -2, -2, -1, -1, -2, -3, -3, -9, -4, -4, -30, -2, -2, -3, -2, -2, -3, -4, -3, -1, -3, -2, -2, -2, -2, -6, -2, -4, -4, -3, -1, -5, -102, -5, -12, -3, -3, -2, -2, -4, -2, -1, -2, -4, -2, -2, -2, -2, -13, -2, -2, -1, -2, -3, -2, -1, -2, -3, -13, -3, -3, -13, -4, -3, -1, -1, -1]
x3 = [-21, -2, -3, -4, -5, -1, -3, -1, -2, -2, -1, -1, -1, -2, -1, -2, -2, -2, -1, -1, -3, -2, -1, -1, -1, -2, -2, -1, -2, -1, -1, -2, -1, -1, -1, -2, -3, -16, -2, -1, -1, -2, -2, -3, -1, -2, -2, -8, -1, -2, -2, -2, -3, -2, -5, -1, -4, -1, -1, -1, -1, -1, -1, -1, -4, -1, -1, -1, -3, -3, -2, -4, -2, -7, -2, -1, -1, -1, -1, -1, -1, -2, -1, -1, -2, -3, -4, -3, -12, -4, -3, -8, -2, -1, -1, -1, -1, -1, -1, -1, -2, -2, -5, -2, -2, -20, -2, -1, -1, -1, -2, -3, -3, -2, -4, -1, -3, -7, -3, -2, -3, -1, -1, -1, -1, -2, -1, -2, -2, -1, -2, -10, -1, -2, -2, -3, -6, -1, -3, -10, -2, -2, -3, -2, -2, -1, -2, -4, -2, -4, -2, -1, -4, -3, -1, -3, -8, -2, -2, -4, -10, -10, -7, -1, -3, -2, -1, -1, -2, -3, -1, -3, -2, -2]
x4 = [-8, -1, -13, -8, -1, -1, -1, -2, -3, -2, -1, -1, -1, -1, -3, -1, -1, -1, -1, -2, -2, -1, -1, -1, -2, -3, -3, -5, -6, -2, -1, -1, -2, -2, -1, -1, -3, -2, -2, -1, -1, -1, -8, -2, -2, -1, -1, -7, -8, -2, -7, -2, -1, -1, -1, -1, -2, -4, -3, -2, -3, -9, -1, -1, -1, -1, -1, -3, -3, -2, -5, -3, -6, -1, -1, -2, -3, -4, -2, -1, -1, -2, -1, -1, -2, -4, -2, -1, -1, -2, -2, -2, -3, -1, -3, -3, -2, -1, -1, -1, -56, -2, -6, -1, -6, -1, -1, -1, -1, -1, -2, -4, -5, -6, -1, -1, -1, -2, -10, -2, -3, -10, -1, -2, -9, -1, -3, -1, -46, -4, -2, -4, -1, -1, -1, -2, -2, -5, -16, -1, -2, -6, -5, -3]

for i, h in enumerate([x1, x2, x3, x4]):
    plt.figure()
    plt.plot(h)
    # plt.xticks(rotation=90)
    # Сетка на графике
    plt.grid()
    # plt.show()
    plt.savefig(f"{i}.png")


# plt.plot(x4)
# plt.grid()
# # plt.show()
# plt.savefig(f"x1.png")