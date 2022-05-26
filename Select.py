import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
inp = "Gurudwara.shp"
out = "Gurudwara_select.shp"
arcpy.Select_analysis(inp, out, "FID<63")
print arcpy.GetMessages()
