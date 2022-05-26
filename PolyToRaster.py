import arcpy
arcpy.env.workspace = "F:\edu\GIS_lab\Punjab\Punjab_dist"
inp = "Gurda.shp"
value_field = "FID"
output = "Gurdas_raster.img"
cell_assignment = "CELL_CENTER"
priority_field = ""
cellsize = "0.002"
arcpy.PolygonToRaster_conversion(inp, value_field, output, cell_assignment, priority_field, cellsize)
print arcpy.GetMessages()
