import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab"
input = "Schools.shp"
output = "Schools1.shp"
arcpy.Dissolve_management(input, output, "", "", "SINGLE_PART", "")
print arcpy.GetMessages()
