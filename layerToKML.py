inp = out
out1 = "F:\edu\GIS_lab\Digitise\symmetry.kmz"
arcpy.LayerToKML_conversion(inp, out, "", "", "", "", "", "")
print arcpy.GetMessages()
