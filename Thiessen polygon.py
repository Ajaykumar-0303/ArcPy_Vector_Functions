import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
inp = "Ludhiana_schools.shp"
out = "Thiessen_schools.shp"
outFields = "ALL"
arcpy.CreateThiessenPolygons_analysis(inp, out, outFields)
print arcpy.GetMessages()
