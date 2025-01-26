import numpy as np
import matplotlib.pyplot as plt
import matplotlib.text as txt
from scipy.stats import chi2

class Dist_chi():
    
    def __init__(self,n,pvar,svar,alpha,dosColas, colaIzquierda, isPDF, viewChip, imagen):
        self.n = n
        self.pvar = pvar
        self.svar = svar
        self.alpha = alpha
        self.dosColas = dosColas
        self.colaIzquierda = colaIzquierda

        self.chic1 = 0.0
        self.chic2 = 0.0
        self.chip = 0.0
        self.pvalor = 0.0

        self.isPDF = isPDF
        self.viewChip = viewChip
        self.imagen = imagen
        
    def ejecutar(self):
        
        global n, pvar, svar, alpha, dosColas, colaIzquierda

        df = self.n - 1      # grados de libertad
        # Generar los datos de la distribucion chi-cuadrado
        x = np.linspace(0, chi2.ppf(0.999, df), 1000)
        y = chi2.pdf(x, df)

        # Crear la figura y los ejes
        
        #fig, ax = plt.subplots(1, 1, facecolor = '#605e5c')
        fig, ax = plt.subplots(1, 1)

        # Graficar la curva de distribución chi-cuadrado
        ax.plot(x, y, 'b-', alpha=0.6)


        def calcularPvalor(chip, dosColas):
            if (dosColas):
                return 2 * chi2.sf(chip, df)
            else:
                if(self.colaIzquierda):
                    return chi2.cdf(chip, df)
                else:
                    return chi2.sf(chip, df)


        def lineaVerticalChip(chip):
            # Linea vertical para el valor X2 de prueba
            ax.plot([chip, chip], [0, chi2.pdf(chip, df)], color='black',
                    label='X\u00b2p: {:.2f}'.format(chip))

            # Etiqueta con el valor X2 de prueba
            ax.annotate('X\u00b2p={:.2f}'.format(chip),
                        xy=(chip - 1.85, -0.01), fontsize=15 )


        def lineaVerticalChic(chic, nomvar):
            # Linea vertical para el valor X2 critico
            ax.plot([chic, chic], [0, chi2.pdf(chic, df)], color='black', ls='--',
                    label='{0}: {1:.2f}'.format(nomvar, chic))

            # Etiqueta con el valor X2 critico
            ax.annotate('{0}={1:.2f}'.format(nomvar, chic),
                        xy=(chic - 1.85, chi2.pdf(chic, df)),
                        color='black',
                        fontsize=15 )


        def areas(chic1, chic2):
            # marca area de rechazo
            x1 = np.linspace(0, chic1, 1000)
            x2 = np.linspace(chic2, chi2.ppf(0.999, df), 1000)
            ax.fill_between(x1, 0, chi2.pdf(x1, df), color='salmon')
            ax.fill_between(x2, 0, chi2.pdf(x2, df), color='salmon')
            ax.fill_between([0], 0, 0, color='salmon',
                            label='Área de rechazo: {:.2f}'.format(self.alpha))

            # marca area de no rechazo
            x3 = np.linspace(chic1, chic2, 1000)
            ax.fill_between(x3, 0, chi2.pdf(x3, df), color='lightgreen',
                            label='Área de no rechazo: {:.2f}'.format(1-self.alpha))


        self.chip = ((self.n-1)*self.svar)/self.pvar

        if(self.viewChip):
            lineaVerticalChip(self.chip)

        if (self.dosColas):
            self.chic1 = chi2.ppf(self.alpha/2, df)
            self.chic2 = chi2.ppf(1-self.alpha/2, df)

            lineaVerticalChic(self.chic1, 'X\u00b2c')
            lineaVerticalChic(self.chic2, 'X\u00b2c')
            areas(self.chic1, self.chic2)
            self.pvalor = calcularPvalor(self.chip, self.dosColas)
        else:
            if (self.colaIzquierda):
                self.chic1 = chi2.ppf(self.alpha, df)
                self.chic2 = chi2.ppf(0.999, df)

                lineaVerticalChic(self.chic1, 'X\u00b2c')
                areas(self.chic1, self.chic2)
                self.pvalor = calcularPvalor(self.chip, self.dosColas)
            else:
                self.chic1 = 0
                self.chic2 = chi2.ppf(1-self.alpha, df)

                lineaVerticalChic(self.chic2, 'X\u00b2c')
                areas(self.chic1, self.chic2)
                self.pvalor = calcularPvalor(self.chip, self.dosColas)

        #Agregando pvalor al legend
        ax.plot([], [], label='pvalor = {:.4f}'.format(self.pvalor),
                color='white')
        
        # etiquetas de las gráficas y ejes
        plt.title("Distribución chi cuadrado", fontsize = 15)
        plt.xlabel("Valores de chi cuadrado", fontsize = 15)
        plt.ylabel("Función de densidad", fontsize = 15)
        ax.legend(loc='upper right')

        #Borrando legend si la grafica es para PDF
        if(self.isPDF):
            plt.legend().remove()

        ax.margins(y=0.15)

        #ax.set_facecolor('#797775')

        #Creando imagen
        if(self.imagen != ''):
            fig.savefig(self.imagen, dpi = 500)
        
        #plt.show()

        return fig
            
        # Mostrar la gráfica

    def getChic1(self):
        return self.chic1

    def getChic2(self):
        return self.chic2

    def getChip(self):
        return self.chip

    def getPvalor(self):
        return self.pvalor