class Solution:
    '''
    first we pick any point and form a line, from now on this is our new "base ground axis".
    Relatively, each line formed by another point and our location gets the angle marked in list

    sort all the angles

    sliding window - as much as we can fit in the angle interval + trick
    '''
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        #slope
        def angle_from_location(p):
            dy, dx = p[0] - location[0], p[1] - location[1]
            return math.degrees(math.atan2(dy, dx))


        #edge case + doing the slope
        same_location_count = 0
        angles = []
        for p in points:
            if p == location:
                same_location_count += 1
            else:
                angles.append(angle_from_location(p))

        #sort + wrapping in circle (case as 2deg and 355 for angle 30 is obviously within the sight but after sort it isnt, so we use the fact that it resets after 360deg and now 355-362 < 30)
        angles.sort()
        angles += [a + 360 for a in angles]


        max_points = 0
        left = 0
        #sliding window
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_points = max(max_points, right - left + 1)

        return max_points + same_location_count

