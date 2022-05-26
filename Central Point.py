import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
inp = "Gurudwara.shp"
out2 = "Gurudwara_center.shp"
distance_method = "EUCLIDEAN_DISTANCE"
arcpy.CentralFeature_stats(inp, out2, distance_method, "", "", "")
print arcpy.GetMessages()
