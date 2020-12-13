
from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14,5,17,28,25,27,26,22,18,15]

# 画之前设置图片大小
plt.figure(figsize=(20,8),dpi=80)

# 绘图
plt.plot(x,y)

# 设置x轴的刻度
_xticj_labels = [1/2 for i in range(4,49)]
plt.xticks(_xticj_labels)
plt.yticks(range(min(y),max(y)+1))

# 保存图片
plt.savefig("./sig.png")


# 显示图片
plt.show()
