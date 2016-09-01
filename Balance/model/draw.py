#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
data_to_plot = [np.random.normal(100, 100, 200),
                np.random.normal(80, 30, 200),
                np.random.normal(90, 20, 200),
                np.random.normal(70, 25, 200)]
print type(data_to_plot)

fig = plt.figure(1, figsize=(9, 6))
# Create an axes instance
ax = fig.add_subplot(111)

## add patch_artist=True option to ax.boxplot()
## to get fill color
bp = ax.boxplot(data_to_plot, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='y', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']: # 上下的帽子
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']: #中值
    median.set(color='r', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']: #异常值
    flier.set(marker='o', color='k', alpha=0.5)


plt.show()