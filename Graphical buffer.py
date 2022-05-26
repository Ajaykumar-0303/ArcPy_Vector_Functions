import arcpy
int3 = "gps_line.shp"
out3 = "Graphical_buffer214.shp"
arcpy.GraphicBuffer_analysis(int3, out3, "8 meters")
print arcpy.GetMessages()
