import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab\Punjab_dist"
inp = "Ludhiana_identity.shp"
out1 = "Ludhiana_cent.shp"
arcpy.FeatureToPoint_management(inp, out1, "CENTROID")
print arcpy.GetMessages()
