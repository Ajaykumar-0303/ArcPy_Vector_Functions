import arcpy
inp3 = r"F:\edu\GIS_lab\Digitise\forest\Forestry.shp", "F:\edu\GIS_lab\Digitise\lakes\lake.shp"
out3 = "F:\edu\GIS_lab\Digitise\spatial_megre.shp"
arcpy.Merge_management([r"F:\edu\GIS_lab\Digitise\forest\Forestry.shp", "F:\edu\GIS_lab\Digitise\lakes\lake.shp"], out3)
print arcpy.GetMessages()
