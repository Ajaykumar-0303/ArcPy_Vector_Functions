import arcpy
inp1 = r"F:\edu\GIS_lab\Tamilnadu\tagged_photos\Output"
out1 = r"F:\edu\GIS_lab\Tamilnadu\tagged_photos\Output\photo_point.shp"
arcpy.GeoTaggedPhotosToPoints_management(inp1, out1)
print arcpy.GetMessages()
