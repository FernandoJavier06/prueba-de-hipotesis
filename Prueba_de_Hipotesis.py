from customtkinter import*
from tkinter import filedialog
from tkinter import*
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from normal import Dist_normal as dn
from tstudent import Dist_student as ds
from chicuadrado import Dist_chi as dc
from pdf_Z import pdf_Z
from pdf_P import pdf_P
from pdf_T import pdf_T
from pdf_C import pdf_C


#colores
color1= "#1b1a19"
color2= "#323130"
color3= "#797775"
color4 = "#c8c6c4"

#figuras para las graficas
canvas = None

#raiz del tkinter
raiz = CTk()
raiz.title("Prueba de Hipótesis")
raiz.resizable(False,False)
raiz.configure(fg_color	= color1)

#obtiene el tamaño de la pantalla
h_pantalla = raiz.winfo_screenheight()
w_pantalla = raiz.winfo_screenwidth()

#divide entre 2 para conseguir el centro y 1.8 en la altura de la app por la barra de tareas
h_pantalla = int(h_pantalla/2 - 720/2)
w_pantalla = int(w_pantalla/2 - 1080/2)

raiz.geometry(f"1080x720+{w_pantalla}+{h_pantalla}")#tamanio y posicion

#varibles de graficasZ
n = StringVar()    
alpha = StringVar()   
P = StringVar()     
smean = StringVar()  
sd = StringVar()
#variables de graficaP      
P = StringVar()       
p = StringVar()
nP = StringVar()
alphaP = StringVar()
#variables para grafica t 
nT = StringVar()    
alphaT = StringVar()   
pmeanT = StringVar()     
smeanT = StringVar()  
sdT = StringVar()
#variales para grafica chi2
nC = StringVar()    
alphaC = StringVar()   
pvar = StringVar()     
svar = StringVar() 

#variable para elegir la cola
tipo_cola = IntVar(raiz)#1: cola izquierda, 2:cola derecha, 3: dos colas
cola_izquierda = False
dos_colas = False

#botones para imprimir pdf
pdf_btn = None
pdfP_btn =None
pdf_btnT = None
pdf_btnC = None

#frames 
#frame de opciones
option_frame =CTkFrame(master = raiz, fg_color=color2)
option_frame.grid(column = 0, row = 0, sticky = 'nsew', padx = 5, pady = 5)

#frame de grafica
graph_frame = CTkFrame(master= raiz, fg_color= "#605e5c" )
graph_frame.grid(column = 1, row = 0, sticky = 'nsew', padx =5,pady= 5)

#frame de datos
values_frame = CTkFrame(master= raiz, fg_color=color2)
values_frame.grid(column = 0, row = 1, sticky = 'nsew', padx =5,pady= 5, columnspan = 2)

values_frame_adaptable = None

#configuracion del grid para los frames
raiz.columnconfigure(0,weight = 1)
raiz.columnconfigure(1,weight = 12)

raiz.rowconfigure(0, weight = 12)
raiz.rowconfigure(1, weight = 1)

grafica_Z = None
grafica_ZPDF1 = None
grafica_ZPDF2 = None

grafica_P = None
grafica_PPDF1 = None
grafica_PPDF2 = None

grafica_T = None
grafica_TPDF1 = None
grafica_TPDF2 = None

grafica_c = None
grafica_cPDF1 = None
grafica_cPDF2 = None


#FUNCIONES PARA GRAFICAR
def graficarZ():
    
    global canvas, tipo_cola, cola_izquierda, dos_colas, pdf_btn, grafica_Z, grafica_ZPDF1,grafica_ZPDF2
    
    if tipo_cola.get() == 1:
        cola_izquierda = True
        dos_colas = False
    elif tipo_cola.get() == 2:
        cola_izquierda = False
        dos_colas = False
    elif tipo_cola.get() == 3:
        cola_izquierda = False
        dos_colas = True
    else: 
        print("error al asignar el tipo de cola")
        
    if(canvas != None):
            canvas.get_tk_widget().destroy()
    grafica_Z = dn(float(eval(n.get())), float(eval(alpha.get())), float(eval(P.get())), float(eval(smean.get())), 
                   float(eval(sd.get())), 0, 0, dos_colas, cola_izquierda, isproporcion=False,isPDF=False,viewZp=True,imagen='')
    grafica_ZPDF1 = dn(float(eval(n.get())), float(eval(alpha.get())), float(eval(P.get())), float(eval(smean.get())), 
                   float(eval(sd.get())), 0, 0, dos_colas, cola_izquierda, isproporcion=False,isPDF=True,viewZp=False,
                   imagen='imagenes/grafica1.png')
    grafica_ZPDF2 = dn(float(eval(n.get())), float(eval(alpha.get())), float(eval(P.get())), float(eval(smean.get())), 
                   float(eval(sd.get())), 0, 0, dos_colas, cola_izquierda, isproporcion=False,isPDF=True,viewZp=True,
                   imagen='imagenes/grafica2.png')
    fig_n = grafica_Z.ejecutar()
    #declarar canvas para la grafica
    canvas = FigureCanvasTkAgg(fig_n, master = graph_frame)  # Crea el area de dibujo en Tkinter

    canvas.get_tk_widget().place(bordermode= 'inside', x= 60, y= 25, relheight= 0.9, relwidth= 0.899)
    
    pdf_btn.configure(state = NORMAL, fg_color = color3)

def graficarP():
    global canvas, tipo_cola, cola_izquierda, dos_colas, pdfP_btn, grafica_P,grafica_PPDF1,grafica_PPDF2
    if tipo_cola.get() == 1:
        cola_izquierda = True
        dos_colas = False
    elif tipo_cola.get() == 2:
        cola_izquierda = False
        dos_colas = False
    elif tipo_cola.get() == 3:
        cola_izquierda = False
        dos_colas = True
    else: 
        print("error al asignar el tipo de cola")
        
    if(canvas != None):
            canvas.get_tk_widget().destroy()
    grafica_P = dn(float(eval(nP.get())), float(eval(alphaP.get())), 0, 0, 
                   0, float(eval(P.get())) , float(eval(p.get())), dos_colas, cola_izquierda, isproporcion=True, isPDF=False, viewZp=True,imagen='')
    grafica_PPDF1 = dn(float(eval(nP.get())), float(eval(alphaP.get())), 0, 0, 
                   0, float(eval(P.get())) , float(eval(p.get())), dos_colas, cola_izquierda, isproporcion=True, isPDF=True, viewZp=False,
                   imagen='imagenes/grafica1.png')
    grafica_PPDF2 = dn(float(eval(nP.get())), float(eval(alphaP.get())), 0, 0, 
                   0, float(eval(P.get())) , float(eval(p.get())), dos_colas, cola_izquierda, isproporcion=True, isPDF=True, viewZp=True,
                   imagen='imagenes/grafica2.png')
    fig_n = grafica_P.ejecutar()
    #declarar canvas para la grafica
    canvas = FigureCanvasTkAgg(fig_n, master = graph_frame)  # Crea el area de dibujo en Tkinter

    canvas.get_tk_widget().place(bordermode= 'inside', x= 60, y= 25, relheight= 0.9, relwidth= 0.899)
    
    pdfP_btn.configure(state = NORMAL, fg_color = color3)
    
def graficarT():
    
    global canvas, tipo_cola, cola_izquierda, dos_colas,pdf_btnT, grafica_T, grafica_TPDF1, grafica_TPDF2
   
    if tipo_cola.get() == 1:
        cola_izquierda = True
        dos_colas = False
    elif tipo_cola.get() == 2:
        cola_izquierda = False
        dos_colas = False
    elif tipo_cola.get() == 3:
        cola_izquierda = False
        dos_colas = True
    else: 
        print("error al asignar el tipo de cola")
        
    if(canvas != None):
            canvas.get_tk_widget().destroy()
            
    grafica_T = ds(float(eval(nT.get())),float(eval(pmeanT.get())),float(eval(sdT.get())) ,float(eval(alphaT.get())),float(eval(smeanT.get())),
                dos_colas, cola_izquierda, isPDF=False,viewtp=True,imagen='')
    grafica_TPDF1 = ds(float(eval(nT.get())),float(eval(pmeanT.get())),float(eval(sdT.get())) ,float(eval(alphaT.get())),float(eval(smeanT.get())),
                dos_colas, cola_izquierda, isPDF=True,viewtp=False,imagen='imagenes/grafica1.png')
    grafica_TPDF2 = ds(float(eval(nT.get())),float(eval(pmeanT.get())),float(eval(sdT.get())) ,float(eval(alphaT.get())),float(eval(smeanT.get())),
                dos_colas, cola_izquierda, isPDF=True,viewtp=True,imagen='imagenes/grafica2.png')
    fig_n = grafica_T.ejecutar()
    #declarar canvas para la grafica
    canvas = FigureCanvasTkAgg(fig_n, master = graph_frame)  # Crea el area de dibujo en Tkinter

    canvas.get_tk_widget().place(bordermode= 'inside', x= 60, y= 25, relheight= 0.9, relwidth= 0.899)
    
    pdf_btnT.configure(state = NORMAL, fg_color = color3)

def graficarC():
    
    global canvas, tipo_cola, cola_izquierda, dos_colas,pdf_btnC, grafica_c, grafica_cPDF1, grafica_cPDF2
    
    if tipo_cola.get() == 1:
        cola_izquierda = True
        dos_colas = False
    elif tipo_cola.get() == 2:
        cola_izquierda = False
        dos_colas = False
    elif tipo_cola.get() == 3:
        cola_izquierda = False
        dos_colas = True
    else: 
        print("error al asignar el tipo de cola")
        
    if(canvas != None):
            canvas.get_tk_widget().destroy()
    grafica_c = dc(float(eval(nC.get())), float(eval(pvar.get())),  float(eval(svar.get())),float(eval(alphaC.get())), 
                    dos_colas, cola_izquierda, isPDF=False,viewChip=True,imagen='')
    grafica_cPDF1 = dc(float(eval(nC.get())), float(eval(pvar.get())),  float(eval(svar.get())),float(eval(alphaC.get())), 
                    dos_colas, cola_izquierda, isPDF=True,viewChip=False,imagen='imagenes/grafica1.png')
    grafica_cPDF2 = dc(float(eval(nC.get())), float(eval(pvar.get())),  float(eval(svar.get())),float(eval(alphaC.get())), 
                    dos_colas, cola_izquierda, isPDF=True,viewChip=True,imagen='imagenes/grafica2.png')
    fig_n = grafica_c.ejecutar()
    #declarar canvas para la grafica
    canvas = FigureCanvasTkAgg(fig_n, master = graph_frame)  # Crea el area de dibujo en Tkinter

    canvas.get_tk_widget().place(bordermode= 'inside', x= 60, y= 25, relheight= 0.9, relwidth= 0.899)
    
    pdf_btnC.configure(state = NORMAL, fg_color = color3) 


#Funciones para crear PDF
def crearpdfZ():

    global tipo_cola, cola_izquierda, dos_colas, grafica_Z, grafica_ZPDF1, grafica_ZPDF2

    grafica_ZPDF1.ejecutar()
    grafica_ZPDF2.ejecutar()
    zc1 = grafica_ZPDF1.getZc1()
    zc2 = grafica_ZPDF1.getZc2()
    zp = grafica_ZPDF1.getZp()
    pvalor = grafica_ZPDF1.getPValor()
    path = filedialog.asksaveasfilename(defaultextension=".pdf")
    if(path != ""):
        pdfZ = pdf_Z(path, dos_colas, cola_izquierda, float(eval(P.get())),float(eval(alpha.get())),
                    zc1,zc2,zp,pvalor)
        pdfZ.crearPDF()

def crearpdfP():
    global tipo_cola, cola_izquierda, dos_colas, grafica_P,grafica_PPDF1,grafica_PPDF2

    grafica_PPDF1.ejecutar()
    grafica_PPDF2.ejecutar()
    zc1 = grafica_P.getZc1()
    zc2 = grafica_P.getZc2()
    zp = grafica_P.getZp()
    pvalor = grafica_P.getPValor()
    path = filedialog.asksaveasfilename(defaultextension=".pdf")
    if(path != ""):
        pdfP = pdf_P(path, dos_colas, cola_izquierda, float(eval(P.get())),float(eval(alphaP.get())),
                    zc1,zc2,zp,pvalor)
        pdfP.crearPDF()

def crearpdfT():
    global tipo_cola, cola_izquierda, dos_colas, grafica_T,grafica_TPDF1,grafica_TPDF2

    grafica_TPDF1.ejecutar()
    grafica_TPDF2.ejecutar()
    tc1 = grafica_T.getTc1()
    tc2 = grafica_T.getTc2()
    tp = grafica_T.getTp()
    pvalor = grafica_T.getPValor()
    path = filedialog.asksaveasfilename(defaultextension=".pdf")
    if(path != ""):
        pdfT = pdf_T(path, dos_colas, cola_izquierda, float(eval(pmeanT.get())),float(eval(alphaT.get())),
                     tc1,tc2,tp,pvalor)
        pdfT.crearPDF()

def crearpdfC():
    global tipo_cola, cola_izquierda, dos_colas, grafica_c, grafica_cPDF1, grafica_cPDF2

    grafica_cPDF1.ejecutar()
    grafica_cPDF2.ejecutar()
    chic1 = grafica_c.getChic1()
    chic2 = grafica_c.getChic2()
    chip = grafica_c.getChip()
    pvalor = grafica_c.getPvalor()
    path = filedialog.asksaveasfilename(defaultextension=".pdf")
    if(path != ""):
        pdfC = pdf_C(path, dos_colas, cola_izquierda, float(eval(pvar.get())),float(eval(alphaC.get())),
                       chic1,chic2,chip,pvalor)
        pdfC.crearPDF()

#Layout Z
def set_layout_Z():
        
        global values_frame_adaptable, pdf_btn
        
        #LAYOUT para z
        if values_frame_adaptable != None:
            values_frame_adaptable.destroy()
        
        values_frame_adaptable = CTkFrame(master= raiz, fg_color=color2)
        values_frame_adaptable.grid(column = 0, row = 1, sticky = 'nsew', padx =5,pady= 5, columnspan = 2)
        
        #media poblacional
        media_poblacional_lbl = CTkLabel(master=values_frame_adaptable,
                                        text= 'Media Poblacional',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        media_poblacional_lbl.place(x = 30, y= 30)

        media_poblacional_entry = CTkEntry(master= values_frame_adaptable,
                                           textvariable= P,
                                            placeholder_text="Media poblacional",
                                            
                                            width=130,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        media_poblacional_entry.place(x=35, y= 60)

        #media muestral
        media_muestral_lbl = CTkLabel(master=values_frame_adaptable,
                                        text= 'Media muestral',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        media_muestral_lbl.place(x = 30, y= 115)

        media_muestral_entry = CTkEntry(master= values_frame_adaptable,
                                            placeholder_text="Media muestral",
                                            textvariable= smean,
                                            width=130,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        media_muestral_entry.place(x=35, y= 145)

        #tamanio de muestra 
        tamanio_lbl = CTkLabel(master=values_frame_adaptable,
                                        text= 'Tamaño de Muestra',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        tamanio_lbl.place(x = 200, y= 30)

        tamanio_entry = CTkEntry(master= values_frame_adaptable,
                                            placeholder_text="Tamaño de Muestra",
                                            textvariable= n,
                                            width=140,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        tamanio_entry.place(x=205, y= 60)

        #desviacion estandar
        desviacion_lbl = CTkLabel(master=values_frame_adaptable,
                                        text= 'Desviación Estandar',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        desviacion_lbl.place(x = 200, y= 115)

        desviacion_entry = CTkEntry(master= values_frame_adaptable,
                                            placeholder_text="Desviación Estandar",
                                            textvariable= sd,
                                            width=140,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        desviacion_entry.place(x=205, y= 145)

        #Significancia
        significancia_lbl = CTkLabel(master=values_frame_adaptable,
                                        text= 'Significancia',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        significancia_lbl.place(x = 370, y= 30)

        significancia_entry = CTkEntry(master= values_frame_adaptable,
                                            placeholder_text="Significancia",
                                            textvariable= alpha,
                                            width=120,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        significancia_entry.place(x=385, y= 60)


        graficar_btn = CTkButton(values_frame_adaptable,
                            width = 185,
                            height = 70,
                            text= "Generar grafica",
                            command= graficarZ, 
                            fg_color = color3)
        graficar_btn.place(x = 850, y= 35)

        pdf_btn = CTkButton(values_frame_adaptable,
                            width = 185,
                            height = 70,
                            state= DISABLED,
                            text= "Guardar como PDF",
                            command = crearpdfZ,
                            fg_color = color2)
        pdf_btn.place(x = 850, y= 120)
        
        left_tail_radio = CTkRadioButton(master = values_frame_adaptable, 
                                            text="Cola Izquierda",
                                            variable= tipo_cola,
                                            value=1).place(x=700 , y= 75)
        
        right_tail_radio = CTkRadioButton( values_frame_adaptable,
                                            text="Cola Derecha",
                                            variable= tipo_cola,
                                            value=2).place(x=700 , y= 105)
        
        two_tail_radio = CTkRadioButton( values_frame_adaptable,
                                            text="Dos Colas",
                                            variable= tipo_cola,
                                            value=3).place(x=700 , y= 135)
        
#Layout Proporcion
def set_layout_P():
    #layout para Proporcion
    global values_frame_adaptable, pdfP_btn
     
    if values_frame_adaptable != None:
        values_frame_adaptable.destroy()
        
    values_frame_adaptable = CTkFrame(master= raiz, fg_color=color2)
    values_frame_adaptable.grid(column = 0, row = 1, sticky = 'nsew', padx =5,pady= 5, columnspan = 2)
    
    #media poblacional
    proporcion_poblacional_lbl = CTkLabel(master=values_frame_adaptable,
                                    text= 'Proporcion Poblacional',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    proporcion_poblacional_lbl.place(x = 30, y= 30)

    proporcion_poblacional_entry = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Proporcion poblacional",
                                        textvariable= P,
                                        width=150,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    proporcion_poblacional_entry.place(x=35, y= 60)
    
    #media muestral
    proporcion_muestral_lbl = CTkLabel(master=values_frame_adaptable,
                                    text= 'Proporcion muestral',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    proporcion_muestral_lbl.place(x = 30, y= 115)

    proporcion_muestral_entry = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Proporcion muestral",
                                        textvariable= p,
                                        width=140,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    proporcion_muestral_entry.place(x=35, y= 145)
    
    #tamanio de muestra 
    tamanioP_lbl = CTkLabel(master=values_frame_adaptable,
                                    text= 'Tamaño de Muestra',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    tamanioP_lbl.place(x = 200, y= 30)

    tamanioP_entry = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Tamaño de Muestra",
                                        textvariable= nP,
                                        width=140,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    tamanioP_entry.place(x=205, y= 60)
    #Significancia
    significancia_lbl = CTkLabel(master=values_frame_adaptable,
                                    text= 'Significancia',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    significancia_lbl.place(x = 370, y= 30)
    
    significanciaP_entry = CTkEntry(master= values_frame_adaptable,
                                            placeholder_text="Significancia",
                                            textvariable= alphaP,
                                            width=120,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
    significanciaP_entry.place(x=385, y= 60)


    graficarP_btn = CTkButton(values_frame_adaptable,
                        width = 185,
                        height = 70,
                        text= "Generar grafica",
                        command= graficarP,
                        fg_color = color3)
    graficarP_btn.place(x = 850, y= 35)

    pdfP_btn = CTkButton(values_frame_adaptable,
                        width = 185,
                        height = 70,
                        text= "Guardar como PDF",
                        state= DISABLED,
                        command=crearpdfP,
                        fg_color = color2)
    pdfP_btn.place(x = 850, y= 120)
    
    left_tail_radioP = CTkRadioButton(master = values_frame_adaptable, 
                                            text="Cola Izquierda",
                                            variable= tipo_cola,
                                            value=1).place(x=700 , y= 75)
        
    right_tail_radioP = CTkRadioButton( values_frame_adaptable,
                                            text="Cola Derecha",
                                            variable= tipo_cola,
                                            value=2).place(x=700 , y= 105)
    
    two_tail_radioP = CTkRadioButton( values_frame_adaptable,
                                            text="Dos Colas",
                                            variable= tipo_cola,
                                            value=3).place(x=700 , y= 135)
    
#Layout tstudent  
def set_layout_T():
    
    global values_frame_adaptable, pdf_btnT
        
    #LAYOUT para T
    if values_frame_adaptable != None:
        values_frame_adaptable.destroy()
    
    values_frame_adaptable = CTkFrame(master= raiz, fg_color=color2)
    values_frame_adaptable.grid(column = 0, row = 1, sticky = 'nsew', padx =5,pady= 5, columnspan = 2)
    
    #media poblacional
    media_poblacional_lblT = CTkLabel(master=values_frame_adaptable,
                                    text= 'Media Poblacional',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    media_poblacional_lblT.place(x = 30, y= 30)

    media_poblacional_entryT = CTkEntry(master= values_frame_adaptable,
                                        textvariable= pmeanT,
                                        placeholder_text="Media poblacional",
                                        width=130,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    media_poblacional_entryT.place(x=35, y= 60)

    #media muestral
    media_muestral_lblT = CTkLabel(master=values_frame_adaptable,
                                    text= 'Media muestral',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    media_muestral_lblT.place(x = 30, y= 115)

    media_muestral_entryT = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Media muestral",
                                        textvariable= smeanT,
                                        width=130,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    media_muestral_entryT.place(x=35, y= 145)

    #tamanio de muestra 
    tamanio_lblT = CTkLabel(master=values_frame_adaptable,
                                    text= 'Tamaño de Muestra',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    tamanio_lblT.place(x = 200, y= 30)

    tamanio_entryT = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Tamaño de Muestra",
                                        textvariable= nT,
                                        width=140,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    tamanio_entryT.place(x=205, y= 60)

    #desviacion estandar
    desviacion_lblT = CTkLabel(master=values_frame_adaptable,
                                    text= 'Desviación Estandar',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    desviacion_lblT.place(x = 200, y= 115)

    desviacion_entryT = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Desviación Estandar",
                                        textvariable= sdT,
                                        width=140,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    desviacion_entryT.place(x=205, y= 145)

    #Significancia
    significancia_lblT = CTkLabel(master=values_frame_adaptable,
                                    text= 'Significancia',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    significancia_lblT.place(x = 370, y= 30)

    significancia_entryT = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Significancia",
                                        textvariable= alphaT,
                                        width=120,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    significancia_entryT.place(x=385, y= 60)


    graficar_btnT = CTkButton(values_frame_adaptable,
                        width = 185,
                        height = 70,
                        text= "Generar grafica",
                        command= graficarT, 
                        fg_color = color3)
    graficar_btnT.place(x = 850, y= 35)

    pdf_btnT = CTkButton(values_frame_adaptable,
                        width = 185,
                        height = 70,
                        text= "Guardar como PDF",
                        state=  DISABLED,
                        command=crearpdfT,
                        fg_color = color2)
    pdf_btnT.place(x = 850, y= 120)
    
    left_tail_radioT = CTkRadioButton(master = values_frame_adaptable, 
                                        text="Cola Izquierda",
                                        variable= tipo_cola,
                                        value=1).place(x=700 , y= 75)
    
    right_tail_radioT = CTkRadioButton( values_frame_adaptable,
                                        text="Cola Derecha",
                                        variable= tipo_cola,
                                        value=2).place(x=700 , y= 105)
    
    two_tail_radioT = CTkRadioButton( values_frame_adaptable,
                                        text="Dos Colas",
                                        variable= tipo_cola,
                                        value=3).place(x=700 , y= 135)
   
#Layout chi cuadrado    
def set_layout_C():
    
    global values_frame_adaptable,pdf_btnC
    
    #LAYOUT para z
    if values_frame_adaptable != None:
        values_frame_adaptable.destroy()
    
    values_frame_adaptable = CTkFrame(master= raiz, fg_color=color2)
    values_frame_adaptable.grid(column = 0, row = 1, sticky = 'nsew', padx =5,pady= 5, columnspan = 2)
    
    #varianza poblacional
    varianza_poblacional_lbl = CTkLabel(master=values_frame_adaptable,
                                    text= 'Varianza Poblacional',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    varianza_poblacional_lbl.place(x = 30, y= 30)

    varianza_poblacional_entry = CTkEntry(master= values_frame_adaptable,
                                        textvariable= pvar,
                                        placeholder_text="Varianza poblacional",
                                        width=130,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    varianza_poblacional_entry.place(x=35, y= 60)

    #varianza muestral
    varianza_muestral_lbl = CTkLabel(master=values_frame_adaptable,
                                    text= 'Varianza muestral',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    varianza_muestral_lbl.place(x = 30, y= 115)

    varianza_muestral_entry = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Varianza muestral",
                                        textvariable= svar,
                                        width=130,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    varianza_muestral_entry.place(x=35, y= 145)

    #tamanio de muestra 
    tamanio_lbl = CTkLabel(master=values_frame_adaptable,
                                    text= 'Tamaño de Muestra',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    tamanio_lbl.place(x = 200, y= 30)

    tamanio_entry = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Tamaño de Muestra",
                                        textvariable= nC,
                                        width=140,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    tamanio_entry.place(x=205, y= 60)

    #Significancia
    significancia_lbl = CTkLabel(master=values_frame_adaptable,
                                    text= 'Significancia',
                                    width=120,
                                    height=25,
                                    font=("comic sans", 15),
                                    fg_color=(color2),
                                    corner_radius=8)
    significancia_lbl.place(x = 370, y= 30)

    significancia_entry = CTkEntry(master= values_frame_adaptable,
                                        placeholder_text="Significancia",
                                        textvariable= alphaC,
                                        width=120,
                                        height=30,
                                        border_width=2,
                                        corner_radius=10)
    significancia_entry.place(x=385, y= 60)


    graficar_btn = CTkButton(values_frame_adaptable,
                        width = 185,
                        height = 70,
                        text= "Generar grafica",
                        command= graficarC, 
                        fg_color = color3)
    graficar_btn.place(x = 850, y= 35)

    pdf_btnC = CTkButton(values_frame_adaptable,
                        width = 185,
                        height = 70,
                        text= "Guardar como PDF",
                        state= DISABLED,
                        command=crearpdfC,
                        fg_color = color2)
    pdf_btnC.place(x = 850, y= 120)
    
    left_tail_radio = CTkRadioButton(master = values_frame_adaptable, 
                                        text="Cola Izquierda",
                                        variable= tipo_cola,
                                        value=1).place(x=700 , y= 75)
    
    right_tail_radio = CTkRadioButton( values_frame_adaptable,
                                        text="Cola Derecha",
                                        variable= tipo_cola,
                                        value=2).place(x=700 , y= 105)
    
    two_tail_radio = CTkRadioButton( values_frame_adaptable,
                                        text="Dos Colas",
                                        variable= tipo_cola,
                                        value=3).place(x=700 , y= 135)      
        
#Opciones
#funcion para normal
def dist_normal():
   
        
        
        print("distribucion normal")
        #cambiar el color de los botones
        z_btn.configure(fg_color = color1)
        p_btn.configure(fg_color = color2)
        t_btn.configure(fg_color = color2)
        chi2_btn.configure(fg_color = color2)
        
        
        global canvas
        
        if(canvas != None):
            canvas.get_tk_widget().destroy()
        
        set_layout_Z()            
             
#funcion para proporcion    
def dist_proporcion():
    
    print("distribucion proporcion")
    #reinciar colores de botones

    z_btn.configure(fg_color = color2)
    p_btn.configure(fg_color = color1)
    t_btn.configure(fg_color = color2)
    chi2_btn.configure(fg_color = color2)
    
    global canvas
        
    if(canvas != None):
        canvas.get_tk_widget().destroy()
    
    set_layout_P()
       
#funcion para t student
def dist_student():
    
    print("distribucion student")
    #reinciar colores de botones

    z_btn.configure(fg_color = color2)
    p_btn.configure(fg_color = color2)
    t_btn.configure(fg_color = color1)
    chi2_btn.configure(fg_color = color2)
    
    global canvas
        
    if(canvas != None):
        canvas.get_tk_widget().destroy()
                
    set_layout_T()
           
#funcion para chi cuadrado
def dist_chi2():
    
    print("distribucion chi2")
    #reinciar colores de botones
    z_btn.configure(fg_color = color2)
    p_btn.configure(fg_color = color2)
    t_btn.configure(fg_color = color2)
    chi2_btn.configure(fg_color = color1)
    
    global canvas
        
    if(canvas != None):
        canvas.get_tk_widget().destroy()
    
    set_layout_C()
    
    
    
        
#BOTONES DE OPTION FRAME
#Boton para un estadistico z
z_btn = CTkButton(option_frame,
                       width = 200,
                       height = 75,
                       text= "Normal  ",
                       command= dist_normal,
                       fg_color = color2,
                       corner_radius = 20)
z_btn.place(x = 25, y= 50)

#boton para un estadistico de proporcion
p_btn = CTkButton(option_frame,
                       width = 200,
                       height = 75,
                       text= "Proporción  ",
                       command= dist_proporcion,
                       fg_color = color2,
                       corner_radius = 20)
p_btn.place(x = 25, y= 125)

#boton para un estadistico de t
t_btn = CTkButton(option_frame,
                       width = 200,
                       height = 75,
                       text= "T-student  ",
                       command= dist_student,
                       fg_color = color2,
                       corner_radius = 20)
t_btn.place(x = 25, y= 200)

#boton para un estadistico chi2
chi2_btn = CTkButton(option_frame,
                       width = 200,
                       height = 75,
                       corner_radius= 20,
                       text= "Chi Cuadrado  ",
                       command= dist_chi2,
                       fg_color = color2)
chi2_btn.place(x = 25, y= 275)

     
#ejecutar ventana
raiz.mainloop()