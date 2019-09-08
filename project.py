import pandas as pd 
import networkx as nx 
from scipy.spatial import distance_matrix
from algo_func import capControllerPlacement
filepath = "Aarnet.gml"
G = nx.read_gml(filepath)
nodes_list = list(G.nodes)
latitude_list = list(G.nodes(data = 'Latitude'))
longitude_list = list(G.nodes(data = 'Longitude'))
internal_list = list(G.nodes(data = 'Internal'))
temp1 = []
temp2 = [] 
temp3 = []
for l, r, t in zip(latitude_list, longitude_list, internal_list):
	temp1.append(l[1])
	temp2.append(r[1])
	temp3.append(t[1])
latitude_list = temp1
longitude_list = temp2
internal_list = temp3
df = pd.DataFrame(list(zip(nodes_list, latitude_list, longitude_list)), columns = ['Places', 'Longitude', 'Latitude'])
df.set_index('Places', inplace = True)
dm = 111*(pd.DataFrame(distance_matrix(df.values, df.values), index = df.index, columns = df.index))
distances = set()
for index, row in dm.iterrows():
	for ele in row:
		distances.add(ele)
	#print(row)
distances = sorted(distances)
distances.remove(0.0)
k = 5
#result = capControllerPlacement(distances, k)
print(dm)