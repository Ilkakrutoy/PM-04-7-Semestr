from datetime import datetime

class Tester:
    def test_module(self, module):
        is_valid, message = module.validate()

        result = {
            "module_name": module.name,
            "module_type": module.module_type,
            "status": "success" if is_valid else "error",
            "message": message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return result
