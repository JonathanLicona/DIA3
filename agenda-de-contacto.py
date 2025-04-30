agenda_contacto = {}

def menu():
    while True:
        print("\n1.Agregar 2.Listar 3.Buscar 4.Actualizar 5.Eliminar 6.Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            n = input("Nombre: ")
            if n in agenda_contacto: print("Ya existe."); continue
            t, e = input("Teléfono: "), input("Email: ")
            agenda_contacto[n] = {'tel': t, 'email': e}
        elif opcion == "2":
            [print(f"{n} | {d['tel']} | {d['email']}") for n, d in agenda_contacto.items()]
        elif opcion == "3":
            n = input("Nombre: ")
            print(f"{n} | {agenda_contacto[n]['tel']} | {agenda_contacto[n]['email']}" if n in agenda_contacto else "No encontrado.")
        elif opcion == "4":
            n = input("Nombre: ")
            if n in agenda_contacto:
                t = input("Nuevo teléfono (enter = igual): ")
                e = input("Nuevo email (enter = igual): ")
                if t: agenda_contacto[n]['tel'] = t
                if e: agenda_contacto[n]['email'] = e
            else: print("No encontrado.")
        elif opcion == "5":
            n = input("Nombre: ")
            print("Eliminado." if agenda_contacto.pop(n, None) else "No encontrado.")
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

menu()
