students = {} # Diccionario general donde se guardan los datos de todos los estudiantes.

def check_id(student_id):
    """
    Verifica si un ID ya está registrado.

    Args:
        student_id: ID del estudiante.
    Returns:
        bool: True si el estudiante está registrado, False si no.
    """
    if student_id in students:
        return True
    else:
        return False

def average(student_id):
    """
    Calcula el promedio del estudiante con el ID dado.

    Args:
        student_id: ID del estudiante.
    Returns:
        float: Promedio del estudiante si este tiene notas registradas.
        str: Mensaje que indique que no hay notas registradas.
    """
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
    """
    Imprime la información de un estudiante con ID dado.

    Args:
        student_id: ID del estudiante.
    Returns:
        None
    """
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
            # Agrega estudiantes.
            student = {} # Diccionario donde se guarda la información de cada estudiante.
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
            student['courses'] = {} # Diccionario donde se guardan los cursos.

            students[student_id] = student # Agrega al diccionario principal a cada estudiante.
            print()

        case '2':
            # Agrega los cursos y sus respectivas notas.
            if len(students) > 0:
                student_id = input('Ingrese el ID del estudiante: ')
                if check_id(student_id):
                    course_name = input('Ingrese el nombre del curso: ')
                    while True:
                        try:
                            grade = int(input('Ingrese la nota: '))
                            if grade < 0 or grade > 100: # Verifica si la nota está en el rango debido (0-100).
                                print('Nota fuera de rango.\n')
                                continue
                            print()
                            break
                        except ValueError:
                            print('Error: Debe ser un número entero.\n')
                        except Exception as e:
                            print('Un error ha ocurrido.', e)

                    students[student_id]['courses'][course_name] = grade # Agrega las notas al diccionario de notas de cada estudiante.
                else:
                    print('Estudiante no registrado.\n')
            else:
                print('No hay estudiantes registrados.\n')

        case '3':
            # Imprime los datos de un estudiante específico.
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
            # Imprime el promedio de un estudiante específico.
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
            # Imprime si el estudiante aprobó todos sus cursos.
            if len(students) > 0:
                student_id = input('Ingrese el ID del estudiante: ')
                if check_id(student_id):
                    if len(students[student_id]['courses']) > 0: # Verifica que el estudiante tenga notas.
                        counter = 0
                        for grade in students[student_id]['courses'].values():
                            if grade < 61: # Verifica si el estudiante tiene notas por debajo de 61.
                                counter += 1
                        if counter > 0:
                            print('No aprobará todos los cursos.\n')
                        else:
                            print('Aprobará todos los cursos.\n')
                else:
                    print('Estudiante no registrado.\n')
            else:
                print('No hay estudiantes registrados.\n')

        case '6':
            # Imprime los datos de todos los estudiantes.
            if len(students) > 0:
                print('\nDATOS GENERALES:')
                for id in students.keys(): # Recorre el diccionario students para obtener la información de cada estudiante.
                    print(f'\nID: {id}')
                    get_students_info(id)
            else:
                print('No hay estudiantes registrados.\n')

        case '7':
            # Termina el ciclo, así mismo terminando el programa.
            print('Saliendo del programa...')
            break

        case _:
            # Caso por defecto. En caso de tener un input inválido.
            print('Opción inválida. Intente nuevamente.\n')