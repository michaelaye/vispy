
# coding: utf-8

# In[4]:

n = 10
loc_data = np.zeros((n, 2))
loc_data[0] = np.array([12, 120])
loc_data[1] = np.array([56, 43])


# In[5]:

loc_data


# In[6]:

class JetManager(object):
    def __init__(self, no):
        self.no = no
        self.lat = loc_data[no][0]
        self.lon = loc_data[no][1]


# In[7]:

simman = Jet(0)


# In[8]:

jet.lat


# In[9]:

jet.lon


# In[18]:

class Particle(object):
    def __init__(self, sourcejet):
        self.source = sourcejet
        self.pos = (self.source.lat, self.source.lon)
        self.origpos = self.pos.copy()
    def update_pos(self, newpos):
        self.pos = newpos


# In[11]:

def convert_porco(old):
    return 180. - old - 3.5


# In[12]:

def convert_porco2(old):
    return 180. - (old - 3.5)


# In[16]:

input = np.arange(0, 360, 5)


# In[17]:

for i, j,k in zip(input, convert_porco(input), convert_porco2(input)):
    print(i,j,k)


# In[30]:

import SpiceyPy as spice


# In[32]:

spice.latrec(200000, -80, 10)


# In[33]:

spice.latrec(200, -80, 10)


# In[34]:

get_ipython().magic('pinfo spice.reclat')


# In[40]:

axes = np.array([250, 260, 270])
axes = axes*1000
point_i = spice.latrec(axes[2], np.deg2rad(170), np.deg2rad(-85))


# In[39]:

spice.surfnm(axes[0], axes[1], axes[2], point_i)


# In[41]:

spice.surfnm(axes[0], axes[1], axes[2], point_i)


# In[42]:

get_ipython().magic('pinfo np.where')


# In[60]:

def _100_():
    import xlrd
    excelFile100sources = '/Users/klay6683/Dropbox/SternchenAndMe/Enceladus_stuff/100_sources_Porco2014.xlsx'
    book = xlrd.open_workbook(excelFile100sources)
    sh = book.sheet_by_index(0)
    # loop over columns in excel sheet
    lonlat = np.zeros((sh.nrows, 2))
    lonlat[:, 0] = sh.col_values(0)[:]
    lons = np.array(sh.col_values(1)[:])
#     ### LONGITUDES !!!
    lonlat[:,1]=180. - (lons - 3.5) # it is West Lon in the paper with different zero and in Voyager era            
    return lonlat


# In[62]:

_100_()[:5]


# In[78]:

df = pd.read_excel('/Users/klay6683/Dropbox/SternchenAndMe/Enceladus_stuff/100_sources_Porco2014.xlsx',
                   header=None)
lonlat = df[[0,1]].values
lonlat[:, 1] = 180. - (lonlat[:, 1] - 3.5)


# In[79]:

lonlat[:5]


# In[75]:

lonlat[:, 0]


# In[76]:

lonlat[:, 0] = 180. - (lonlat[:, 0] -3.5)


# In[77]:

lonlat[:5]


# In[82]:

i=50
'jet'+str(i).zfill(2)


# l = False

# In[84]:

check = 'False'


# In[86]:

if check:
    print("yes")


# In[104]:

convert_porco2(62.59)


# In[93]:

convert_porco(58.64)


# In[110]:

lonlat[93]


# In[100]:

number2reset = 15000
lonlat_all = lonlat
dlon = np.zeros(number2reset)
dlon[:] = np.deg2rad(lonlat_all[3,1])
dlat = np.zeros(number2reset)
dlat[:] = np.deg2rad((lonlat_all[3,0]))
source_lat = dlat[0]
source_lon = dlon[0]


# In[101]:

source_lon


# In[103]:

np.rad2deg(source_lon)


# In[115]:

convert_porco2(184.81)


# In[112]:

df.loc[93]


# In[123]:

lonlat[90:100]


# In[114]:

get_ipython().magic('pinfo2 convert_porco2')


# In[ ]:



