import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab\Punjab_dist"
out = "Gurda.shp"
count = arcpy.GetCount_management(out)
print count
print arcpy.GetMessages()
