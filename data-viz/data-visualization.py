import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

ariseism_btops = pd.read_csv('data-viz/ariseism_bigtops.csv')
ariseism_stops = pd.read_csv('data-viz/ariseism_smalltops.csv')
ariseism_bbottoms = pd.read_csv('data-viz/ariseism_bigbottoms.csv')
ariseism_sbottoms = pd.read_csv('data-viz/ariseism_smallbottoms.csv')

brandy_btops = pd.read_csv('data-viz/brandy_bigtops.csv')
brandy_stops = pd.read_csv('data-viz/brandy_smalltops.csv')
brandy_bbottoms = pd.read_csv('data-viz/brandy_bigbottoms.csv')
brandy_sbottoms = pd.read_csv('data-viz/brandy_smallbottoms.csv')

#print(ariseism.head())
ariseism_btops['category'] = 'Big Tops'
ariseism_stops['category'] = 'Small Tops'
ariseism_bbottoms['category'] = 'Big Bottoms'
ariseism_sbottoms['category'] = 'Small Bottoms'

brandy_btops['category'] = 'Big Tops'
brandy_stops['category'] = 'Small Tops'
brandy_bbottoms['category'] = 'Big Bottoms'
brandy_sbottoms['category'] = 'Small Bottoms'

#combined = pd.concat([ariseism, brandy])
stop_comparison = pd.concat([ariseism_stops, brandy_stops])

plt.figure(figsize=(12,6))
sns.histplot(data=stop_comparison, x = 'category', y = 'price')
plt.title('Big Top Price Comparison: Ariseism vs. Brandy Melville')
plt.show()