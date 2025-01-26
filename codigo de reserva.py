#tamaño de la raiz
raiz.geometry(f'1080x720+{w_pantalla}+{h_pantalla}')


#No redimensionar
raiz.resizable(0,0)

#CREACION DE FRAMES

#FRAME 1

frame1 = tk.Frame(raiz)
frame1.pack()

#SUB FRAME DE VALORES
values_frame = tk.Frame(frame1)
values_frame.config(bg="red",width="360", height= "540")
values_frame.pack(side="left", anchor= "n") #empacar el frame en la raiz


#SUB FRAME DE GRsAFICA
graph_frame = tk.Frame(frame1)
graph_frame.config(bg="blue",width="720", height= "540")
graph_frame.pack(side="right", anchor= "n") #empacar el frame en la raiz


#FRAME 2 

frame2 = tk.Frame(raiz)
frame2.pack()

#Sub frame de opciones
options_frame = tk.Frame(frame2)
options_frame.config(bg="green",width="1080", height= "180")
options_frame.pack(side="bottom", anchor= "w") #empacar el frame en la raiz

# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren/
#Tkinter y Matplotlib

from tkinter import Tk, Frame,Button,Label, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(dpi=90, figsize=(7,5),facecolor='#00faafb7')
plt.title("Grafica en Tkinter con Matplotlib",color='red',size=16, family="Arial")

plt.xlim(-4, 14)
plt.ylim(-8, 8)
ax.set_facecolor('black')

ax.axhline(linewidth=2, color='r')
ax.axvline(linewidth=2, color='r')

ax.set_xlabel("Eje  Horizontal", color='black')
ax.set_ylabel("Eje  Vertical", color='black')
ax.tick_params(direction='out', length=6, width=2, 
	colors='black',
    grid_color='r', grid_alpha=0.5)

def graficar_datos():
	nivel = scale.get()
	x = np.arange(-np.pi, 4*np.pi, 0.01) 	
	line, = ax.plot(x, nivel*np.sin(x), 
		color ='b', linestyle='solid')
	canvas.draw()
	label.config(text= nivel)
	line.set_ydata(np.sin(x)+10)
	ventana.after(100, graficar_datos)

ventana = Tk()
ventana.geometry('642x498')
ventana.wm_title('Grafica Matplotlib con Scale')
ventana.minsize(width=642,height=495)

frame = Frame(ventana,  bg='gray22',bd=3)
frame.grid(column=0,row=0)

canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
canvas.get_tk_widget().grid(column=0, row=0, columnspan=3, padx=5, pady =5)

Button(frame, text='Grafica Datos', width = 15, bg='magenta',fg='white', command= graficar_datos).grid(column=0, row=1, pady =5)
label = Label(frame, width = 15)
label.grid(column=1, row=1, pady =5)

scale = ttk.Scale(frame, to = 6, from_ =0, orient='horizontal', length=300)
scale.grid(column=2, row=1)

style = ttk.Style()
style.configure("Horizontal.TScale", background= 'gray22')  
ventana.mainloop()



estadisticoZ = val_frame(raiz)
        values_frame = estadisticoZ.set_layout()







 right_tail_radio = customtkinter.CTkRadioButton(values_frame_adaptable, 
                                                       text="Cola Derecha",
                                                       variable= radio_var,
                                                       value=2)
        right_tail_radio.pack(padx = 650, pady= 140)
        
        two_tail_radio = customtkinter.CTkRadioButton(values_frame_adaptable, 
                                                       text="Dos Colas",
                                                       variable= radio_var,
                                                       value=3)
        two_tail_radio.pack(padx = 650, pady= 170)
        
        


        pvar = 5        # varianza poblacional
        svar = 7.91     # varianza muestral
        n = 14          # tamano de la muestra
        
        alpha = 0.10    # nivel de significancia

        dosColas = False
        colaIzquierda = False


from customtkinter import*
from tkinter import*

#colores
color1= "#1b1a19"
color2= "#323130"
color3= "#797775"
color4 = "#c8c6c4"

class val_frame:
    
    frame1 = None
        
    def set_layout(estadistico):
        
        global frame1
        frame1 = CTkFrame(master = estadistico, fg_color='#323130')
        frame1.grid(column = 0, row = 1, sticky = 'nsew', padx =5,pady= 5, columnspan = 2)
        
        #LAYOUT para z
        
        #media poblacional
        media_poblacional_lbl = CTkLabel(master=frame1,
                                        text= 'Media Poblacional',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        media_poblacional_lbl.place(x = 30, y= 30)

        media_poblacional_entry = CTkEntry(master= frame1,
                                            placeholder_text="Media poblacional",
                                            width=130,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        media_poblacional_entry.place(x=35, y= 60)

        #media muestral
        media_muestral_lbl = CTkLabel(master=frame1,
                                        text= 'Media muestral',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        media_muestral_lbl.place(x = 30, y= 115)

        media_muestral_entry = CTkEntry(master= frame1,
                                            placeholder_text="Media muestral",
                                            width=130,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        media_muestral_entry.place(x=35, y= 145)

        #tamanio de muestra 
        tamanio_lbl = CTkLabel(master=frame1,
                                        text= 'Tamaño de Muestra',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        tamanio_lbl.place(x = 200, y= 30)

        tamanio_entry = CTkEntry(master= frame1,
                                            placeholder_text="Tamaño de Muestra",
                                            width=140,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        tamanio_entry.place(x=205, y= 60)

        #desviacion estandar
        desviacion_lbl = CTkLabel(master=frame1,
                                        text= 'Desviación Estandar',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        desviacion_lbl.place(x = 200, y= 115)

        desviacion_entry = CTkEntry(master= frame1,
                                            placeholder_text="Desviación Estandar",
                                            width=140,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        desviacion_entry.place(x=205, y= 145)

        #Significancia
        significancia_lbl = CTkLabel(master=frame1,
                                        text= 'Significancia',
                                        width=120,
                                        height=25,
                                        font=("comic sans", 15),
                                        fg_color=(color2),
                                        corner_radius=8)
        significancia_lbl.place(x = 370, y= 30)

        significancia_entry = CTkEntry(master= frame1,
                                            placeholder_text="Significancia",
                                            width=120,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        significancia_entry.place(x=385, y= 60)

        limpiar_btn = CTkButton(frame1,
                            width = 100,
                            height = 75,
                            text= "Limpiar campos",
                            #falta command
                            fg_color = color3)
        limpiar_btn.place(x = 725, y= 60)

        graficar_btn = CTkButton(frame1,
                            width = 185,
                            height = 70,
                            text= "Generar grafica",
                            #falta command
                            fg_color = color3)
        graficar_btn.place(x = 850, y= 25)

        pdf_btn = CTkButton(frame1,
                            width = 185,
                            height = 70,
                            text= "Guardar como PDF",
                            #falta command
                            fg_color = color3)
        pdf_btn.place(x = 850, y= 110)
        
        return frame1
        
        
        #LAYOUT para z
        print("estadistico z")
        

        
        