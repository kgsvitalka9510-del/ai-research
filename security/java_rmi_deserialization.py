"""Java RMI Deserialization Fix"""
import pickle
import io

class SafeUnpickler(pickle.Unpickler):
    """Safe unpickler that restricts allowed classes."""
    ALLOWED_CLASSES = {'builtins': ['dict', 'list', 'str', 'int', 'float', 'bool']}
    
    def find_class(self, module, name):
        if module in self.ALLOWED_CLASSES and name in self.ALLOWED_CLASSES[module]:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(f"Class {module}.{name} not allowed")

def safe_deserialize(data):
    """Safely deserialize data."""
    return SafeUnpickler(io.BytesIO(data)).load()
