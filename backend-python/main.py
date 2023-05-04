from flask import Flask, request
from flask_cors import CORS
import pandas
import numpy
positive_roots=[]
roots=[]
numberOfRoots=0
Front_table=[]
repeated_roots=[]
test=""
def showRes(routh_table,equation):
    eqroots = numpy.roots(equation)
    for i in range(len(eqroots)):
        eqroots[i]=numpy.round(eqroots[i], 3)
        if((eqroots[i] in roots) and complex(eqroots[i]).imag!=0):
            repeated_roots.append(eqroots[i])
        roots.append(numpy.round(eqroots[i], 3))

    for i in range(len(roots)):
        if (complex(roots[i]).real > 0):
            # print(all_roots[i])
            positive_roots.append(numpy.round(roots[i], 3))
    counter=0
    sign=[]
    for i in range (len(routh_table)):
        if(routh_table[i][0]>=0 ):
            sign.append("+")
        else:
            sign.append("-")

    for i in range(len(sign)-1):
        if(sign[i]!=sign[i+1]):
            counter=counter+1
    if(counter==0 and len(repeated_roots)==0):
        Front_table.append("_________________________________________________________")
        Front_table.append("System is STABLE")
        Front_table.append("Roots are : "+str(roots).replace("(","").replace(")","").replace("-0+","").replace("-0-","").replace("0-","").replace("0+",""))
        # Front_table.append(str(roots))

        print("System is STABLE")
        print("Roots are ")
        print(roots)
    elif (len(repeated_roots)!=0):
        Front_table.append("_________________________________________________________")
        Front_table.append("System is UNSTABLE because of Repeated Roots  ")
        Front_table.append("Roots are : "+str(roots).replace("(","").replace(")","").replace("-0+","").replace("-0","").replace("0+",""))
        Front_table.append("Repeated Roots are : "+str(repeated_roots).replace("(","").replace(")","").replace("-0+","").replace("-0","").replace("0+",""))


        print("System is UNSTABLE because of Repeated Roots  ")
        print("Roots are ")
        print(roots)
        print("Repeated Roots are ")
        print(repeated_roots)
    else:
        Front_table.append("_________________________________________________________")
        Front_table.append("System is UNSTABLE")
        Front_table.append("Roots are : "+str(roots).replace("(","").replace(")","").replace("-0+","").replace("-0","").replace("0+",""))

        Front_table.append("Number of positive roots = "+str(counter))

        print("System is UNSTABLE")
        print("Roots are ")
        print(roots)
        print("Number of positive roots = "+str(counter))
        numberOfRoots=counter
    if(len(positive_roots)!=0):
      Front_table.append("Positive roots are : "+str(positive_roots).replace("(","").replace(")","").replace("-0+","").replace("-0","").replace("0+",""))
      # Front_table.append(str(positive_roots))
      print("Positive roots are ")
      print(positive_roots)
    roots.clear()
    positive_roots.clear()
    repeated_roots.clear()

def find_Right_hand_Plan_roots(row,equation,power):
    return
    # auxiliary=[]
    # for i in range(len(row)):
    #     auxiliary.append(row[i])
    #     auxiliary.append(0)
    # while(len(auxiliary)!=power+1):
    #     auxiliary.pop(len(auxiliary)-1)
    # # print(auxiliary)
    # quotient, rx = numpy.polynomial.polynomial.polydiv(equation,auxiliary)
    # print(quotient)
    # all_roots=numpy.roots(quotient)
    # eqroots=numpy.roots(equation)
    # for i in range(len(eqroots)):
    #     if(not(numpy.round(eqroots[i],3) in roots)):
    #       roots.append(numpy.round(eqroots[i],3))
    #
    # for i in range(len(roots)):
    #     if(complex(roots[i]).real>0):
    #         # print(all_roots[i])
    #         positive_roots.append(numpy.round(roots[i],3))

def fix_zero_row(row,power,length):

    fixed_row=[]
    i=0

    while(power>=0 and i<len(row)):
        fixed_row.append(row[i]*power)
        i=i+1
        power=power-2
    return add_zeros(fixed_row, length)

def add_zeros(array, length):
    zero_row=True
    if len(array)!= length:
        for i in range(len(array), length):
            array.append(0)
    for i in range(0, length):
        if(array[i]!=0 and array[i]!="ε"):
            zero_row=False
    return array,zero_row

def Routh(equation,reversed,row_names,col_names,order):
 epsilon_used = False;
 routh_table = []
 first_row = []
 for i in range(0, len(equation),2):
    first_row.append(equation[i])
 routh_table.append(first_row)
 # Front_table.append(first_row)
 second_row = []
 for i in range(1, len(equation),2):
    second_row.append(equation[i])
 second_row,bool = add_zeros(second_row, len(first_row))
 routh_table.append(second_row)
 # Front_table.append(second_row)



 for i in range(2, len(equation)):
    layers = []
    for j in range(0, len(first_row) - 1):
        if (routh_table[i - 1][0] == 0):
            if(not reversed):
             reversed_equation = equation[::-1]
            elif(reversed):
             return
            Routh(reversed_equation,True,row_names,col_names,order)
            routh_table[i - 1][0] = "ε"
            epsilon_used = True
            layers.append(("("+routh_table[i - 1][0] + "*" + str(routh_table[i - 2][j + 1]) + "-" + str(routh_table[i - 2][0] * routh_table[i - 1][j + 1]) + ")/(" + routh_table[i - 1][0]+")"))
        elif (routh_table[i - 1][0] == "ε"):
            layers.append(("("+routh_table[i - 1][0] + "*" + str(routh_table[i - 2][j + 1]) + "-" + str(routh_table[i - 2][0] * routh_table[i - 1][j + 1]) + ")/(" + routh_table[i - 1][0]+")"))
        elif(type(routh_table[i - 1][0]) == str and routh_table[i - 1][0] != "ε"):
            layers.append(("("+routh_table[i - 1][0] + "*" + str(routh_table[i - 2][j + 1]) + "-" + str(
                routh_table[i - 2][0]) + "*" + str(routh_table[i - 1][j + 1]) + ")/(" + routh_table[i - 1][0]+")"))
        else:
            layers.append(
                round((routh_table[i - 1][0] * routh_table[i - 2][j + 1] - routh_table[i - 2][0] * routh_table[i - 1][j + 1]) / routh_table[i - 1][0],
                      2))
    layers,is_zero_row = add_zeros(layers, len(first_row))
    if(is_zero_row and order-(i-1)!=2 and order-(i-1)!=1):
     layers,bool=fix_zero_row(routh_table[i-1],order-(i-1),len(first_row))
    routh_table.append(layers)
    # if(is_zero_row and order-(i-1)==2):
    #   layers.append(routh_table[i-1][1])
    #   layers, is_zero_row = add_zeros(layers, len(first_row))
    #   routh_table.append(layers)
    #   i=  len(equation)
    #   break


    # Front_table.append(layers)
 if(not reversed and not epsilon_used  ):
  find_Right_hand_Plan_roots(None,equation,None)
  routh_table_data=pandas.DataFrame(routh_table)
  routh_table_data.index = row_names
  routh_table_data.columns=col_names
  print(routh_table_data)
  print("table")


  # for i in range(len(routh_table)):
  #  Front_table.append((routh_table[i]))
  Front_table.append("Routh Table : ")
  Front_table.append("_________________________________________________________")
  Front_table.append(str(routh_table_data))

  showRes(routh_table, equation)

  Front_table.append("----------------------------------------------------------------")


 if(reversed):
     routh_table_data = pandas.DataFrame(routh_table)
     routh_table_data.index = row_names
     routh_table_data.columns = col_names
     print(routh_table_data)
     print("reversed table")
     reversed_equation = equation[::-1]


     # for i in range(len(routh_table)):
     #
     #     Front_table.append((routh_table[i]))
     Front_table.append("Routh Table Using Reversed Equation Method : ")
     Front_table.append("_________________________________________________________")
     Front_table.append(str(routh_table_data))

     showRes(routh_table,reversed_equation)
     Front_table.append("----------------------------------------------------------------")


 # Front_table.append(routh_table)
  # Front_table.append("----------------------------------------------------------------")
 if(epsilon_used):
  routh_table_data = pandas.DataFrame(routh_table)
  routh_table_data.index = row_names
  routh_table_data.columns = col_names
  print(routh_table_data)
  print("epsilon table")
  # for i in range(len(routh_table)):
  #     Front_table.append((routh_table[i]))



  for i in range(len(routh_table)):
     for j in range(len(routh_table[0])):
         routh_table[i][j]=round(float(eval(str(str(routh_table[i][j]).replace("ε","0.001")))),4)
  routh_table_data = pandas.DataFrame(routh_table)
  routh_table_data.index=row_names
  routh_table_data.columns = col_names
  print(routh_table_data)
  print("epsilon evaluated table")
  Front_table.append("Routh Table Using Epsilon Method : ε = 0.001 ")
  Front_table.append("_________________________________________________________")
  Front_table.append(str(routh_table_data))
  showRes(routh_table,equation)
  Front_table.append("----------------------------------------------------------------")
  # for i in range(len(routh_table)):
  #     print(routh_table[i])
  #     Front_table.append(routh_table[i])
  # Front_table.append("----------------------------------------------------------------")


def get_coefficients(poly_string):
    poly_string.replace("S","s")
    # Split the polynomial string into its individual terms
    terms = poly_string.split('+')

    # Initialize a list to store the coefficients
    coefficients = []

    # Loop through each term and extract its coefficient
    for i in range(len(terms)-2):
        # Split the term into its coefficient and degree
        coefficient, degree = terms[i].split('s^')
        # Convert the coefficient to an integer if it's not empty, or 0 otherwise
        if coefficient == '':
            coefficients.append(1)
        else:
            coefficients.append(int(coefficient))
    coefficient = terms[len(terms) - 2].replace("s^1", "").replace("s","")
    if coefficient == '':
        coefficients.append(1)
    else:
        coefficients.append(int(coefficient))
    coefficient=int(terms[len(terms)-1].replace("s^0",""))
    coefficients.append(coefficient)

    return coefficients


def Main(data):
 Front_table.clear()
 order =data[0]
 user_input=data[1]
 equation = get_coefficients(user_input)
 print(equation)
 row_names=[]
 col_names=[]
 for i in range(int(order), -1, -1):
    # equation.append(int(input("Enter the coefficient of s^" + str(i) + ": ")))
    row_names.append("s^"+str(i)+" |")
 for i in range(int(order), -1, -2):
    col_names.append("")
 Routh(equation,False,row_names,col_names,int(order))
 return Front_table

 print("---------------------------------------------------------------------\n\n")
 power=int(order)
 for i in range(len(Front_table)):

     print(Front_table[i])

###### controller
app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

@app.route('/routh', methods=['POST'])
def run_my_code():
     data = request.get_json()
     Main(data)
     for i in range (len(Front_table)):
         Front_table[i]=str(Front_table[i])

     return Front_table


if __name__ == '__main__':
    app.run()
