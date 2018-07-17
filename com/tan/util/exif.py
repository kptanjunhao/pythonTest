#coding=utf-8
import exifread

class GPSInfo:
    latitude = 0.0
    longitude = 0.0
    altitude = 0.0

# def all_files(root, patterns='*', single_level=False, yield_folders=False):
#     patterns = patterns.split(';')
#     for path, subdirs, files in os.walk(root):
#         if yield_folders:
#             files.extend(subdirs)
#         files.sort()
#         for name in files:
#             for pattern in patterns:
#                 if fnmatch.fnmatch(name, pattern):
#                     yield os.path.join(path, name)
#                     break
#                 if single_level:
#                     break

def parse_altitude(titude):
    parent = titude.split('/')[0]
    child = titude.split('/')[1]
    return float(parent)/float(child)

def parse_gps(titude):
    first_number = titude.split(',')[0]
    second_number = titude.split(',')[1]
    third_number = titude.split(',')[2]
    third_number_parent = third_number.split('/')[0]
    third_number_child = third_number.split('/')[1]
    third_number_result = float(third_number_parent) / float(third_number_child)
    return float(first_number) + float(second_number)/60 + third_number_result/3600


# def write_data(paths):
#     index = 1
#     for path in all_files(paths, '*.jpg'):
#         f = open(path[2:], 'rb')
#         tags = exifread.process_file(f)
#         # jsonFile.writelines('"type": "Feature","properties": {"cartodb_id":"'+str(index)+'"},"geometry": {"type": "Point","coordinates": [')
#         latitude = tags['GPS GPSLatitude'].printable[1:-1]
#         longitude = tags['GPS GPSLongitude'].printable[1:-1]
#         print(latitude)
#         print(parse_gps(latitude))
#         # print tags['GPS GPSLongitudeRef']
#         # print tags['GPS GPSLatitudeRef']
#         jsonFile.writelines('{"type": "Feature","properties": {"cartodb_id":"' + str(index) + '"')
#         jsonFile.writelines(',"OS":"' + str(tags['Image Software']) + '","Model":"' + str(tags['Image Model']) + '","Picture":"'+str(path)+'"')
#         jsonFile.writelines('},"geometry": {"type": "Point","coordinates": [' + str(parse_gps(longitude)) + ',' + str(
#             parse_gps(latitude)) + ']}},\n')
#         index += 1

def imgInfo(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    return tags

def gpsInfo(path):
    try:
        tags = imgInfo(path)
        latitude = tags['GPS GPSLatitude'].printable[1:-1]
        longitude = tags['GPS GPSLongitude'].printable[1:-1]
        altitude = tags['GPS GPSAltitude'].printable[1:-1]
        gpsInf = GPSInfo()
        gpsInf.latitude = parse_gps(latitude)
        gpsInf.longitude = parse_gps(longitude)
        gpsInf.altitude = parse_altitude(altitude) * 0.3048 # 英尺转换为米
        return gpsInf
    except:
        return

def googleMapsUrl(latitude,longitude,altitude=500):
    return "http://www.google.cn/maps/@"+str(latitude)+","+str(longitude)+","+str(altitude)+"m"
