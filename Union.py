import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
input = "Punjab.shp", "Ludhiana.shp"
output1 = "union_ludhi.shp"
arcpy.Union_analysis(["Punjab.shp", "Ludhiana.shp"], output1, "", "0.03","")
print arcpy.GetMesages()
