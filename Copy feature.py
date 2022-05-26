import arcpy
featureclass = arcpy.ListFeatureClasses()
for feature in featureclass:
    fdes = arcpy.Describe(feature)

arcpy.CopyFeatures_management(feature,"F:\edu\GIS_lab\Punjab\Punjab_dist\python10" + fdes.basename)
print arcpy.GetMessages()
