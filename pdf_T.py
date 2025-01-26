from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class pdf_T():

    #Constructor
    def __init__(self, nombreArchivo, dosColas, colaIzquierda,
                 pmean, alpha, tc1, tc2, tp, pvalor):
        self.c = canvas.Canvas(nombreArchivo, pagesize=letter)
        self.dosColas = dosColas
        self.colaIzquierda = colaIzquierda
        self.pmean = pmean
        self.alpha = alpha
        self.tc1 = tc1
        self.tc2 = tc2
        self.tp = tp
        self.pvalor = pvalor

    #Funcion para crear pdf
    def crearPDF(self):

        w,h = letter

        def pruebaDosColas(c, pmean, alpha, tc1, tc2, tp, pvalor):
            c.drawString(50, h-50, "PRUEBA DE HIPÓTESIS")
            c.drawString(50, h-80, "1.Formulación de hipótesis.")
            c.drawString(50, h-95, '   Ho: \u03BC = {:.2f}'.format(pmean))
            c.drawString(50, h-110, '   H1: \u03BC \u2260 {:.2f}'.format(pmean))
            c.drawString(50, h-130, "2.Nivel de significancia.")
            c.drawString(50, h-145, '   \u03B1 = {:.2f}'.format(alpha))
            c.drawString(50, h-165, "3.Estadístico de prueba.")
            c.drawImage("imagenes/formulaT.png", 100, h-230, width=75, height=50)
            c.drawString(50, h-250, "4.Regla de decisión.")
            c.drawImage("imagenes/grafica1.png", 125, h-515, width=400, height=250)
            c.drawString(50, h-530, 
                         '      *Área de no rechazo: se encuentra entre el rango de valores de t [{:.2f},{:.2f}].'.format(tc1,tc2))
            c.drawString(50, h-545, 
                         '      *Área de rechazo: se encuentra fuera del rango de valores de t [{:.2f},{:.2f}].'.format(tc1,tc2))
            c.showPage()
            c.drawString(50, h-80, "5.Prueba del estadístico.")
            c.drawString(50, h-95, '     tp = {:.2f}'.format(tp))
            c.drawString(50, h-110, '     pvalor = {:.4f}'.format(pvalor))
            c.drawImage("imagenes/grafica2.png", 125, h-375, width=400, height=250)
            c.drawString(50, h-395, "6.Resultados.")
            if((tp >= tc1) & (tp <= tc2) & (pvalor > alpha)):
                c.drawString(50, h-410,'     a)No se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de "t de prueba" tp = {:.2f} se encuentra en el "área de no rechazo" dentro '.format(tp))
                c.drawString(50, h-440,'        del rango [{:.2f},{:.2f}].'.format(tc1,tc2))
                c.drawString(50, h-455, 
                             '     c)El pvalor es mayor que la significancia: pvalor = {:.4f} > \u03B1 = {:.4f}.'.format(pvalor,alpha))
            else:
                c.drawString(50, h-410,'     a)Se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de "t de prueba" tp = {:.2f} se encuentra en el "área de rechazo" fuera '.format(tp))
                c.drawString(50, h-440,'        del rango [{:.2f},{:.2f}].'.format(tc1,tc2))
                c.drawString(50, h-455, 
                             '     c)El pvalor es menor que la significancia: pvalor = {:.4f} < \u03B1 = {:.4f}.'.format(pvalor,alpha))
                
            c.drawString(50, h-470,'     d)Interprete el resultado.')

        def pruebaColaIzq(c, pmean, alpha, tc1, tp, pvalor):
            c.drawString(50, h-50, "PRUEBA DE HIPÓTESIS")
            c.drawString(50, h-80, "1.Formulación de hipótesis.")
            c.drawString(50, h-95, '   Ho: \u03BC \u2265 {:.2f}'.format(pmean))
            c.drawString(50, h-110, '   H1: \u03BC < {:.2f}'.format(pmean))
            c.drawString(50, h-130, "2.Nivel de significancia.")
            c.drawString(50, h-145, '   \u03B1 = {:.2f}'.format(alpha))
            c.drawString(50, h-165, "3.Estadístico de prueba.")
            c.drawImage("imagenes/formulaT.png", 100, h-230, width=75, height=50)
            c.drawString(50, h-250, "4.Regla de decisión.")
            c.drawImage("imagenes/grafica1.png", 125, h-515, width=400, height=250)
            c.drawString(50, h-530, 
                         '      *Área de no rechazo: se encuentra a la derecha del valor crítico tc = {:.2f}.'.format(tc1))
            c.drawString(50, h-545, 
                         '      *Área de rechazo: se encuentra a la izquierda del valor crítico tc = {:.2f}.'.format(tc1))
            c.showPage()
            c.drawString(50, h-80, "5.Prueba del estadístico.")
            c.drawString(50, h-95, '     tp = {:.2f}'.format(tp))
            c.drawString(50, h-110, '     pvalor = {:.4f}'.format(pvalor))
            c.drawImage("imagenes/grafica2.png", 125, h-375, width=400, height=250)
            c.drawString(50, h-395, "6.Resultados.")
            if((tp >= tc1) & (pvalor > alpha)):
                c.drawString(50, h-410,'     a)No se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de “t de prueba ” tp = {:.2f} se encuentra en el “área de no rechazo” a la derecha '.format(tp))
                c.drawString(50, h-440,'        de “t crítico” tc = {:.2f}.'.format(tc1))
                c.drawString(50, h-455, 
                             '     c)El pvalor es mayor que la significancia: pvalor = {:.4f} > \u03B1 = {:.4f}.'.format(pvalor,alpha))
            else:
                c.drawString(50, h-410,'     a)Se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de “t de prueba ” tp = {:.2f} se encuentra en el “área de rechazo” a la izquierda '.format(tp))
                c.drawString(50, h-440,'        de “t crítico” tc = {:.2f}.'.format(tc1))
                c.drawString(50, h-455, 
                             '     c)El pvalor es menor que la significancia: pvalor = {:.4f} < \u03B1 = {:.4f}.'.format(pvalor,alpha))
            
            c.drawString(50, h-470,'     d)Interprete el resultado.')

        def pruebaColaDer(c, pmean, alpha, tc2, tp, pvalor):
            c.drawString(50, h-50, "PRUEBA DE HIPÓTESIS")
            c.drawString(50, h-80, "1.Formulación de hipótesis.")
            c.drawString(50, h-95, '   Ho: \u03BC \u2264 {:.2f}'.format(pmean))
            c.drawString(50, h-110, '   H1: \u03BC > {:.2f}'.format(pmean))
            c.drawString(50, h-130, "2.Nivel de significancia.")
            c.drawString(50, h-145, '   \u03B1 = {:.2f}'.format(alpha))
            c.drawString(50, h-165, "3.Estadístico de prueba.")
            c.drawImage("imagenes/formulaT.png", 100, h-230, width=75, height=50)
            c.drawString(50, h-250, "4.Regla de decisión.")
            c.drawImage("imagenes/grafica1.png", 125, h-515, width=400, height=250)
            c.drawString(50, h-530, 
                         '      *Área de no rechazo: se encuentra a la izquierda del valor crítico tc = {:.2f}.'.format(tc2))
            c.drawString(50, h-545, 
                         '      *Área de rechazo: se encuentra a la derecha del valor crítico tc = {:.2f}.'.format(tc2))
            c.showPage()
            c.drawString(50, h-80, "5.Prueba del estadístico.")
            c.drawString(50, h-95, '     tp = {:.2f}'.format(tp))
            c.drawString(50, h-110, '     pvalor = {:.4f}'.format(pvalor))
            c.drawImage("imagenes/grafica2.png", 125, h-375, width=400, height=250)
            c.drawString(50, h-395, "6.Resultados.")
            if((tp <= tc2) & (pvalor > alpha)):
                c.drawString(50, h-410,'     a)No se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de “t de prueba ” tp = {:.2f} se encuentra en el “área de no rechazo” a la izquierda '.format(tp))
                c.drawString(50, h-440,'        de “t crítico” tc = {:.2f}.'.format(tc2))
                c.drawString(50, h-455, 
                             '     c)El pvalor es mayor que la significancia: pvalor = {:.4f} > \u03B1 = {:.4f}.'.format(pvalor,alpha))
            else:
                c.drawString(50, h-410,'     a)Se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de “t de prueba ” tp = {:.2f} se encuentra en el “área de rechazo” a la derecha '.format(tp))
                c.drawString(50, h-440,'        de “t crítico” tc = {:.2f}.'.format(tc2))
                c.drawString(50, h-455, 
                             '     c)El pvalor es menor que la significancia: pvalor = {:.4f} < \u03B1 = {:.4f}.'.format(pvalor,alpha))
                
            c.drawString(50, h-470,'     d)Interprete el resultado.')

        if(self.dosColas):
            pruebaDosColas(self.c, self.pmean, self.alpha, self.tc1, self.tc2, self.tp,
                           self.pvalor)
        elif(self.colaIzquierda):
            pruebaColaIzq(self.c, self.pmean, self.alpha, self.tc1, self.tp, self.pvalor)
        else:
            pruebaColaDer(self.c, self.pmean, self.alpha, self.tc2, self.tp, self.pvalor)
        self.c.showPage()
        self.c.save()