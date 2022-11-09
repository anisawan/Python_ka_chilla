#step 1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt
#step 2 set theme
sns.set_theme(style="ticks", color_codes=True)
#step 3 import data set
ship = sns.load_dataset("titanic")
print(ship)
#step 4 plot basic graph with 1 variable (count)
# p = sns.countplot(x="sex", data=ship)
# plt.show()

#step 5 plot basic graph with 2 variables (count plot)
# p = sns.countplot(x="sex", data=ship, hue="class")
# plt.show()

#step 6 plot basic graph with 2 variables (count plot) with title
p = sns.countplot(x="sex", data=ship, hue="class")
p.set_title("count plot")
plt.show()
