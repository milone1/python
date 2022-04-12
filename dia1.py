#programa que cambie de monedas.
print("===========OPCIONES=========");
print("1.- De soles a Dolares");
print("2.- De Dolares a soles");
print("3.- De soles a Euros");
print("4.- De Euros a soles");
option = "0"

while(option == "0"):
    value = input("Ingrese el monto:")
    option = input("Ingrese una opcion: ");
    if(option == "1"):
        dollar = float(value) / 3.80
        formatDollar = "$ {:,.2f}".format(dollar)
        print("El valor de soles a Dolares es de: ", str(formatDollar))
        response = input("Desea salir: yes o not: ")
        if(response == "yes"):
            option = "1"
        else:
            option = "0"
    elif(option == "2"):
        soles = float(value) * 3.80
        formatSoles = "s/ {:,.2f}".format(soles)
        print("El valor de soles a Dolares es de: ", str(formatSoles))
        response = input("Desea salir: yes o not: ")
        if(response == "yes"):
            option = "1"
        else:
            option = "0"
    elif(option == "3"):
        euros = float(value) / 4.05
        formatEuro = "€ {:,.2f}".format(euros)
        print("El valor de soles a Dolares es de: ", str(formatEuro))
        response = input("Desea salir: yes o not: ")
        if(response == "yes"):
            option = "1"
        else:
            option = "0"
    elif(option == "4"):
        soles = float(value) * 4.05
        formatSoles = "s/ {:,.2f}".format(soles)
        print("El valor de soles a Dolares es de: ", str(formatSoles))
        response = input("Desea salir: yes o not: ")
        if(response == "yes"):
            option = "1"
        else:
            option = "0"