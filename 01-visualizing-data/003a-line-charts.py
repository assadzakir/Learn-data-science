from matplotlib import pyplot as plt

mentions = [500, 505]

years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)

plt.xticks(years)

plt.ylabel("# of times I heard someone say 'data science'")

# if you don't do this, matplotlib will label the x-axis 0, 1
# and then add a +2.013e3 off in the corner (bad matplotlib!)

plt.ticklabel_format(useOffset=False)

# misleading y-axis only shows the part above 500
plt.axis([2012.5,2014.5,499,506])
plt.title("Look at the 'Huge' Increase!")
plt.show()

# plt.axis([2012.5,2014.5,0,550])
# plt.title("Not So Huge Anymore")
# plt.show()
