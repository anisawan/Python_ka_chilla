# cat plot
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic = sns.load_dataset("titanic")
sns.catplot(x="sex", y="survived", hue="class", data=titanic)
# g=(g.map(plt.scatter, "age", "fare").add_legend())
plt.show()