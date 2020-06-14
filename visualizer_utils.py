from typing import List, Tuple

def convert_coordinates(arr: List[Tuple[float,float]], window_width: int, window_height: int, top_left_long: float, top_left_lat: float, long_size: float, lat_size: float) -> List[Tuple[float,float]]:
    '''
    Convert's lat long coordiantes in arr into coodrinates to be displayed.

    Args:
        arr:  List(Tuple(Float,Float)), arr we are coverting into pixel coordinates
        window_width: width of window (x axis)
        window_height: height of window (y axis)
        top_left_long: top left corner latitude coordinate (x)
        top_left_lat: top left corner long coordinate (y)
        long_size: longitude (x) covered across the window
        lat_size:  latitude (y) covered across the window
    '''
    converted = []

    for long, lat in arr:
        print(f'{long} {lat}')
        # takes distance from top left corner and then scales the distance by size of window
        x = int((abs(long - top_left_long)) * window_width/long_size)
        y = int(abs((lat - top_left_lat)) * window_height/lat_size)
        print(x)
        assert(x > 0)
        print(y)
        assert(y > 0)
        converted.append((x,y))
        
    return converted