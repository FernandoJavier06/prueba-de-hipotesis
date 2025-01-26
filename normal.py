import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import norm

class Dist_normal():
    
    def __init__(self, n, alpha, pmean, smean, sd, P, p, dosColas,colaIzquierda,isproporcion, isPDF, viewZp, imagen):
        # variables generales para los dos tipos de problemas
        self.n = n         # tamano de la muestra
        self.alpha = alpha   # nivel de significancia

        # variables si es problema de media
        self.pmean = pmean     # media poblacional
        self.smean = smean  # media muestral
        self.sd = sd      # desviacion estandar

        # variables si es problema de proporcion
        self.P = P        # proporcion poblacional
        self.p = p      # porporcion muestral
        
        #variable de verificacoin de colas
        self.dosColas = dosColas
        self.colaIzquierda = colaIzquierda
        self.isproporcion = isproporcion 

        self.zc1 = 0.0
        self.zc2 = 0.0
        self.zp = 0.0
        self.pvalor = 0.0

        self.isPDF = isPDF
        self.viewZp = viewZp
        self.imagen = imagen

    
    def ejecutar(self):
        
        global n,alpha, pmean, smean, sd, P, p, dosColas ,colaIzquierda, isproporcion, zc1, zc2, zp, pvalor
        
        # Generar los datos para la distribución normal
        # Eje x con 4 desviaciones estandar de la media y eje y con funcion de la densidad
        x = np.linspace(-4, 4, 100)
        y = norm.pdf(x, 0, 1)

        # Crear la figura y los ejes
        #px = 1/plt.rcParams['figure.dpi'], figsize=(672*px, 420*px)
        #fig, ax = plt.subplots(1, 1 , facecolor = '#605e5c')
        fig, ax = plt.subplots(1, 1)
        
        
        # Graficar la curva de distribución normal 
        ax.plot(x, y)

        # Funcion para calcular el pvalor
        def calcularPValor(zp, dosColas):
            if (zp > 0):
                zp = -zp
            if (dosColas):
                return 2 * norm.cdf(zp, 0, 1)
            else:
                return norm.cdf(zp, 0, 1)


        # Funciones para graficar


        def lineaVerticalZp(zp):
            # Linea vertical para el valor z de prueba
            ax.plot([zp, zp], [0, norm.pdf(zp)], color='black', ls='-',
                    label='Zp: {:.2f}'.format(zp))

            # etiqueta con el valor z de prueba
            ax.annotate('Zp={:.2f}'.format(zp),
                        xy=(zp, norm.pdf(zp, 0, 1)),
                        xytext=(zp-0.45, -0.045),
                        fontsize=15)


        def lineaVerticalZc(zc, nomvar):
            # Linea vertical para el valor z critico
            ax.plot([zc, zc], [0, 0.15], color='black', ls='--',
                    label='{0}: {1:.2f}'.format(nomvar, zc))

            # etiqueta con el valor z de prueba
            ax.annotate('{0}={1:.2f}'.format(nomvar, zc),
                        xy=(zc-0.45, 0.15),
                        fontsize=15,
                        color='black')


        def areas(zc1, zc2):
            # marca area de rechazo
            x1 = np.linspace(-4, zc1, 100)
            x2 = np.linspace(zc2, 4, 100)
            ax.fill_between(x1, 0, norm.pdf(x1, 0, 1), color='salmon')
            ax.fill_between(x2, 0, norm.pdf(x2, 0, 1), color='salmon')
            ax.fill_between([0], 0, 0, color='salmon',
                            label='Área de rechazo: {:.2f}'.format(self.alpha))

            # marca area de no rechazo
            x3 = np.linspace(zc1, zc2, 100)
            ax.fill_between(x3, 0, norm.pdf(x3, 0, 1), color='lightgreen',
                            label='Área de no rechazo: {:.2f}'.format(1-self.alpha))


        # Comprobar que tipo de problema es
        if (self.isproporcion):
            # valor z de prueba para media
            self.zp = (self.p-self.P)/(np.sqrt((self.P*(1-self.P))/self.n))
        else:
            # valor z de prueba para proporcion
            self.zp = (self.smean - self.pmean)/(self.sd/np.sqrt(self.n))

        if(self.viewZp):
            lineaVerticalZp(self.zp)

        if (self.dosColas):
            self.zc1 = norm.ppf(self.alpha/2, 0, 1)
            self.zc2 = -self.zc1
            self.pvalor = calcularPValor(self.zp, self.dosColas)

            lineaVerticalZc(self.zc1, 'Zc')
            lineaVerticalZc(self.zc2, 'Zc')
            areas(self.zc1, self.zc2)
        else:
            if (self.colaIzquierda):
                self.zc1 = norm.ppf(self.alpha, 0, 1)
                self.zc2 = 4
                self.pvalor = norm.cdf(self.zp, 0, 1)

                lineaVerticalZc(self.zc1, 'Zc')
                areas(self.zc1, self.zc2)
            else:
                self.zc2 = norm.ppf((1-self.alpha), 0, 1)
                self.zc1 = -4
                self.pvalor = calcularPValor(self.zp, self.dosColas)

                lineaVerticalZc(self.zc2, 'Zc')
                areas(self.zc1, self.zc2)

        # Establecer las etiquetas de los ejes
        ax.set_xlabel('Valores de z', fontsize = 15)
        ax.set_ylabel('Densidad de probabilidad', fontsize = 15)
        # ax.set_yticks([0,0.4])
        # ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))

        #Agregando pvalor al legend
        ax.plot([], [], label='pvalor: {:.4f}'.format(self.pvalor),
                color='white')

        # Leyenda y título del gráfico
        ax.legend(loc='upper right')

        #Borrando legend si la grafica es para PDF
        if(self.isPDF):
            plt.legend().remove()

        ax.set_title('Curva de distribución normal estándar', fontsize = 15)
        ax.margins(y=0.15)


        #ax.set_facecolor('#797775')

        #Creando imagen
        if(self.imagen != ''):
            fig.savefig(self.imagen, dpi = 500)

        # Mostrar la gráfica
        #plt.show()

        return fig
    

    def getZc1(self):
        return self.zc1
    
    def getZc2(self):
        return self.zc2
    
    def getZp(self):
        return self.zp
    
    def getPValor(self):
        return self.pvalor 
    

        
        
