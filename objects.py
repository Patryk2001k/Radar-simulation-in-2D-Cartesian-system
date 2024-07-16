import math

class Object:
    def __init__(self, position_x, position_y, speed_x, speed_y):
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed_x
        self.speed_y = speed_y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.grid = {} 
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)
        self.update_grid(obj)

    def update_grid(self, obj):
        x, y = int(obj.position_x), int(obj.position_y)
        self.grid[(x, y)] = obj

    def update(self):
        self.grid.clear()
        for obj in self.objects:
            obj.position_x += obj.speed_x
            obj.position_y += obj.speed_y
            self.update_grid(obj)

class Radar:
    def __init__(self, center_x, center_y, radius, angle_step, world):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.angle_step = angle_step
        self.current_angle = 0
        self.scanned_points = []
        self.world = world

    def is_within_circle(self, x, y):
        return (x - self.center_x)**2 + (y - self.center_y)**2 <= self.radius**2

    def is_within_angle(self, x, y):
        if x == 0 and y == 0:
            return True
        else:
            angle = math.degrees(math.atan2(y - self.center_y, x - self.center_x))
            angle = (angle + 360) % 360
            min_angle = self.current_angle
            max_angle = (self.current_angle + self.angle_step) % 360  
            if min_angle < max_angle:
                return min_angle <= angle <= max_angle
            else:
                return min_angle <= angle or angle <= max_angle

    def detect_object(self):
        for x in range(self.center_x - self.radius, self.center_x + self.radius + 1):
            for y in range(self.center_y - self.radius, self.center_y + self.radius + 1):
                if self.is_within_circle(x, y) and self.is_within_angle(x, y):
                    if (int(x), int(y)) in self.world.grid:
                        self.scanned_points.append((x, y, self.world.grid[(int(x), int(y))]))
                 
    def rotate_and_scan(self):
        self.scanned_points.clear()
        self.detect_object()
        print(f"Scanning angle range: ({self.current_angle}, {(self.current_angle + self.angle_step) % 360})")
        self.display_scanned_points()
        self.current_angle = (self.current_angle + self.angle_step) % 360

    def display_scanned_points(self):
        for point in self.scanned_points:
            print(f"Detected object at {point[0]}, {point[1]}")

# Example of how we can use it
# world = World(100, 100)
# obj = Object(0, 0, 0, 1)
# world.add_object(obj)
# radar = Radar(0, 0, 20, 45, world)

