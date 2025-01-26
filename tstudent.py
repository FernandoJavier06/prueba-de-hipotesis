import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator 
from scipy.stats import t

class Dist_student():
    def __init__(self,n,loc,scale,alpha,muestra, twocolas, colaleft, isPDF, viewtp, imagen):
        self.n = n
        self.loc = loc
        self.scale = scale
        self.alpha = alpha
        self.muestra = muestra
        self.twocolas = twocolas
        self.colaleft = colaleft
        
        self.tc1 = 0.0
        self.tc2 = 0.0
        self.tp = 0.0
        self.pvalor = 0.0

        self.isPDF = isPDF
        self.viewtp = viewtp
        self.imagen = imagen
        
    def ejecutar(self):
        
        global n, loc, scale, alpha, muestra, twocolas, colaleft

        df = self.n - 1
        self.tp = (self.muestra - self.loc)*np.sqrt(self.n)/self.scale

        #Definiendo el marco para la gráfica
        
        #fig, ax = plt.subplots(1,1, facecolor = '#605e5c')
        fig, ax = plt.subplots(1,1)

        def calcularPValor(tp, dosColas, df):
            if(tp > 0):
                tp = -tp
            if(dosColas):
                return 2 * t.cdf(tp,df)
            else:
                return t.cdf(tp,df)


        #Agregando los valores de x para la gráfica t-Student
        def DomRang(GradosLibertad):
            x = np.linspace(t.ppf(0.001, GradosLibertad), t.ppf(0.999, GradosLibertad), 1000)
            ax.plot(x, t.pdf(x, GradosLibertad))

        #Area de rechazo en la gráfica
        def AreaRechazo(Tcritico, GradosLibertad):
            x1 = np.linspace(t.ppf(0.001, GradosLibertad), Tcritico, 1000)
            x2 = np.linspace(self.tc2, t.ppf(0.999, df), 1000)
            if (self.twocolas):
                ax.fill_between(x1, 0, t.pdf(x1,GradosLibertad), color='salmon', label='Área de rechazo: ({:.2f})'.format(self.alpha))
                ax.fill_between(x2, 0, t.pdf(x2,GradosLibertad), color='salmon')
            else:
                if(self.colaleft):
                    ax.fill_between(x1, 0, t.pdf(x1,GradosLibertad), color='salmon', label='Área de rechazo: ({:.2f})'.format(self.alpha))
                else:
                    ax.fill_between(x2, 0, t.pdf(x2,GradosLibertad), color='salmon', label='Área de rechazo: ({:.2f})'.format(self.alpha))

        #Area de no rechazo en la gráfica
        def AreaNoRechazo(Tcritico1, Tcritico2, GradosLibertad):
            x3= np.linspace(Tcritico1, Tcritico2, 1000)
            ax.fill_between(x3, 0, t.pdf(x3, GradosLibertad), color='lightgreen', label='Área de no rechazo: ({:.2f})'.format(1-self.alpha))

        #Agregando líneas de separación
        def LineaSeparadora (Tcritico1, Tcritico2, GradosLibertad=df):
            ax.plot([Tcritico1,Tcritico1],[0, 0.15], color='black', linestyle='--', label='tc: {:.2f}'.format(Tcritico1))
            ax.annotate('tc= {:.2f}'.format(Tcritico1), xy=(Tcritico1, t.pdf(Tcritico1,GradosLibertad)), xytext=(Tcritico1-0.3, 0.15),fontsize=15, color='black')
            if(Tcritico2 != 0):
                ax.plot([Tcritico2,Tcritico2],[0, 0.15], color='black', linestyle='--',label='tc: {:.2f}'.format(Tcritico2))
                ax.annotate('tc= {:.2f}'.format(Tcritico2), xy=(Tcritico2, t.pdf(Tcritico2,GradosLibertad)), xytext=(Tcritico2-0.3, 0.15),fontsize=15, color='black')

        #Agregando tpueba
        def Tprueba(Tprueba, GradosLibertad=df):
            ax.plot([Tprueba, Tprueba],[0, t.pdf(Tprueba, GradosLibertad)], color="black", label='tp: {:.2f}'.format(Tprueba))
            ax.annotate('tp= {:.2f}'.format(Tprueba), xy=(Tprueba, t.pdf(Tprueba,GradosLibertad)), xytext=(Tprueba-0.3, -0.04),fontsize=15, color='black')


        if(self.viewtp):
            Tprueba(self.tp)

        #Condiciones para que se ejecute de dos colas, una cola (izquierda o derecha)
        if (self.twocolas):
            self.tc1 = t.ppf(self.alpha/2, df) 
            self.tc2 = -self.tc1
            self.pvalor = calcularPValor(self.tp, self.twocolas,df)
            
            #Tprueba(self.tp)
            LineaSeparadora(self.tc1,self.tc2)
            DomRang(df)
            AreaRechazo(self.tc1, df)
            AreaNoRechazo(self.tc1,self.tc2,df)
        else: 
            if(self.colaleft):
                self.tc1 = t.ppf(self.alpha, df)
                self.tc2 = t.ppf(0.999,df)
                self.pvalor = calcularPValor(self.tp, self.twocolas,df)

                #Tprueba(self.tp)
                LineaSeparadora(self.tc1,0)
                DomRang(df)
                AreaRechazo(self.tc1, df)
                AreaNoRechazo(self.tc1, self.tc2, df)
            else:
                self.tc2 = t.ppf(1-self.alpha, df)
                self.tc1 = t.ppf(0.001, df)
                self.pvalor = calcularPValor(self.tp, self.twocolas,df)

                #Tprueba(self.tp)
                LineaSeparadora(self.tc2,0)
                DomRang(df)
                AreaRechazo(self.tc2, df)
                AreaNoRechazo(self.tc1, self.tc2, df)
                

        #Agregando pvalor al legend
        ax.plot([], [], label='pvalor: {:.4f}'.format(self.pvalor),
                color='white')
        
        
        #Agregando la títulos al marco
        ax.legend(loc='upper right')

        #Borrando legend si la grafica es para PDF
        if(self.isPDF):
            plt.legend().remove()

        #Etiquetas a la gráfica y ejes
        plt.title('Distribución t de student', fontsize = 15)
        plt.xlabel('Valores de t', fontsize = 15)
        plt.ylabel('Densidad de probabilidad', fontsize = 15)
        ax.margins(y=0.15)

        #ax.set_facecolor('#797775')

        #Creando imagen
        if(self.imagen != ''):
            fig.savefig(self.imagen, dpi = 500)

        #Mostrando la gráfica
        #plt.show()

        return fig 
        
    
    def getTc1(self):
        return self.tc1
    
    def getTc2(self):
        return self.tc2
    
    def getTp(self):
        return self.tp
    
    def getPValor(self):
        return self.pvalor
    
    