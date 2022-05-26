import arcpy
inp3="Punjab_centroid.shp"
out3="standard_distance12.shp"
arcpy.StandardDistance_stats(inp3, out3,"1_STANDARD_DEVIATION")
print arcpy.GetMessages()
