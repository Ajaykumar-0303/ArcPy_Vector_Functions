import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
inp = "Ludhiana_schools.shp"
out = "Median_schools.shp"
arcpy.MedianCenter_stats(inp, out)
print arcpy.GetMessages()
