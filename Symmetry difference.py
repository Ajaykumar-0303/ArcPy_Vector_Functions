import arcpy
inp = r"F:\edu\GIS_lab\Digitise\forest\Forestry.shp"
update = "F:\edu\GIS_lab\Digitise\lakes\lake.shp"
out = "F:\edu\GIS_lab\Digitise\symmetry019.shp"
arcpy.SymDiff_analysis(inp, update, out, "ALL", "")
print arcpy.GetMessages()
