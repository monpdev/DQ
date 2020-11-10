import matplotlib.pyplot as plt

houses['Lot Area'].plot.box()
plt.show()
houses['SalePrice'].plot.box()
plt.show()

lotarea_difference = houses['Lot Area'].mean()-houses['Lot Area'].median()
saleprice_difference = houses['SalePrice'].mean()-houses['SalePrice'].median()