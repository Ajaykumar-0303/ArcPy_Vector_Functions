import Arcpy
inp3="Punjab_centroid.shp"
out3="standard_distance212.shp"
arcpy.DirectionalDistribution_stats(inp3, out3, "1_STANDARD_DEVIATION")
print arcpy.GetMessages()
