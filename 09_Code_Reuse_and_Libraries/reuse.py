# Factory Class
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type.upper() == "CIRCLE":
            return Circle()
        elif shape_type.upper() == "SQUARE":
            return Square()
        else:
            raise ValueError("Tipe shape tidak diketahui")
