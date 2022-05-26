import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
input = "Rail.shp", "Ludhiana.shp"
output = "Intersection.shp"
arcpy.Intersect_analysis(["Rail.shp", "Ludhiana.shp"], "Intersection.shp", "ALL", "", "INPUT")
print arcpy.GetMessages()
