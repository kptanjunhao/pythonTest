#coding=utf-8
from math import pi,radians,sin,cos,asin,sqrt,fabs,tan

earthRadius = 6371.393 # km 地球平均半径

def angleToRadian(angle):
    return pi / 180.0 * angle

def radianToAngle(radian):
    return 180.0 / pi * radian

def distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2.0 * asin(sqrt(a))
    r = earthRadius
    return c * r * 1000.0

# 经度，纬度
def gsPoint(latitude,longitude):
    ProjNo = 0
    ZoneWide = 6
    iPI = pi / 180.0
    a = 6378245.0
    f = 1.0 / 298.3
    ProjNo = (int)(longitude / ZoneWide)
    longitude0 = ProjNo * ZoneWide + ZoneWide / 2
    longitude0 = longitude0 * iPI
    latitude0 = 0
    longitude1 = longitude * iPI
    latitude1 = latitude * iPI
    e2 = 2 * f - f * f
    ee = e2 * (1.0 - e2)
    NN = a / sqrt(1.0 - e2 * sin(latitude1) * sin(latitude1))
    T = tan(latitude1) * tan(latitude1)
    C = ee * cos(latitude1) * cos(latitude1)
    A = (longitude1 - longitude0) * cos(latitude1)
    M = a * ((1 - e2 / 4 - 3 * e2 * e2 / 64 - 5 * e2 * e2 * e2 / 256) * latitude1 - (3 * e2 / 8 + 3 * e2 * e2 / 32 + 45 * e2 * e2* e2 / 1024) * sin(2 * latitude1) + (15 * e2 * e2 / 256 + 45 * e2 * e2 * e2 / 1024) * sin(4 * latitude1) - (35 * e2 * e2 * e2 / 3072) * sin( 6 * latitude1))
    xval = NN * (A + (1 - T + C) * A * A * A / 6 + (5 - 18 * T + T * T + 72 * C - 58 * ee) * A * A * A * A * A / 120)
    yval = M + NN * tan(latitude1) * (A * A / 2 + (5 - T + 9 * C + 4 * C * C) * A * A * A * A / 24 + (61 - 58 * T + T * T + 600 * C - 330 * ee) * A * A * A * A * A * A / 720)
    X0 = 1000000 * (ProjNo + 1) + 500000
    Y0 = 0
    xval = xval + X0
    yval = yval + Y0
    return xval, yval
