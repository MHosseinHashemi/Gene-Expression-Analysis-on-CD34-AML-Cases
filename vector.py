import math

class Vector():
    
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector."
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = "There is no unique parallel component."
    NO_UNIQUE_ORTHAGONAL_COMPONENT_MSG = "There is no unique orathagonal component."

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        
        except ValueError:
            raise ValueError("The coordinates must be nonempty")
        
        except TypeError:
            raise TypeError("The coordinates must be an iterable")
        

    def __str__(self):
        return "Vector: {}".format(self.coordinates)
    

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    

    def plus(self, v):
        new_coordinates = []
        for index in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[index] + v.coordinates[index])
        
        return Vector(new_coordinates)
    

    def minus(self, v):
        new_coordinates = []
        for index in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[index] - v.coordinates[index])
        
        return Vector(new_coordinates)
    

    def times_scaler(self, v):
        new_coordinates = []
        for value in self.coordinates:
            new_coordinates.append(value * v)
        
        return Vector(new_coordinates)


    def vector_mag_norm(self):
        normalized_magnitude = []
        for value in self.coordinates:
            value *= value
            normalized_magnitude.append(value)

        return math.sqrt(sum(normalized_magnitude))
    

    def vector_dir_norm(self):
        normalized_vector = []
        norm = self.vector_mag_norm()
        norm = 1 / norm
        for value in self.coordinates:
            normalized_vector.append(norm * value)
        
        return Vector(normalized_vector)
    

    def dot_product(self, v):
        dot_result = []
        for index in range(len(self.coordinates)):
            dot_result.append(self.coordinates[index] *  v.coordinates[index])

        return sum(dot_result)
    

    def vectors_angle(self, v):
        dot_res = self.dot_product(v)
        temp_var = self.vector_mag_norm() * v.vector_mag_norm()
        if temp_var == 0:
            print("Division by Zero!: One of your vectors is a Zero Vector")
        else:
            angle = math.acos(dot_res/temp_var)
            angle_in_degree = angle * 180/math.pi
        
        return angle, angle_in_degree
    

    def is_parallel(self, v):
        factor_list = []
        # Checking for Zero Vectors ... 
            # Part 1
        if self.coordinates[0] == 0:
            if len(set(self.coordinates)) == 1:
                return "One of the given vectors is a Zero Vector, Hence they are paralel"
            # Part 2
        elif v.coordinates[0] == 0:
            if len(set(v.coordinates)) == 1:
                return "One of the given vectors is a Zero Vector, Hence they are paralel"
        else:
            for index in range(len(self.coordinates)):
                factor_list.append("%.3f"%(self.coordinates[index] / v.coordinates[index]))
            if len(set(factor_list)) == 1:
                return "Yes! Two given vectors are parallel"
            else:
                return "No! Two given vectors are not parallel"

    
    def is_orthogonal(self, v):
        dot_res = round(self.dot_product(v), 3)
        if abs(dot_res) <= 0.001:
            return "Yes! Two given vectors are orthogonal"
        else:
            return "No! Two given vectors are not orthogonal"
            

    def parallel_component(self, b):
        try:
            unit = b.vector_dir_norm() 
            weight = self.dot_product(unit)
            return unit.times_scaler(weight)
        
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e


    def orthagonal_component(self, b):
        try:
            projection = self.parallel_component(b)
            return self.minus(projection)
            
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_ORTHAGONAL_COMPONENT_MSG)
            else:
                raise e


