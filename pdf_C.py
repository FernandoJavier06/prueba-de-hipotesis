from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class pdf_C():
    #Constructor
    def __init__(self, nombreArchivo, dosColas, colaIzquierda,
                 pvar, alpha, chic1, chic2, chip, pvalor):
        self.c = canvas.Canvas(nombreArchivo, pagesize=letter)
        self.dosColas = dosColas
        self.colaIzquierda = colaIzquierda
        self.pvar = pvar
        self.alpha = alpha
        self.chic1 = chic1
        self.chic2 = chic2
        self.chip = chip
        self.pvalor = pvalor

    #Funcion para crear pdf
    def crearPDF(self):

        w, h = letter

        def pruebaDosColas(c, pvar, alpha, chic1, chic2, chip, pvalor):
            c.drawString(50, h-50, "PRUEBA DE HIPÓTESIS")
            c.drawString(50, h-80, "1.Formulación de hipótesis.")
            c.drawString(50, h-95, '   Ho: \u03C3² = {:.2f}'.format(pvar))
            c.drawString(50, h-110, '   H1: \u03C3² \u2260 {:.2f}'.format(pvar))
            c.drawString(50, h-130, "2.Nivel de significancia.")
            c.drawString(50, h-145, '   \u03B1 = {:.2f}'.format(alpha))
            c.drawString(50, h-165, "3.Estadístico de prueba.")
            c.drawImage("imagenes/formulaC.png", 100, h-230, width=125, height=50)
            c.drawString(50, h-250, "4.Regla de decisión.")
            c.drawImage("imagenes/grafica1.png", 125, h-515, width=400, height=250)
            c.drawString(50, h-530, 
                         '      *Área de no rechazo: se encuentra entre el rango de valores de X² [{:.2f},{:.2f}].'.format(chic1,chic2))
            c.drawString(50, h-545, 
                         '      *Área de rechazo: se encuentra fuera del rango de valores de X² [{:.2f},{:.2f}].'.format(chic1,chic2))
            c.showPage()
            c.drawString(50, h-80, "5.Prueba del estadístico.")
            c.drawString(50, h-95, '     X²p = {:.2f}'.format(chip))
            c.drawString(50, h-110, '     pvalor = {:.4f}'.format(pvalor))
            c.drawImage("imagenes/grafica2.png", 125, h-375, width=400, height=250)
            c.drawString(50, h-395, "6.Resultados.")
            if((chip >= chic1) & (chip <= chic2) & (pvalor > alpha)):
                c.drawString(50, h-410,'     a)No se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de "X² de prueba" X²p = {:.2f} se encuentra en el "área de no rechazo" dentro '.format(chip))
                c.drawString(50, h-440,'        del rango [{:.2f},{:.2f}].'.format(chic1,chic2))
                c.drawString(50, h-455, 
                             '     c)El pvalor es mayor que la significancia: pvalor = {:.4f} > \u03B1 = {:.4f}.'.format(pvalor,alpha))
            else:
                c.drawString(50, h-410,'     a)Se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de "X² de prueba" X²p = {:.2f} se encuentra en el "área de rechazo" fuera '.format(chip))
                c.drawString(50, h-440,'        del rango [{:.2f},{:.2f}].'.format(chic1,chic2))
                c.drawString(50, h-455, 
                             '     c)El pvalor es menor que la significancia: pvalor = {:.4f} < \u03B1 = {:.4f}.'.format(pvalor,alpha))
            
            c.drawString(50, h-470,'     d)Interprete el resultado.')
        
        def pruebaColaIzq(c, pvar, alpha, chic1, chip, pvalor):
            c.drawString(50, h-50, "PRUEBA DE HIPÓTESIS")
            c.drawString(50, h-80, "1.Formulación de hipótesis.")
            c.drawString(50, h-95, '   Ho: \u03C3² \u2265 {:.2f}'.format(pvar))
            c.drawString(50, h-110, '   H1: \u03C3² < {:.2f}'.format(pvar))
            c.drawString(50, h-130, "2.Nivel de significancia.")
            c.drawString(50, h-145, '   \u03B1 = {:.2f}'.format(alpha))
            c.drawString(50, h-165, "3.Estadístico de prueba.")
            c.drawImage("imagenes/formulaC.png", 100, h-230, width=125, height=50)
            c.drawString(50, h-250, "4.Regla de decisión.")
            c.drawImage("imagenes/grafica1.png", 125, h-515, width=400, height=250)
            c.drawString(50, h-530, 
                         '      *Área de no rechazo: se encuentra a la derecha del valor crítico X²c = {:.2f}.'.format(chic1))
            c.drawString(50, h-545, 
                         '      *Área de rechazo: se encuentra a la izquierda del valor crítico X²c = {:.2f}.'.format(chic1))
            c.showPage()
            c.drawString(50, h-80, "5.Prueba del estadístico.")
            c.drawString(50, h-95, '     X²p = {:.2f}'.format(chip))
            c.drawString(50, h-110, '     pvalor = {:.4f}'.format(pvalor))
            c.drawImage("imagenes/grafica2.png", 125, h-375, width=400, height=250)
            c.drawString(50, h-395, "6.Resultados.")
            if((chip >= chic1) & (pvalor > alpha)):
                c.drawString(50, h-410,'     a)No se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de “X² de prueba ” X²p = {:.2f} se encuentra en el “área de no rechazo” a la derecha '.format(chip))
                c.drawString(50, h-440,'        de “X² crítico” X²c = {:.2f}.'.format(chic1))
                c.drawString(50, h-455, 
                             '     c)El pvalor es mayor que la significancia: pvalor = {:.4f} > \u03B1 = {:.4f}.'.format(pvalor,alpha))
            else:
                c.drawString(50, h-410,'     a)Se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de “X² de prueba ” X²p = {:.2f} se encuentra en el “área de rechazo” a la izquierda '.format(chip))
                c.drawString(50, h-440,'        de “X² crítico” X²c = {:.2f}.'.format(chic1))
                c.drawString(50, h-455, 
                             '     c)El pvalor es menor que la significancia: pvalor = {:.4f} < \u03B1 = {:.4f}.'.format(pvalor,alpha))
                
            c.drawString(50, h-470,'     d)Interprete el resultado.')

        def pruebaColaDer(c, pvar, alpha, chic2, chip, pvalor):
            c.drawString(50, h-50, "PRUEBA DE HIPÓTESIS")
            c.drawString(50, h-80, "1.Formulación de hipótesis.")
            c.drawString(50, h-95, '   Ho: \u03C3² \u2264 {:.2f}'.format(pvar))
            c.drawString(50, h-110, '   H1: \u03C3² > {:.2f}'.format(pvar))
            c.drawString(50, h-130, "2.Nivel de significancia.")
            c.drawString(50, h-145, '   \u03B1 = {:.2f}'.format(alpha))
            c.drawString(50, h-165, "3.Estadístico de prueba.")
            c.drawImage("imagenes/formulaC.png", 100, h-230, width=125, height=50)
            c.drawString(50, h-250, "4.Regla de decisión.")
            c.drawImage("imagenes/grafica1.png", 125, h-515, width=400, height=250)
            c.drawString(50, h-530, 
                         '      *Área de no rechazo: se encuentra a la izquierda del valor crítico X²c = {:.2f}.'.format(chic2))
            c.drawString(50, h-545, 
                         '      *Área de rechazo: se encuentra a la derecha del valor crítico X²c = {:.2f}.'.format(chic2))
            c.showPage()
            c.drawString(50, h-80, "5.Prueba del estadístico.")
            c.drawString(50, h-95, '     X²p = {:.2f}'.format(chip))
            c.drawString(50, h-110, '     pvalor = {:.4f}'.format(pvalor))
            c.drawImage("imagenes/grafica2.png", 125, h-375, width=400, height=250)
            c.drawString(50, h-395, "6.Resultados.")
            if((chip <= chic2) & (pvalor > alpha)):
                c.drawString(50, h-410,'     a)No se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de “X² de prueba ” X²p = {:.2f} se encuentra en el “área de no rechazo” a la izquierda '.format(chip))
                c.drawString(50, h-440,'        de “X² crítico” X²c = {:.2f}.'.format(chic2))
                c.drawString(50, h-455, 
                             '     c)El pvalor es mayor que la significancia: pvalor = {:.4f} > \u03B1 = {:.4f}.'.format(pvalor,alpha))
            else:
                c.drawString(50, h-410,'     a)Se rechaza Ho.')
                c.drawString(50, h-425, 
                             '     b)El valor de “X² de prueba ” X²p = {:.2f} se encuentra en el “área de rechazo” a la derecha '.format(chip))
                c.drawString(50, h-440,'        de “X² crítico” X²c = {:.2f}.'.format(chic2))
                c.drawString(50, h-455, 
                             '     c)El pvalor es menor que la significancia: pvalor = {:.4f} < \u03B1 = {:.4f}.'.format(pvalor,alpha))
                
            c.drawString(50, h-470,'     d)Interprete el resultado.')
        
        if(self.dosColas):
            pruebaDosColas(self.c, self.pvar, self.alpha, self.chic1, self.chic2, self.chip
                           ,self.pvalor)
        elif(self.colaIzquierda):
            pruebaColaIzq(self.c, self.pvar, self.alpha, self.chic1, self.chip,self.pvalor)
        else:
            pruebaColaDer(self.c, self.pvar, self.alpha, self.chic2, self.chip,self.pvalor)

        self.c.showPage()
        self.c.save()
