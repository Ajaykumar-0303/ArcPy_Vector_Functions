import arcpy
arcpy.env.workspace ="F:\edu\GIS_lab\Punjab\Punjab_dist"
arcpy.CreateFileGDB_management ("F:\edu\GIS_lab\Punjab\Punjab_dist", "python8.gdb")
print arcpy.GetMessages()
