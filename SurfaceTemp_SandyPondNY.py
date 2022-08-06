import ee 
from ee_plugin import Map
from tabulate import tabulate

'''
    Author:         Gabriel Peters, ugrad (ggp2366@rit.edu)
    Latest Version: 0.2.2 (8/6/22)
    Affiliation:    CIS, Rochester Institute of Technology
 
'''

#  ------------------- READ ME ------------------

'''
 Important info:
    1. This code is designed to provide estimated surface temperature data
       from Landsat 9 Level 2 data, for a specific set of manually selected
       coordinates 
    2. Verbose settings are utilized to make the output easy to understand.
       To see fine details set these settings to "True"
    3. In order to run you need to install the tabulate package. To do this,
       type the following commands into the QGIS command line and then restart QGIS
              import pip
              pip.main(['install', 'tabulate'])
'''

# Verbose settings:

Verbose = False

Console = False


#     ----------- Defining TidbiT Geometry ----------


# Define a Point object.
point1 = ee.Geometry.Point([-76.1646402, 43.6596454]) # #1148
point2 = ee.Geometry.Point([-76.1776992, 43.6428234]) # #5977
point3 = ee.Geometry.Point([-76.1669502, 43.6500498]) # #5967
point4 = ee.Geometry.Point([-76.1839152, 43.6623287]) # #3512
point5 = ee.Geometry.Point([-76.1880032, 43.6675437]) # #3515

# Print the result to the console.

if (Console == True):
  print('Tidbit Coordinates: ')
  print('point1 = (-76.1646402, 43.6596454)')
  print('point2 = (-76.1776992, 43.6428234)')
  print('point3 = (-76.1669502, 43.6500498)')
  print('point4 = (-76.1839152, 43.6623287)')
  print('point5 = (-76.1880032, 43.6675437)')


Map.addLayer(point1,
             {'color': 'red'},
             'Geometry [red]: point1')

Map.addLayer(point2,
             {'color': 'green'},
             'Geometry [green]: point2')

Map.addLayer(point3,
             {'color': 'blue'},
             'Geometry [blue]: point3')

Map.addLayer(point4,
             {'color': 'yellow'},
             'Geometry [yellow]: point4')

Map.addLayer(point5,
             {'color': 'black'},
             'Geometry [black]: point5')

Map.centerObject(point4, 13)

print(f'Point1 - #1148 \nPoint2 - #5977 \nPoint3 - #5967 \nPoint4 - #3512 \nPoint5 - #3515')


#     ------------ Filtering Collection -------------


#Imports
Landsat9_C2_T1_L2 = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2")

# Create an image collection from surface reflectance dataset consisting of only images from days that had sampling occur somewhere

print('Images found...', Landsat9_C2_T1_L2.size().getInfo())
print('--------------------------------------------------')

imageCollection = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2") \
              .filterDate('2022-6-9', '2022-6-23') \
              .filterMetadata('CLOUD_COVER', 'less_than', 50) \
              .filterBounds(point1)

print('Filtered Over Region: ', imageCollection.size().getInfo())

# setting image variable:
#image = ee.Image( INSERT PRODUCT ID );        # get specific image
image = ee.Image(imageCollection.first())

# Get the timestamp and convert it to a date.
date = (ee.Date(image.get('system:time_start')).format('YYYY-MM-dd')).getInfo()
if (Console == True):
  print('Timestamp:', date)

# setting surface temperature variable
ST_b10 = image.select('ST_B10')

image1 = ee.Image(image)

if (Verbose == True):
    Map.addLayer(               # adding map layer for surface temp image
      image,
      {'min':0, 'max':65535, 'bands':['ST_B10']},
      'ST_B10'
    )
    Map.addLayer(               # adding map layer for true color
      image,
      {'min':0, 'max':20000, 'bands':['SR_B4', 'SR_B3', 'SR_B2']},
      'True Color'
    )

#   ------------ Extracting Pixel Values ------------


# extract the pixel value for point1
data = image.select("ST_B10").reduceRegion(ee.Reducer.first(),point1,10).get("ST_B10")

# convert to number
dataN = ee.Number(data).getInfo()

scaleFactor = 0.00341802
constant = 149.0

print('--------------------------------------------------')

if (Console == True):
  print('Point1 (Dock): ')

  # pixel value
  print('Pixel Value: ', dataN)


# pixel value in Kelvin
surfTemp = dataN * scaleFactor + constant

if (Console == True):
  print('Pixel Value (Kelvin): ', surfTemp)


# pixel value in Fahrenheit
surfTempF = (surfTemp - 273) * 1.8 + 32

if (Console == True):
  print('Pixel Value (Fahrenheit): ', surfTempF)

  print('--------------------------------------------------')
  print('Point2 (Wigwam): ')


# extract the pixel value for point2
data2 = image.select("ST_B10").reduceRegion(ee.Reducer.first(),point2,10).get("ST_B10")

# convert to number
dataN2 = ee.Number(data2).getInfo()

if (Console == True):
  # pixel value
  print('Pixel Value: ', dataN2)


# pixel value in Kelvin
surfTemp2 = dataN2 * scaleFactor + constant

if (Console == True):
  print('Pixel Value (Kelvin): ', surfTemp2)


# pixel value in Fahrenheit
surfTempF2 = (surfTemp2 - 273) * 1.8 + 32

if (Console == True):
  print('Pixel Value (Fahrenheit): ', surfTempF2)

  print('--------------------------------------------------')
  print('Point3 (Seber): ')


# extract the pixel value for point3
data3 = image \
.select("ST_B10") \
.reduceRegion(ee.Reducer.first(),point3,10) \
.get("ST_B10")

# convert to number
dataN3 = ee.Number(data3).getInfo()

if (Console == True):
  # pixel value
  print('Pixel Value: ', dataN3)


# pixel value in Kelvin
surfTemp3 = dataN3 * scaleFactor + constant

if (Console == True):
  print('Pixel Value (Kelvin): ', surfTemp3)


# pixel value in Fahrenheit
surfTempF3 = (surfTemp3 - 273) * 1.8 + 32

if (Console == True):
  print('Pixel Value (Fahrenheit): ', surfTempF3)

  print('--------------------------------------------------')
  print('Point4 (South Carl): ')


# extract the pixel value for point4
data4 = image \
.select("ST_B10") \
.reduceRegion(ee.Reducer.first(),point4,10) \
.get("ST_B10")

# convert to number
dataN4 = ee.Number(data4).getInfo()

if (Console == True):
  # pixel value
  print('Pixel Value: ', dataN4)


# pixel value in Kelvin
surfTemp4 = dataN4 * scaleFactor + constant

if (Console == True):
  print('Pixel Value (Kelvin): ', surfTemp4)


# pixel value in Fahrenheit
surfTempF4 = (surfTemp4 - 273) * 1.8 + 32

if (Console == True):
  print('Pixel Value (Fahrenheit): ', surfTempF4)

  print('--------------------------------------------------')
  print('Point5 (North Carl): ')


# extract the pixel value for point5
data5 = image \
.select("ST_B10") \
.reduceRegion(ee.Reducer.first(),point5,10) \
.get("ST_B10")

# convert to number
dataN5 = ee.Number(data5).getInfo()

if (Console == True):
  # pixel value
  print('Pixel Value: ', dataN5)


# pixel value in Kelvin
surfTemp5 = dataN5 * scaleFactor + constant

if (Console == True):
  print('Pixel Value (Kelvin): ', surfTemp5)


# pixel value in Fahrenheit
surfTempF5 = (surfTemp5 - 273) * 1.8 + 32

if (Console == True):
  print('Pixel Value (Fahrenheit): ', surfTempF5)




#   -------------- Making a Data Table --------------

time = (ee.Date(image.get('system:time_start')).format('HH MM ss')).getInfo()

print('Data Table:')

dataTable = [
  ['TidbiT', 'Location (Sandy Pond)', 'Pixel Value', 'Kelvin (K)', 'Fahrenheit (F)', '(year-month-day hour-minute-second)'],
  ['#1148', '(-76.1646402, 43.6596454)', dataN, surfTemp, surfTempF, date + ' ' + time],
  ['#5977', '(-76.1776992, 43.6428234)', dataN2, surfTemp2, surfTempF2, date + ' ' + time],
  ['#5967', '(-76.1669502, 43.6500498)', dataN3, surfTemp3, surfTempF3, date + ' ' + time],
  ['#3512', '(-76.1839152, 43.6623287)', dataN4, surfTemp4, surfTempF4, date + ' ' + time],
  ['#3515', '(-76.1880032, 43.6675437)', dataN5, surfTemp5, surfTempF5, date + ' ' + time],
]

#chart = ui.Chart(dataTable).setChartType('Table')
print(tabulate(dataTable))
#chart.setDownloadable('CSV')
#print('Chart is downloadable as: ', chart.getDownloadable())
