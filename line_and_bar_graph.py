# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_style(style=None, rc=None)
# flower = sns.load_dataset("iris")
# #change fiqure size
# plt.figure(figsize=(2,3))
# sns.lineplot(x="sepal_length", y="sepal_width", data=flower)
# plt.title("Line chart")
# #set limits
# plt.xlim(2)
# plt.ylim(1)
# sns.set_theme() # to make style changable from defaults use this line of code befor using set_style
# sns.set_style("whitegrid")
# plt.show()


#Bar plot
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style(style=None, rc=None)
flower = sns.load_dataset("iris")
sns.barplot(x="species", y="sepal_width", data=flower)

plt.show()
