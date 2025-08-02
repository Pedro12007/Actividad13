students = {}

def check_id(student_id):
    if student_id in students:
        return True
    else:
        return False

while True:
    print('Opciones:')
    print('1. Agregar estudiantes.')
    print('2. Agregar curso con nota.')
    print('3. Consultar estudiante.')
    print('4. Calcular promedio de estudiante.')
    print('5. Verificar si un estudiante aprueba.')
    print('6. Mostrar a todos los estudiantes.')
    print('7. Salir del programa.')

    option = input('Elija una opción: ')

    match option:
        case '1':
            student = {}
            while True:
                student_id = input('Ingrese el ID de estudiante: ')
                if not check_id(student_id):
                    break
                else:
                    print('ID ya existe. Intente nuevamente.\n')
            name = input('Ingrese el nombre: ')
            career = input('Ingrese carrera o programa académico: ')

            student['name'] = name
            student['career'] = career
            student['courses'] = {}

            students[student_id] = student

        case '2':
            while True:
                student_id = input('Ingrese el ID de estudiante: ')
                if check_id(student_id):
                    course_name = input('Ingrese el nombre del curso: ')
                    grade = int(input('Ingrese la nota: '))

                    students[student_id]['courses'][course_name] = grade

        case '3':
            pass

        case '4':
            pass

        case '5':
            pass

        case '6':
            pass

        case '7':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción inválida. Intente nuevamente.\n')