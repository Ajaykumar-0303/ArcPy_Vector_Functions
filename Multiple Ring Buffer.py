arcpy.env.workspace = "F:\edu\GIS_lab\Punjab\Punjab_dist"
int = out
out1 = "Multi_buff_rail.shp"
arcpy.MultipleRingBuffer_analysis(int, out1, [100, 200, 300], "meters", "", "ALL")
print arcpy.GetMessages()
