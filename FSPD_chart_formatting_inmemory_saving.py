
# coding: utf-8

# In[ ]:


# formatting output chart for F/S/TPD targets and saving them into memory & html format for automated mailing
import pandas as pd
from matplotlib import pyplot as plt
import sys   

# in memory saving and decoding to bytes and to html
import io
import base64

# df_fspd is a pandas dataframe with granularity of date and segment

list_of_images = []

for seg in np.unique(df_fspd.index.get_level_values('segment').values):
    plt.figure(figsize=(15, 8))
    plt.plot(df_fspd.loc[seg].index.values, df_fspd.loc[seg]['fpd90'], color = "red", label = "FPD90", marker='.', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(df_fspd.loc[seg].index.values, df_fspd.loc[seg]['spd90'], color = "orange", label = "SPD90", marker='.', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(df_fspd.loc[seg].index.values, df_fspd.loc[seg]['tpd90'], color = "gold", label = "TPD90", marker='.', linestyle='dashed',linewidth=2, markersize=12)
    plt.title("FSTPD90 chart for segment " + seg)
    plt.tick_params(axis='x', labelrotation = 90)
    plt.legend()
    # to avoid distored axis due to spikes in measures for dates with low count of cases
    plt.ylim(0, 1.15*max([df_fspd.loc[seg]['fpd90'].quantile(q=0.9) , df_fspd.loc[seg]['spd90'].quantile(q=0.9) , df_fspd.loc[seg]['tpd90'].quantile(q=0.9)))
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(.5)) 
    plt.gca().yaxis.set_minor_locator(mtick.AutoMinorLocator())
    plt.grid(linestyle='dotted')
    # instead of showing (plt.show) save in memory
    f = io.BytesIO()
    plt.savefig(f,format='png')
    f.seek(0)
    # img_data = f.read()
    data = f.getvalue()         # get data from file (BytesIO)
    data = base64.b64encode(data) # convert to base64 as bytes
    data = data.decode()          # convert bytes to string
    list_of_images.append('<br><img src="data:image/png;base64,{}"></br>'.format(data))

