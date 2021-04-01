from geopy.distance import geodesic
class Solution:
	def fn(self):
		city1=input('City 1:')
		city2=input('City 2:')
		lat1,lon1=city1.split(",")

		lat1=lat1[0:-2]
		lon1=lon1[1:-2]

		lat2,lon2=city2.split(",")
		lat2=lat2[0:-2]
		lon2=lon2[1:-2]


		coords_1 = (lat1,  lon1)
		coords_2 = (lat2 , lon2)

		print ("City1 and City2 are",geodesic(coords_1, coords_2).kilometers,"km apart",end="")
		print()




Solution().fn()