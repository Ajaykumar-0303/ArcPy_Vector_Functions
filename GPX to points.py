import arcpy
arcpy.env.workspace = "F:\edu\ERDAS\Data\New folder\GPX1"
inp = "Track_2022-02-18 153319.gpx"
out = "2gps_points214.shp"
arcpy.GPXtoFeatures_conversion(inp, out)
print arcpy.GetMessages()
