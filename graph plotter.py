import matplotlib.pyplot as plt

x = [2, 4, 5]
y = [2, 3, 6]

plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Demo Graph')

plt.grid(True)  # Izgara çizgileri ekle

plt.xticks([1, 2, 3, 4, 5, 6])  # x ekseni işaretleri için özelleştirilmiş değerler belirle
plt.yticks([1, 2, 3, 4, 5, 6])  # y ekseni işaretleri için özelleştirilmiş değerler belirle

plt.axhline(0, color='black', linewidth=0.5)  # x ekseni etrafında yatay çizgi çiz
plt.axvline(0, color='black', linewidth=0.5)  # y ekseni etrafında dikey çizgi çiz

plt.legend(['Data Points'], loc='upper left')  # Grafik için açıklama ekleyin

plt.show()
