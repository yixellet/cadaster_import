from pyproj import CRS, Transformer

def transform(coords, zone=1):
    msk_1 = CRS.from_proj4('+proj=tmerc +lat_0=0 +lon_0=46.05 +k=1 +x_0=1300000 +y_0=-4714743.504 +ellps=krass +towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +units=m +no_defs')
    msk_2 = CRS.from_proj4('+proj=tmerc +lat_0=0 +lon_0=49.05 +k=1 +x_0=2300000 +y_0=-4714743.504 +ellps=krass +towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +units=m +no_defs')
    tr = Transformer.from_crs(msk_1, 4326)
    wgs = tr.transform(coords[1], coords[0])
    return(wgs)

if __name__ == '__main__':
    print(transform([558880, 1341834]))