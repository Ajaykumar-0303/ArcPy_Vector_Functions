import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
inp = "Ludhiana_schools.shp"
out = "Mean_schools.shp"
arcpy.MeanCenter_stats(inp, out)
print arcpy.GetMessages()
