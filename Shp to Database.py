import arcpy
input = ["Punjab_dist.shp", "Punjab_railway.shp", "Punjab_st.shp"]
output = "F:\edu\GIS_lab\Punjab\Punjab_dist\python8.gdb"
arcpy.FeatureClassToGeodatabase_conversion(input, output)
print arcpy.GetMessages()
