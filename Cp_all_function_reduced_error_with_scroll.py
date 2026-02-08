from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from symfit import Fit,Variable,Parameter,Eq,Ge
from tkinter import messagebox
import symfit as sf
import sympy as sp
from sympy.plotting import plot
F=[] #list function to store cp models without paramters & mainly to erase paramters during loping
FF=[]  #list of functions with parametrs after fitting
p=[]   # unable to find a way to count number of paramters in an experession [nops()]. so i am storing the nops along with the input functions
# paramters & variables
T = Variable('T')
a = Parameter('a')
b = Parameter('b')
c = Parameter('c')
d = Parameter('d')
e = Parameter('e')
f = Parameter('f')
g = Parameter('g')
# root just a name of GUI window
root =Tk()
root.title("Cp fitter")
root.geometry("3000x2000")
messagebox.showwarning(title="Select Cp function properly ", message="""Note:
1. select Cp models one by one from low temperature function
 2.If you reselecting a function, whatever the functions next to that selected before will be automatically deleted
   so select those again""")
tol=[0.2,0.3,0.3,0.3]
def plot():
    try:
        Cpd = np.genfromtxt(filepath)
        T_d = Cpd[:, 0]
        Cp_d = Cpd[:, 1]
        plt.plot(T_d, Cp_d, label="True")
        plt.xlabel("Temperature")
        plt.ylabel("Cp")
        plt.legend()
        plt.show()

    except:
        messagebox.showwarning(title="Selecct data file", message="Please select valid data file")
        print(filepath)
def file_open():
    root.filename = filedialog.askopenfilename(title="select a file",filetypes=(("dat files","*.dat"),("all files","*.*")))
    global filepath
    filepath = root.filename

def tol_F1():
    tol[0]=(r2_F1.get())
    #F1_R2_set_var=tol[0]
def tol_F2():
    tol[1]=(r2_F2.get())
def tol_F3():
    tol[2]=(r2_F3.get())
def tol_F4():
    tol[3]=(r2_F4.get())

def debye():
    #try:
        #del F[1::1]
        #del FF[1::1]
        #F[0]=a * T ** 3
        #F[0]=a * T ** 3
        #print(F)
    #except:
    F.clear()
    FF.clear()
    p.clear()
    F.append(a * T ** 3)
    FF.append(a * T ** 3)
    p.append(1)
    #print("FF=", FF)
    #print("F=",F)
    try:
        selected_funs.pack_forget()
        selected_funs = Label(root, text=F).grid(row=8, column=1, columnspan=3)
    except:
        selected_funs = Label(root, text=F).grid(row=8, column=1, columnspan=3)
def debye_and_electronic():
    #try:
        #del F[1::1]
        #del FF[1::1]
        #F[0] = a * T ** 3
        #F[0] = a * T ** 3
        # print(F)
        #print(F)
    #except:
    F.clear()
    FF.clear()
    p.clear()
    F.append(a * T ** 3 + b * T)
    FF.append(a * T ** 3+ b * T)
    p.append(2)
    #print("FF=",FF)
    #print("F=",F)
    try:
        selected_funs.pack_forget()
        selected_funs = Label(master=second_frame, text=F).grid(row=8, column=1, columnspan=3)
    except:
        selected_funs = Label(second_frame, text=F).grid(row=8, column=1, columnspan=3)
first_fun=StringVar()
first_fun.set(0)

Var_second_fn = StringVar()
Var_second_fn.set("--")
def Second_fun(Var_second_fn):
    try:
        del F[1::1]
        del FF[1::1]
        del p[1::1]
        if (Var_second_fn=="Maier kelly       [a + b*T + c*T^(-2)]"):
            F.append(a + b*T + c*T**(-2))
            FF.append(a + b * T + c * T ** (-2))
            p.append(3)
        elif (Var_second_fn=="MT Data           [a + b*T + c*T^(-2) + d*T^(2)]"):
            F.append(a + b * T + c * T ** (-2)+ d*T**(2))
            FF.append(a + b * T + c * T ** (-2)+ d*T**(2))
            p.append(4)
        elif (Var_second_fn=="Holland            [a + b*T + c*T^(-2) + d*T^(-0.5)]"):
            F.append(a + b*T + c*T**(-2) + d*T**(-0.5))
            FF.append(a + b*T + c*T**(-2) + d*T**(-0.5))
            p.append((4))
        elif (Var_second_fn=="Polynomial      [a + b*T + c*T^(2) + d*T^(-0.5)]"):
            F.append(a + b*T + c*T**(2) + d*T**(-0.5))
            FF.append(a + b*T + c*T**(2) + d*T**(-0.5))
            p.append((4))
        elif (Var_second_fn=="Hass - Fisher   [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5)]"):
            F.append(a + b*T + c*T**(-2) + d*T**(2) + e*T**(-0.5))
            FF.append(a + b*T + c*T**(-2) + d*T**(2) + e*T**(-0.5))
            p.append((5))
        elif (Var_second_fn=="Shomate          [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5) + f*T^(-3) + g/T ]"):
            F.append(a + b*T + c*T**(-2) + d*T**(2) + e*T**(-0.5) + f*T**(-3) + g/T )
            FF.append(a + b*T + c*T**(-2) + d*T**(2) + e*T**(-0.5) + f*T**(-3) + g/T )
            p.append((7))
    except:
        if (Var_second_fn == "Maier kelly       [a + b*T + c*T^(-2)]"):
            F.append(a + b * T + c * T ** (-2))
            FF.append(a + b * T + c * T ** (-2))
            p.append(3)
        elif (Var_second_fn == "MT Data           [a + b*T + c*T^(-2) + d*T^(2)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2))
            p.append(4)
        elif (Var_second_fn == "Holland            [a + b*T + c*T^(-2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_second_fn == "Polynomial      [a + b*T + c*T^(2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_second_fn == "Hass - Fisher   [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            p.append((5))
        elif (Var_second_fn == "Shomate          [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5) + f*T^(-3) + g/T ]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            p.append((7))
    try:
        selected_funs.pack_forget()
        selected_funs = Label(second_frame, text=F).grid(row=8, column=1, columnspan=3)
    except:
        selected_funs = Label(second_frame, text=F).grid(row=8, column=1, columnspan=3)
    #print(F)
    #print(FF)

Var_third_fn= StringVar()
Var_third_fn.set("--")
def Third_fun(Var_third_fn):
    try:
        del F[2::1]
        del FF[2::1]
        del p[2::1]
        if (Var_third_fn == "Maier kelly       [a + b*T + c*T^(-2)]"):
            F.append(a + b * T + c * T ** (-2))
            FF.append(a + b * T + c * T ** (-2))
            p.append(3)
        elif (Var_third_fn == "MT Data           [a + b*T + c*T^(-2) + d*T^(2)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2))
            p.append(4)
        elif (Var_third_fn == "Holland            [a + b*T + c*T^(-2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_third_fn == "Polynomial      [a + b*T + c*T^(2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_third_fn == "Hass - Fisher   [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            p.append((5))
        elif (Var_third_fn == "Shomate          [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5) + f*T^(-3) + g/T ]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            p.append((7))
    except:
        if (Var_third_fn == "Maier kelly       [a + b*T + c*T^(-2)]"):
            F.append(a + b * T + c * T ** (-2))
            FF.append(a + b * T + c * T ** (-2))
            p.append(3)
        elif (Var_third_fn == "MT Data           [a + b*T + c*T^(-2) + d*T^(2)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2))
            p.append(4)
        elif (Var_third_fn == "Holland            [a + b*T + c*T^(-2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_third_fn == "Polynomial      [a + b*T + c*T^(2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_third_fn == "Hass - Fisher   [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            p.append((5))
        elif (Var_third_fn == "Shomate          [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5) + f*T^(-3) + g/T ]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            p.append((7))
    try:
        selected_funs.pack_forget()
        selected_funs = Label(second_frame, text=F).grid(row=8, column=1, columnspan=3)
    except:
        selected_funs = Label(second_frame, text=F).grid(row=8, column=1, columnspan=3)
    #print(F)
    #print(FF)


Var_Fourth_fn= StringVar()
Var_Fourth_fn.set("--")

def Fourth_fun(Var_Fourth_fn):
    try:
        del F[3::1]
        del FF[3::1]
        del p[3::1]
        if (Var_Fourth_fn == "Maier kelly       [a + b*T + c*T^(-2)]"):
            F.append(a + b * T + c * T ** (-2))
            FF.append(a + b * T + c * T ** (-2))
            p.append(3)
        elif (Var_Fourth_fn == "MT Data           [a + b*T + c*T^(-2) + d*T^(2)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2))
            p.append(4)
        elif (Var_Fourth_fn == "Holland            [a + b*T + c*T^(-2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_Fourth_fn == "Polynomial      [a + b*T + c*T^(2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_Fourth_fn == "Hass - Fisher   [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            p.append((5))
        elif (Var_Fourth_fn == "Shomate          [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5) + f*T^(-3) + g/T ]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            p.append((7))
    except:
        if (Var_Fourth_fn == "Maier kelly       [a + b*T + c*T^(-2)]"):
            F.append(a + b * T + c * T ** (-2))
            FF.append(a + b * T + c * T ** (-2))
            p.append(3)
        elif (Var_Fourth_fn == "MT Data           [a + b*T + c*T^(-2) + d*T^(2)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2))
            p.append(4)
        elif (Var_Fourth_fn == "Holland            [a + b*T + c*T^(-2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_Fourth_fn == "Polynomial      [a + b*T + c*T^(2) + d*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            FF.append(a + b * T + c * T ** (2) + d * T ** (-0.5))
            p.append((4))
        elif (Var_Fourth_fn == "Hass - Fisher   [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5)]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5))
            p.append((5))
        elif (Var_Fourth_fn == "Shomate          [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5) + f*T^(-3) + g/T ]"):
            F.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            FF.append(a + b * T + c * T ** (-2) + d * T ** (2) + e * T ** (-0.5) + f * T ** (-3) + g / T)
            p.append((7))
    try:
        selected_funs.pack_forget()
        selected_funs = Label(second_frame, text=F).grid(row=8, column=1, columnspan=3)
    except:
        selected_funs = Label(second_frame, text=F).grid(row=8, column=1, columnspan=3)
    #print(F)
    #print(FF)
def regression():
    global result
    messagebox.showinfo("Please Wait", "This operation will take several minutes  PLEASE WAIT")
    Cpd = np.genfromtxt(filepath)
    T_d = Cpd[:, 0]
    Cp_d = Cpd[:, 1]
    ip = p[0]
    for i in range(ip, len(Cpd), 1):
        model = F[0]
        T_d1 = T_d[0:i + 1]  # i+1 beacuse of range(ip,i+1) is ip to i
        Cp_d1 = Cp_d[0:i + 1]
        fit = Fit(model, T_d1, Cp_d1)
        fit_result = fit.execute()
        rse = ((fit_result.objective_value)/(len(T_d1)-p[0]))**0.5
        if (rse <= tol[0]):
            try:
                FF[0] = FF[0].subs(a, fit_result.value(a))
                FF[0] = FF[0].subs(b, fit_result.value(b))
            except:
                FF[0] = FF[0].subs(a, fit_result.value(a))
            #print("0 to ", i)
            #print(FF[0])
            #print(rse)
        else:
            break
        FF[0] = F[0]
    i = i - 1  # revising privious value to loop
    model = F[0]
    T_d1 = T_d[0:i + 1]
    Cp_d1 = Cp_d[0:i + 1]
    fit = Fit(model, T_d1, Cp_d1)
    fit_result = fit.execute()
    rse = ((fit_result.objective_value)/(len(T_d1)-p[0]))**0.5
    if (rse < tol[0]):
        try:
            FF[0] = FF[0].subs(a, fit_result.value(a))
            FF[0] = FF[0].subs(b, fit_result.value(b))
        except:
            FF[0] = FF[0].subs(a, fit_result.value(a))
    else:
        print("for first Cp function r_sq is poor")
    Brk_points = np.empty(len(F) + 1, int)
    TK = np.empty(len(FF) + 1, float)
    TK[0] = 0
    Brk_points[0] = 0
    Brk_points[1] = i
    TK[1] = T_d[i]
    for v in range(1,len(FF),1):
        val = FF[v - 1].subs(T, TK[v])
        slope = sf.diff(FF[v - 1], T).subs(T, TK[v])
        ip = Brk_points[v] + p[v]
        for i in range( len(Cpd),ip,-1):
            FF[v] = F[v]
            model = F[v]
            T_d1 = T_d[Brk_points[v]:i]
            Cp_d1 = Cp_d[Brk_points[v]:i]
            constraints = [Eq((FF[v].subs(T, T_d[Brk_points[v]])), val),Eq((sf.diff(FF[v], T).subs(T, T_d[Brk_points[v]])), slope)]
            fit = Fit(model, T_d1, Cp_d1, constraints=constraints)
            fit_result = fit.execute()
            rse=((fit_result.objective_value)/(len(T_d1)-p[v]))**0.5
            if (rse>= tol[v]):
                pass
            else:
                break
        if(1==ip and rse>tol[v]):
            print("function in position" + str(v+1) + "is no fitting properly with r_sq = "+str(r_sq))
            break

        try:
            FF[v] = FF[v].subs(a, fit_result.value(a))
            FF[v] = FF[v].subs(b, fit_result.value(b))
            FF[v] = FF[v].subs(c, fit_result.value(c))
            FF[v] = FF[v].subs(d, fit_result.value(d))
            FF[v] = FF[v].subs(e, fit_result.value(e))
            FF[v] = FF[v].subs(f, fit_result.value(f))
            FF[v] = FF[v].subs(g, fit_result.value(g))
        except:
            try:
                FF[v] = FF[v].subs(a, fit_result.value(a))
                FF[v] = FF[v].subs(b, fit_result.value(b))
                FF[v] = FF[v].subs(c, fit_result.value(c))
                FF[v] = FF[v].subs(d, fit_result.value(d))
                FF[v] = FF[v].subs(e, fit_result.value(e))
                FF[v] = FF[v].subs(f, fit_result.value(f))
            except:
                try:
                    FF[v] = FF[v].subs(a, fit_result.value(a))
                    FF[v] = FF[v].subs(b, fit_result.value(b))
                    FF[v] = FF[v].subs(c, fit_result.value(c))
                    FF[v] = FF[v].subs(d, fit_result.value(d))
                    FF[v] = FF[v].subs(e, fit_result.value(e))
                except:
                    try:
                        FF[v] = FF[v].subs(a, fit_result.value(a))
                        FF[v] = FF[v].subs(b, fit_result.value(b))
                        FF[v] = FF[v].subs(c, fit_result.value(c))
                        FF[v] = FF[v].subs(d, fit_result.value(d))
                    except:
                        FF[v] = FF[v].subs(a, fit_result.value(a))
                        FF[v] = FF[v].subs(b, fit_result.value(b))
                        FF[v] = FF[v].subs(c, fit_result.value(c))

        #print(FF[v])
        Brk_points[v + 1] = i-1   # range of python range(0:i), has 0to i-1
        TK[v + 1] = T_d[i-1]
    print("FF=",FF)
    print("TK:",TK)
    model_data = np.empty(Brk_points[v + 1] + 1, float)
    from sympy.plotting import plot
    if(len(F)==3):
        p1 = plot(FF[0], (T, 0, TK[1]), legend=True, label='fn 1', line_color='red', show=False)
        p1.extend(plot(FF[1], (T, TK[1], TK[2]), legend=True, label='fn 3', line_color='b', show=False))
        p1.extend(plot(FF[2], (T, TK[2], TK[3]), legend=True, label='fn 3', line_color='c', show=False))
        #p1.extend(T_d,Cp_d, legend = True, label ='DATA',line_color='bo')
        p1.show()
        for fi in range(0, len(model_data), 1):
            if (fi <= Brk_points[1]):
                model_data[fi] = FF[0].subs(T, T_d[fi])
            elif (fi > Brk_points[1] and fi <= Brk_points[2]):
                model_data[fi] = FF[1].subs(T, T_d[fi])
            elif (fi > Brk_points[2] and fi <= Brk_points[3]):
                model_data[fi] = FF[2].subs(T, T_d[fi])
        plt.plot(T_d[Brk_points[0]:Brk_points[1]+1], model_data[Brk_points[0]:Brk_points[1]+1], color="black", label="Fn 1")
        plt.plot(T_d[Brk_points[1]:Brk_points[2]+1], model_data[Brk_points[1]:Brk_points[2]+1], color="red", label="Fn 2")
        plt.plot(T_d[Brk_points[2]:Brk_points[3]+1], model_data[Brk_points[2]:Brk_points[3]+1], color="green", label="Fn 3")
        plt.plot(T_d[0:Brk_points[3] + 1], Cp_d[0:Brk_points[3] + 1],'x', label="Measured")
        plt.legend()
        plt.show()

        result = FF[0], "\t valid from  ", str(TK[0]) + '\t', str(TK[1]), '\n', FF[1], "\t valid from  ", str(TK[1]), '\t', str(TK[2]), '\n', FF[2], "\t valid from  ", str(TK[2]), '\t', str(TK[2])


    elif(len(FF)==2):
        p1 = plot(FF[0], (T, 0, TK[1]), legend=True, label='function 1', line_color='red', show=False)
        p1.extend(plot(FF[1], (T, TK[1], TK[2]), legend=True, label='function 2', line_color='b', show=False))
        p1.show()
        for fi in range(0, len(model_data), 1):
            if (fi < Brk_points[1]):
                model_data[fi] = FF[0].subs(T, T_d[fi])
            else:
                model_data[fi] = FF[1].subs(T, T_d[fi])
        plt.plot(T_d[Brk_points[0]:Brk_points[1] + 1], model_data[Brk_points[0]:Brk_points[1] + 1], color="black", label="Fn 1")
        plt.plot(T_d[Brk_points[1]:Brk_points[2] + 1], model_data[Brk_points[1]:Brk_points[2] + 1], color="red", label="Fn 2")
        plt.plot(T_d[0:Brk_points[2] + 1], Cp_d[0:Brk_points[2] + 1],'x',label="Measured")
        plt.legend()
        plt.show()
        result = FF[0], "\t valid from  " , str(TK[0]) + '\t' , str(TK[1]) ,'\n', FF[1] , "\t valid from  " , str(TK[1]) , '\t' , str(TK[2])

        #result = FF[0], "\t valid from  ", str(TK[0]) + '\t', str(TK[1]), '\n', FF[1], "\t valid from  ", str(TK[1]), '\t', str(TK[2])
    elif (len(F) == 4):
        p1 = plot(FF[0], (T, 0, TK[1]), legend=True, label='function 1', line_color='red', show=False)
        p1.extend(plot(FF[1], (T, TK[1], TK[2]), legend=True, label='function 2', line_color='b', show=False))
        p1.extend(plot(FF[2], (T, TK[2], TK[3]), legend=True, label='function 3', line_color='c', show=False))
        p1.extend(plot(FF[3], (T, TK[3], TK[4]), legend=True, label='function 4', line_color='m', show=False))
        p1.show()

        for fi in range(0, len(model_data), 1):
            if (fi <= Brk_points[1]):
                model_data[fi] = FF[0].subs(T, T_d[fi])
            elif (fi > Brk_points[1] and fi <= Brk_points[2]):
                model_data[fi] = FF[1].subs(T, T_d[fi])
            elif (fi > Brk_points[2] and fi <= Brk_points[3]):
                model_data[fi] = FF[2].subs(T, T_d[fi])
            elif (fi > Brk_points[3]):
                model_data[fi] = FF[3].subs(T, T_d[fi])
        plt.plot(T_d[Brk_points[0]:Brk_points[1] + 1], model_data[Brk_points[0]:Brk_points[1] + 1], color="black", label="Fn 1")
        plt.plot(T_d[Brk_points[1]:Brk_points[2] + 1], model_data[Brk_points[1]:Brk_points[2] + 1], color="red", label="Fn 2")
        plt.plot(T_d[Brk_points[2]:Brk_points[3] + 1], model_data[Brk_points[2]:Brk_points[3] + 1], color="green", label="Fn 3")
        plt.plot(T_d[Brk_points[3]:Brk_points[4] + 1], model_data[Brk_points[3]:Brk_points[4] + 1], color="green", label="Fn 4")
        plt.plot(T_d[0:Brk_points[3] + 1], Cp_d[0:Brk_points[3] + 1],'x',label="Measured")
        plt.legend()
        plt.show()

        result = FF[0], "\t valid from  ", str(TK[0]) + '\t', str(TK[1]), '\n', FF[1], "\t valid from  ", str(TK[1]), '\t', str(TK[2]),'\n', FF[2], "\t valid from  ", str(TK[2]), '\t', str(TK[2]),'\n', FF[3], "\t valid from  ", str(TK[3]), '\t', str(TK[4])
    top=Toplevel()
    top.geometry("1700x1200")
    top.title("Output Cp functions")
    Label(top,text= result).pack()
    top.mainloop()

from tkinter import ttk

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_scrollbar_H = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
my_scrollbar_H.pack(side=BOTTOM, fill=X)
# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))


my_canvas.configure(xscrollcommand=my_scrollbar_H.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)
# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")



myLabel = Label(second_frame, text = "This is a simple programme to do segmented regression of cp data with popular Cp functions").grid(row =0,column=0)
file_open_label = Label(second_frame, text ="Select the data file ---->",borderwidth=1,relief= "solid",bg="yellow",font=('Helvetica', 18, 'bold')).grid(row = 1,column =0,padx =40 ,pady =40)
#opening data file & ploting graph
file_open =Button(second_frame, text = "open file", command =file_open,borderwidth=3).grid(row=1, column=1,sticky =W)
plot_graph = Button(second_frame,text ="Plot Graph",command =plot).grid(row=2,column=0)
#first function or low temperature function
First_function=Label(second_frame,text = "Low temperature function:",borderwidth=1,relief= SUNKEN,font=('Helvetica', 15, 'bold')).grid(row=3,column=1)
Debye_button=Radiobutton(second_frame, text ="Debye [ a*T^3 ]",variable=first_fun,value=a*T**3,command = debye).grid(row=3, column =2,sticky=W)
Debye_plus_electronic_button=Radiobutton(second_frame, text ="Debye + Electronic [ a*T^3+ b*T ]",variable=first_fun,value=a*T**3+b*T,command=debye_and_electronic).grid(row=4, column =2,sticky =W)
#second function
Second_function=Label(second_frame,text = "Second Cp function:",borderwidth=1,relief= SUNKEN,font=('Helvetica', 15, 'bold')).grid(row=5,column=1)
function_2 =OptionMenu(second_frame, Var_second_fn, "Maier kelly       [a + b*T + c*T^(-2)]","MT Data           [a + b*T + c*T^(-2) + d*T^(2)]","Holland            [a + b*T + c*T^(-2) + d*T^(-0.5)]","Polynomial      [a + b*T + c*T^(2) + d*T^(-0.5)]","Hass - Fisher   [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5)]","Shomate          [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5) + f*T^(-3) + g/T ]" ,command=Second_fun).grid(row=5, column =2,pady =50,sticky =W)
#third function
third_function=Label(second_frame,text = "Third Cp function:",borderwidth=1,relief= SUNKEN,font=('Helvetica', 15, 'bold')).grid(row=6,column=1)
function_3 =OptionMenu(second_frame, Var_third_fn, "Maier kelly       [a + b*T + c*T^(-2)]","MT Data           [a + b*T + c*T^(-2) + d*T^(2)]","Holland            [a + b*T + c*T^(-2) + d*T^(-0.5)]","Polynomial      [a + b*T + c*T^(2) + d*T^(-0.5)]","Hass - Fisher   [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5)]","Shomate          [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5) + f*T^(-3) + g/T ]",command=Third_fun ).grid(row=6, column =2,pady =40,sticky =W)
#fourth function
fourth_function=Label(second_frame,text = "Fourth Cp function:",borderwidth=1,relief= SUNKEN,font=('Helvetica', 15, 'bold')).grid(row=7,column=1)
function_4 =OptionMenu(second_frame, Var_Fourth_fn,"Maier kelly       [a + b*T + c*T^(-2)]","MT Data           [a + b*T + c*T^(-2) + d*T^(2)]","Holland            [a + b*T + c*T^(-2) + d*T^(-0.5)]","Polynomial      [a + b*T + c*T^(2) + d*T^(-0.5)]","Hass - Fisher   [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5)]","Shomate          [a + b*T + c*T^(-2) + d*T^(2) + e*T^(-0.5) + f*T^(-3) + g/T ]",command = Fourth_fun).grid(row=7, column =2,pady =40,sticky =W)

Final_funs_text=Label(second_frame, text = "Selected functions:",borderwidth=2,relief= SUNKEN,font=('Helvetica', 17, 'bold'),bg="yellow").grid(row =8,column=0)

do_regression_button = Button(second_frame,text= "DO FITTING",borderwidth=4,relief= SUNKEN,font=('Helvetica', 20, 'bold'),bg="black",fg="green",command=regression).grid(row=9,column=1,columnspan=2,rowspan=2,padx=100,pady=50)
rsqlabel=Label(second_frame,text="Sum of Sqares of Residuals",borderwidth=1,relief= "solid",bg="white",font=('Helvetica', 12, 'bold')).grid(row=1,column=6)
r2_F1=DoubleVar()
r2_F1.set(tol[0])
scale_F1 = Scale(second_frame,variable =r2_F1, from_= 0, to =1,resolution=0.001,orient=HORIZONTAL,length=250).grid(row=3, column =6,padx=20)
r2_F1_Button=Button(second_frame,text="Set",command=tol_F1).grid(row=3, column =7,padx=30)
#F1_R2_set_var=DoubleVar()
#F1_R2_set=Label(textvar=F1_R2_set_var,bg="white").grid(row=3, column =8,padx=30)
r2_F2=DoubleVar()
r2_F2.set(tol[1])
scale_F2 = Scale(second_frame, variable =r2_F2, from_= 0, to =1,resolution=0.001,orient=HORIZONTAL,length=250).grid(row=5, column =6,padx=20)
r2_F2_Button=Button(second_frame,text="Set",command=tol_F2).grid(row=5, column =7,padx=30)
r2_F3=DoubleVar()
r2_F3.set(tol[2])
scale_F3 = Scale(second_frame,  variable =r2_F3, from_= 0, to =1,resolution=0.001,orient=HORIZONTAL,length=250).grid(row=6, column =6,padx=20)
r2_F3_Button=Button(second_frame,text="Set",command=tol_F3).grid(row=6, column =7,padx=30)
r2_F4=DoubleVar()
r2_F4.set(tol[3])
scale_F4 = Scale(second_frame, variable =r2_F4, from_= 0, to =1,resolution=0.001,orient=HORIZONTAL,length=250).grid(row=7, column =6,padx=20)
r2_F4_Button=Button(second_frame,text="Set",command=tol_F4).grid(row=7, column =7,padx=30)




root.mainloop()



print(p)
print(FF)
print(tol)