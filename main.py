path = "J:/OneDrive/Clase/Ingenieria informatica/Curso 2/PEL/Ejercicios/PEL-Actividad-Colaborativa/"
content = "#include<iostream>\n#include<string>\n#include<vector>\n\nusing namespace std;\n\nint main(int argc, char const *argv[]) {\n\n\treturn 0;\n}"
for i in range(1, 34):
    name = "Ejercicio" + str(i) + ".cpp"
    file = open(path+name, 'w')
    file.write(content)
    file.close()