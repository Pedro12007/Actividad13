students = {}

def check_id(student_id):
    if student_id in students:
        return True
    else:
        return False

while True:
    print('OPCIONES:')
    print('1. Agregar estudiantes.')
    print('2. Agregar curso con nota.')
    print('3. Consultar estudiante.')
    print('4. Calcular promedio de estudiante.')
    print('5. Verificar si un estudiante aprueba.')
    print('6. Mostrar a todos los estudiantes.')
    print('7. Salir del programa.')

    option = input('Elija una opción: ')
    print()

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
            print()

        case '2':
            if len(students) > 0:
                student_id = input('Ingrese el ID del estudiante: ')
                if check_id(student_id):
                    course_name = input('Ingrese el nombre del curso: ')
                    while True:
                        try:
                            grade = int(input('Ingrese la nota: '))
                            if grade < 0 or grade > 100:
                                print('Nota fuera de rango.\n')
                                continue
                            print()
                            break
                        except ValueError:
                            print('Error: Debe ser un número entero.\n')
                        except Exception as e:
                            print('Un error a ocurrido.', e)

                    students[student_id]['courses'][course_name] = grade
                else:
                    print('Estudiante no registrado.\n')
            else:
                print('No hay estudiantes registrados.\n')

        case '3':
            if len(students) > 0:
                student_id = input('Ingrese el ID del estudiante: ')
                if check_id(student_id):
                    print('\nDATOS:')
                    print(f'Nombre: {students[student_id]['name']}')
                    print(f'Carrera: {students[student_id]['career']}')
                    if len(students[student_id]['courses']) > 0:
                        print('Notas:')
                        for course, grade in students[student_id]['courses'].items():
                            print(f'Curso: {course} | Nota: {grade}')
                    else:
                        print('No hay notas registradas.\n')
                    print()
                else:
                    print('Estudiante no registrado.\n')

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