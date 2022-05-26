import arcpy
inp2 = "gps_point.shp"
out2 = "2gps_line214.shp"
arcpy.PointsToLine_management(inp2, out2)
print arcpy.GetMessages()
