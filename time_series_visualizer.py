import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import matplotlib.dates as mdates
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.date = pd.to_datetime(df.date)
df.set_index(df.date,inplace=True)

# Clean data
df = df[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]


def draw_line_plot():
  plt.clf()
  fig, ax = plt.subplots(figsize=(12,4))
  ax.plot('date','value',data=df,color='#ea0119');
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019');
  plt.xlabel('Date');
  plt.ylabel('Page Views');
  ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)));

    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  plt.clf()
    # Copy and modify data for monthly bar plot
  df_bar = df.copy() 
  df_bar['Year'] = pd.DatetimeIndex(df_bar.index).year
  df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month
  df_bar = df_bar.groupby(['Year','Month'])['value'].mean()
  df_bar = df_bar.unstack()
    # Draw bar plot
  fig = df_bar.plot(kind= 'bar', figsize = (15,10)).figure
  plt.ylabel('Average Page Views');
  plt.xlabel('Years');
  legend_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
  plt.legend(legend_names);

    # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  plt.clf()
    # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box['Year'] = pd.DatetimeIndex(df_box['date']).year
  df_box['Month'] = pd.DatetimeIndex(df_box['date']).month
    # Draw box plots (using Seaborn)
  fig, axes = plt.subplots(1, 2,figsize=(15, 5))
  sns.boxplot(ax=axes[0],data=df_box,x='Year',y='value',hue='Year',fliersize=1,legend=False,palette=sns.color_palette(n_colors=4));
  axes[0].set_yticks(range(0,200001,20000));
  axes[0].set_ylabel('Page Views');
  axes[0].set_title('Year-wise Box Plot (Trend)');
  sns.boxplot(ax=axes[1],data=df_box,x='Month',y='value',hue='Month',fliersize=1,legend=False,palette=sns.color_palette("husl", 12));
  axes[1].set_xticks(range(12))
  axes[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
  axes[1].set_yticks(range(0,200001,20000));
  axes[1].set_ylabel('Page Views');
  axes[1].set_title('Month-wise Box Plot (Seasonality)');




    # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
