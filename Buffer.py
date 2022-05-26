import arcpy
inp=r"F:\Digi\forest\forest.shp"
out=r"F:\Digi\forest\fbuffer12.shp"
arcpy.Buffer_analysis(inp, out, "1000 meters")
print arcpy.GetMessages()
