students = {}

def check_id(student_id):
    if student_id in students:
        return True
    else:
        return False

def average(student_id):
    if len(students[student_id]['courses']) > 0:
        sum = 0
        for grade in students[student_id]['courses'].values():
            sum += grade
        try:
            return sum / len(students[student_id]['courses'])
        except ZeroDivisionError:
            print('Error: No se puede dividir por cero.')
        except Exception as e:
            print('Un error ha ocurrido.', e)
    else:
        return 'No hay notas registradas.'

def get_students_info(student_id):
    print(f'Nombre: {students[student_id]['name']}')
    print(f'Carrera: {students[student_id]['career']}')
    if len(students[student_id]['courses']) > 0:
        print('Notas:')
        for course, grade in students[student_id]['courses'].items():
            print(f'    Curso: {course} | Nota: {grade}')
    else:
        print('No hay notas registradas.\n')
    print()

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
                            print('Un error ha ocurrido.', e)

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
                    get_students_info(student_id)
                else:
                    print('Estudiante no registrado.\n')
            else:
                print('No hay estudiantes registrados.\n')

        case '4':
            if len(students) > 0:
                student_id = input('Ingrese el ID del estudiante: ')
                if check_id(student_id):
                    print('\nPROMEDIO:')
                    print(f'{average(student_id)}\n')
                else:
                    print('Estudiante no registrado.\n')
            else:
                print('No hay estudiantes registrados.\n')

        case '5':
            if len(students) > 0:
                student_id = input('Ingrese el ID del estudiante: ')
                if check_id(student_id):
                    if len(students[student_id]['courses']) > 0:
                        for grade in students[student_id]['courses'].values():
                            if grade < 61:
                                print('No aprobará todos los cursos.\n')
                                break
                            else:
                                print('Aprobará todos los cursos.\n')
                else:
                    print('Estudiante no registrado.\n')
            else:
                print('No hay estudiantes registrados.\n')

        case '6':
            if len(students) > 0:
                print('\nDATOS GENERALES:')
                for id in students.keys():
                    print(f'\nID: {id}')
                    get_students_info(id)
            else:
                print('No hay estudiantes registrados.\n')

        case '7':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción inválida. Intente nuevamente.\n')