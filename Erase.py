import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
input="Punjab_dist.shp"
erase= "Ludhiana.shp"
output="Erase.shp"
arcpy.Erase_analysis(input, erase, output, "")
print arcpy.GetMessages()
