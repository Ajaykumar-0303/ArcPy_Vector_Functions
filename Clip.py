import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
inp = r"F:\edu\GIS_lab\Punjab\Punjab_dist.shp"
clip = r"F:\edu\GIS_lab\Punjab\Ludhiana.shp"
arcpy.Clip_analysis(inp, clip, "F:\edu\GIS_lab\Punjab\Ludik.shp")
print arcpy.GetMessages()
