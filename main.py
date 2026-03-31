from module import Module
from tester import Tester
from file_manager import FileManager

def main():
    print("=== Тестирование программного модуля ===")

    name = input("Введите название модуля: ")
    module_type = input("Введите тип модуля: ")

    module = Module(name, module_type)

    tester = Tester()
    result = tester.test_module(module)

    print("\nРезультат тестирования:")
    print(result)

    FileManager.save_result(result)
    print("Результат сохранен в файл results.json")

if __name__ == "__main__":
    main()
