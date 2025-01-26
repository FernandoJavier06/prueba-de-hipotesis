from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4

class pdf_P():

    #Constructor
    def __init__(self, nombreArchivo, dosColas, colaIzquierda,
                 P, alpha, zc1, zc2, zp,pvalor):
        self.c = canvas.Canvas(nombreArchivo, pagesize=letter)
        self.dosColas = dosColas
        self.colaIzquierda = colaIzquierda
        self.P = P
        self.alpha = alpha
        self.zc1 = zc1
        self.zc2 = zc2
        self.zp = zp
        self.pvalor = pvalor

    #Funcion para crear pdf
    def crearPDF(self):

        w,h = letter

        def pruebaDosColas(c, P, alpha, zc1, zc2, zp, pvalor):
            self.c.drawString(50, h-50, "PRUEBA DE HIPÓTESIS")
            c.drawString(50, h-80, "1.Formulación de hipótesis")
            c.drawString(50, h-95, '   H0: P = {:.2f}'.format(P))
            c.drawString(50, h-110, '   H1: P \u2260 {:.2f}'.format(P))
            c.drawString(50, h-130, "2.Nivel de significancia")
            c.drawString(50, h-145, '   \u03B1 = {:.2f}'.format(alpha))
            c.drawString(50, h-165, "3.Estadístico de prueba")
            c.drawImage("imagenes/formulaZProporcion.png", 100, h-230, width=75, height=50)
            c.drawString(50, h-250, "4.Regla de decisión")
            c.drawImage("imagenes/grafica.png", 125, h-515, width=400, height=250)
            c.drawString(50, h-530, 
                         '      *Área de no rechazo: Se encuentra entre el rango de valores de z [{:.2f},{:.2f}]'.format(zc1,zc2))
            c.drawString(50, h-545, 
                         '      *Área de rechazo: Se encuentra fuera del rango de valores de z [{:.2f},{:.2f}]'.format(zc1,zc2))
            c.drawString(50, h-565, "5.Prueba del estadístico")
            c.drawString(50, h-580, '     Zp = {:.2f}'.format(zp))
            c.drawString(50, h-595, '     pvalor = {:.4f}'.format(pvalor))
            c.drawString(50, h-615, "6.Resultados")
            if((zp >= zc1) & (zp <= zc2) & (pvalor > alpha)):
                c.drawString(50, h-630, 
                             '     a)Debido a que el valor de prueba Zp = {:.2f} se encuentra dentro del rango [{:.2f},{:.2f}],'.format(zp,zc1,zc2))
                c.drawString(50, h-645, "     no se rechaza H0")
                c.drawString(50, h-660, 
                             '     b)Ya que el pvalor = {:.4f} > \u03B1 = {:.4f}, no se rechaza H0'.format(pvalor,alpha))
            else:
                c.drawString(50, h-630, 
                             '     a)Debido a que el valor de prueba Zp = {:.2f} se encuentra fuera del rango [{:.2f},{:.2f}],'.format(zp,zc1,zc2))
                c.drawString(50, h-645, "      se rechaza H0")
                c.drawString(50, h-660, 
                             '     b)Ya que el pvalor = {:.4f} < \u03B1 = {:.4f}, Se rechaza H0'.format(pvalor,alpha))

        def pruebaColaIzq(c, P, alpha, zc1, zp, pvalor):
            self.c.drawString(50, h-50, "PRUEBA DE HIPÓTESIS")
            c.drawString(50, h-80, "1.Formulación de hipótesis")
            c.drawString(50, h-95, '   H0: P \u2265 {:.2f}'.format(P))
            c.drawString(50, h-110, '   H1: P < {:.2f}'.format(P))
            c.drawString(50, h-130, "2.Nivel de significancia")
            c.drawString(50, h-145, '   \u03B1 = {:.2f}'.format(alpha))
            c.drawString(50, h-165, "3.Estadístico de prueba")
            c.drawImage("imagenes/formulaZProporcion.png", 100, h-230, width=75, height=50)
            c.drawString(50, h-250, "4.Regla de decisión")
            c.drawImage("imagenes/grafica.png", 125, h-515, width=400, height=250)
            c.drawString(50, h-530, 
                         '      *Área de no rechazo: Se encuentra a la derecha del valor crítico Zc = {:.2f}'.format(zc1))
            c.drawString(50, h-545, 
                         '      *Área de rechazo: Se encuentra a la izquierda del valor crítico Zc = {:.2f}'.format(zc1))
            c.drawString(50, h-565, "5.Prueba del estadístico")
            c.drawString(50, h-580, '     Zp = {:.2f}'.format(zp))
            c.drawString(50, h-595, '     pvalor = {:.4f}'.format(pvalor))
            c.drawString(50, h-615, "6.Resultados")
            if((zp >= zc1) & (pvalor > alpha)):
                c.drawString(50, h-630, 
                             '     a)Debido a que el valor de prueba Zp = {:.2f} \u2265 Zc = {:.2f}, no se rechaza H0'.format(zp,zc1))
                c.drawString(50, h-645, 
                             '     b)Ya que el pvalor = {:.4f} > \u03B1 = {:.4f}, no se rechaza H0'.format(pvalor,alpha))
            else:
                c.drawString(50, h-630, 
                             '     a)Debido a que el valor de prueba Zp = {:.2f} < Zc = {:.2f}, se rechaza H0'.format(zp,zc1))
                c.drawString(50, h-645, 
                             '     b)Ya que el pvalor = {:.4f} < \u03B1 = {:.4f}, se rechaza H0'.format(pvalor,alpha))

        def pruebaColaDer(c, P, alpha, zc2, zp, pvalor):
            self.c.drawString(50, h-50, "PRUEBA DE HIPÓTESIS")
            c.drawString(50, h-80, "1.Formulación de hipótesis")
            c.drawString(50, h-95, '   H0: P \u2264 {:.2f}'.format(P))
            c.drawString(50, h-110, '   H1: P > {:.2f}'.format(P))
            c.drawString(50, h-130, "2.Nivel de significancia")
            c.drawString(50, h-145, '   \u03B1 = {:.2f}'.format(alpha))
            c.drawString(50, h-165, "3.Estadístico de prueba")
            c.drawImage("imagenes/formulaZProporcion.png", 100, h-230, width=75, height=50)
            c.drawString(50, h-250, "4.Regla de decisión")
            c.drawImage("imagenes/grafica.png", 125, h-515, width=400, height=250)
            c.drawString(50, h-530, 
                         '      *Área de no rechazo: Se encuentra a la izquierda del valor crítico Zc = {:.2f}'.format(zc2))
            c.drawString(50, h-545, 
                         '      *Área de rechazo: Se encuentra a la derecha del valor crítico Zc = {:.2f}'.format(zc2))
            c.drawString(50, h-565, "5.Prueba del estadístico")
            c.drawString(50, h-580, '     Zp = {:.2f}'.format(zp))
            c.drawString(50, h-595, '     pvalor = {:.4}'.format(pvalor))
            c.drawString(50, h-615, "6.Resultados")
            if((zp <= zc2) & (pvalor > alpha)):
                c.drawString(50, h-630, 
                             '     a)Debido a que el valor de prueba Zp = {:.2f} \u2264 Zc = {:.2f}, no se rechaza H0'.format(zp,zc2))
                c.drawString(50, h-645, 
                             '     b)Ya que el pvalor = {:.4f} > \u03B1 = {:.4f}, no se rechaza H0'.format(pvalor,alpha))
            else:
                c.drawString(50, h-630, 
                             '     a)Debido a que el valor de prueba Zp = {:.2f} > Zc = {:.2f}, se rechaza H0'.format(zp,zc2))
                c.drawString(50, h-645, 
                             '     b)Ya que el pvalor = {:.4f} < \u03B1 = {:.4f}, se rechaza H0'.format(pvalor,alpha))

        if(self.dosColas):
            pruebaDosColas(self.c, self.P, self.alpha, self.zc1, self.zc2, self.zp, 
                           self.pvalor)
        elif(self.colaIzquierda):
            pruebaColaIzq(self.c, self.P, self.alpha, self.zc1, self.zp, self.pvalor)
        else:
            pruebaColaDer(self.c, self.P, self.alpha, self.zc2, self.zp, self.pvalor)
        self.c.showPage()
        self.c.save()


