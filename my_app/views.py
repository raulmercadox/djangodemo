from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
layout= """
<h1> Sitio Web Principal </h1>
<hr>
<ul>
    <li> 
        <a href="/inicio"> Inicio </a>    
    </li>
    <li> 
        <a href="/hola"> Hola </a>    
    </li>
    <li> 
        <a href="/otros"> Otros </a>    
    </li>
    <li> 
        <a href="/contacto/carlos"> Contacto </a>    
    </li>
     <li> 
        <a href="/prueba/juan"> Prueba </a>    
    </li>
</ul>
"""
def index (request):

    html = """
      <h1>Principal</h1>
      <ul>
      """
    year=2021
    while year<=2050:
        if year%2==0:
            html+=f"<li> {str(year)}</li>"
        year+=1
    html+="</ul>"    
    return HttpResponse(layout+html)
    

def holamundo(request,redirigir=0):
    if redirigir==1:
       # return redirect('/contacto/juan')
        return redirect ('contactos',nombre='Pedro')
    html="""
        <h1>Hola Mundo</h1>
        <h3>Holas</h3>
        """

    return HttpResponse(layout+html)
                        
def otros(request):
    return HttpResponse(layout+"""
                        <h1>Hola Mundo</h1>
                        <h3>Otros</h3>
                        """)
                
def contacto(request,nombre=""):
    html=""
    if nombre:
        html+=f"""
                        <h1>Hola Contacto</h1>
                        <h3>Otros : {nombre}</h3>
                        """
      
    
    return HttpResponse(layout+f"<h2> Contacto</h2>"+html)

def prueba (request,prueba="Hola"):
    return HttpResponse (layout+f"""
                         <h1>Otra prueba </h1>
                         <h3> {prueba}  </h3>
                         """)
                        