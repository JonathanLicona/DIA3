biblioteca = {}

print("bienvenido al menu de la biblioteca principal")


def menu():
    while True:
        print("\n1.Agregar 2.Mostrar 3.Buscar ID 4.Buscar Título 5.Actualizar 6.Eliminar 7.Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            id = input("ID: ")
            if id in biblioteca:
                print("ID ya registrado.")
                continue
            t, a, y = input("Título: "), input("Autor: "), input("Año: ")
            biblioteca[id] = {'titulo': t, 'autor': a, 'anio': y}
        elif opcion == "2":
            [print(f"ID: {id} | Título: {d['titulo']} | Autor: {d['autor']} | Año: {d['anio']}")
             for id, d in biblioteca.items()]
        elif opcion == "3":
            id = input("ID: ")
            print(
                f"ID: {id} | Título: {biblioteca[id]['titulo']} | Autor: {biblioteca[id]['autor']} | Año: {biblioteca[id]['anio']}" if id in biblioteca else "No encontrado.")
        elif opcion == "4":
            t = input("Título: ").lower()
            e = [f"ID: {id} | Título: {d['titulo']} | Autor: {d['autor']} | Año: {d['anio']}" for id,
                 d in biblioteca.items() if d['titulo'].lower() == t]
            print("\n".join(e) if e else "No encontrado.")
        elif opcion == "5":
            id = input("ID: ")
            if id in biblioteca:
                a, y = input("Nuevo autor (enter = igual): "), input(
                    "Nuevo año (enter = igual): ")
                if a:
                    biblioteca[id]['autor'] = a
                if y:
                    biblioteca[id]['anio'] = y
                print("Actualizado.")
            else:
                print("No encontrado.")
        elif opcion == "6":
            id = input("ID: ")
            print("Eliminado." if biblioteca.pop(
                id, None) else "No encontrado.")
        elif opcion == "7":
            break
        else:
            print("Opción inválida.")


menu()
