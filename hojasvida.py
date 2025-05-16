# 2. Consultar hojas de vida, con opciones para:
# • Buscar por nombre, documento o correo electrónico
# • Filtrar por años de experiencia, formación o habilidades
# • Visualizar en formato legible cada sección por separado o en conjunto

def search_by_document(document):
    return curriculum.get(document)

def search_by_name(partial_name):
    result = {id: info for id, info in curriculum.items() if partial_name.lower() in info["name"].lower()}
    return result


def search_by_mail(mail):
    result = {id: info for id, info in curriculum.items() if partial_name.lower() in info["name"].lower()}
    return result

def check_str(massage):#Esta función verifica que el valor ingresado no esté vacío.


    entry = input(massage).strip()
    if entry == "":
        print(" no puede estar vacio!")
        return check_str(massage)
    else :
        return entry
    



choice = input("ingrese :" )
#si es 2 primero preguntar si la busqueda es por nombre, documento y eso o de una vez coja los 3 en la busqueda
if choice == "2":

            ##aqui iria el hacer otro match o otros if elif por si lo hacemos pidiendo que tipo de busqueda quiere hacer

        document = check_str("Enter : ")  #pasamos con conv str para validar
        result = search_by_document(document)   #Mejor pedir directamente con el check_str
        if result:
            print(result)
        else:
            print("Not found.")


elif choice == "3":
            name = input("Enter name to search: ")
            results = search_by_name(name)
            if results:
                for sid, data in results.items():
                    print(f"ID: {sid}, Data: {data}")
            else:
                print("No  found.")



elif choice == "4":
            mail = input("Enter mail to search: ")
            results = search_by_mail(mail)
            if results:
                for sid, data in results.items():
                    print(f"ID: {sid}, Data: {data}")
            else:
                print("No  found.")

            
