<%-- 
    Document   : Registro
    Created on : 14/09/2023, 6:39:53 p. m.
    Author     : ADMON
--%>
<%@taglib  prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro</title>
    <link rel="stylesheet" href="Public/Estilos/style.css">


</head>
<!--cambiar la clase del button registrar ya que al cambiarle las propiedades cambio todo copiar el de visual y crear una nueva .-->
<body>
    <main>
        <div id="divContainer">
            <div id="divFormulario">

            <!--  action="../controlador/controladorInicioSession.php"   PONER LA VISTA DE REGISTRO EXIOSO YA PUEDE INICIAR SESION  -->
            <form  class = "formulario" action="controladorSesion"  method="post" onclick="cambiarColor();">

                    <div id="tituloForm">
                        <div id="iconoForm">
                            <!--aca me botada el error de desabilitar la imagen-->
                            <img src="Public/imgs/logoQ1.png" alt="logo" width="70px" height="70px" />

                        </div>
                        <div>
                            <h1>Farmacit</h1>
                        </div>
                    </div>
                    <div class="areainputsG">

                        <div id="plbIngresar">
                            <h2>Ingresa a tu cuenta</h2>
                        </div>
                        <%
                        if (request.getParameter("msj") != null) {
                            String mensaje = request.getParameter("msj");
                        %>
                            <h5 style="font-size: 18px; color: red;" id="datosInvalidos"  role="alert">el mensaje con innerHtml esta en proceso </h5>
                            
                        <%
                        }
                        %>




                      
                       


                        <div class="areaInputForm">
                            <input type="text" placeholder="Email o Numero de identificacion"  class="inputsForm" name="emailDocumento" id="DocumentoCorreo" onchange="RemplazarValor();" required>
                        </div>
                        <div class="areaInputForm">
                            <input type="password" placeholder="Contraseña" class="inputsForm" name="contrasena" id="contrasena" required>
                        </div>
                        <div class="olvidarContrasena">
                            <h3><a href="">¿Olvido la contraseña?</a></h3>
                        </div>
                        <!--en este div cambie la clase--> 
                        <div class="divButtonIngresar">
                            <button class="buttonIngresarF" style="font-family: inherit; font-size: 18px;" type="submit"  name="btnIngresar" value="iniciarSession" onclick=" return verificarCampos() && mostrarMensaje();"  > 
                            <!--onclick="/*location.href='index.php*/'"-->
                            <h3>Ingresar</h3>
                            </button>

                        </div>
                        <div id="divCrearC">
                            <p>¿No tienes una cuenta?<a href="controladorDireccionamiento?opcion=crearCuenta" class="linkCuenta"><h4>Crear una cuenta</h4></a></p>
                           
                        </div>
                        

                    </div>
                </form>

            </div>
           


        </div>

    </main>
                        
          <%
            if (request.getParameter("mensaje") != null) {
                String mensajeC = request.getParameter("mensaje");
            %>
            <script>
               // Declaración de contar en un alcance más amplio, fuera de cualquier función
                                let contar = true;

                    function mostrarAlertaUnaVez() {
                        if (contar) {
                            window.alert("<%= mensajeC %>");
                            contar = false;
                            return true;
                        }
                        return false;
                    }

                    // Llamar a la función mostrarAlertaUnaVez en algún lugar de tu código cuando sea apropiado
                    if (mostrarAlertaUnaVez()) {
                        // La alerta se mostrará la primera vez que se ejecute esta condición
                    }
              


                    
                    
                   
               
            </script>

            <%
            }
            %>
    
</body>

    <script>
        
        
        
        
        
        
        
        
            function verificarCampos(){
                
                !(function(window, document) {//Esta es una función IIFE que toma window y document como argumentos, que son objetos globales. y se utliza para encapsular las variables

                    // Obtener los valores de correo y contraseña
                    let correo = document.getElementById("DocumentoCorreo").value;
                    let contrasena = document.getElementById("contrasena").value;

                    // Verificar si los campos están vacíos
                    if (correo.trim() === "" || contrasena.trim() === "") {
                        // Mostrar un mensaje de alerta
                        window.alert("Rellene todos los campos");
                      return false; // Detiene el envío del formulario/
                    }
                
                })(window, document);
             }
             
             
             function cambiarColor(){

                //nombre

                    const colorOriginal = "rgb(118, 118, 118)";
                    let inputCorreo = document.querySelector("#DocumentoCorreo");


                    inputCorreo.addEventListener("input", function(event) {
                       inputCorreo.style.borderBottomColor = "black";
                    });

//                    Agrega un evento de blur al input
                    inputCorreo.addEventListener("blur", function() {
//                    Cambia el color del input al original  
                      inputCorreo.style.borderBottomColor = colorOriginal;  
                                                                        
                   });
                   

                    let inputContrasena = document.querySelector("#contrasena");

                    inputContrasena.addEventListener("input", function(event) {
                       inputContrasena.style.borderBottomColor = "black";
                    });

//                    Agrega un evento de blur al input
                    inputContrasena.addEventListener("blur", function() {
//                     Cambia el color del input al original  
                      inputContrasena.style.borderBottomColor = colorOriginal;                                               
                   });
 
              }
             
             function RemplazarValor(){
                   
           // escuchar el evento del input de correo o nombre y quitarle y remplazar al momento que cambie el valor al h5
                let hMensaje = document.getElementById("datosInvalidos");
                let inputCorreo = document.getElementById("DocumentoCorreo");
                
                  
                                
                 
                 
             }
             
//             function cambiarColorMensaje(){
//                 
//                 let hMensaje = document.getElementById("datosInvalidos");
//                
//            }
//            
//             function mostrarMensaje(){
//                 
//                setTimeout(function() {
//                    window.location.href = "otra_pagina.html";
//                }, 3000); // 3000 milisegundos (3 segundos)
//
//
//                 
//                 
//                 
//             }

   

             
             
             
             
    
    
    
    function verificarCredenciales(){// function en desuso porque hay un eror de direcconamiento , nose porque no me direcciona 
          // Crear una instancia de XMLHttpRequest para realizar la solicitud AJAX
                let xhr = new XMLHttpRequest();

                // Configurar el manejo de la respuesta
                xhr.onreadystatechange = function () {
                    
                    if (xhr.readyState === 4 && xhr.status === 200) {
                        // Obtener la respuesta del servidor
                        let respuesta = xhr.responseText;

                        // Manejar la respuesta según su valor
                        console.log("La respuesta es: " + respuesta);

                        if (respuesta === "true") {
                            document.getElementById("datosInvalidos").innerHTML = "";
                            return true;// Permitir el envío del formulario
                        } else if (respuesta === "false") {
                            document.getElementById("datosInvalidos").innerHTML = "Datos Invalidos";
                            return false; // Detiene el envío del formulario
                        } else {
                            document.getElementById("datosInvalidos").innerHTML = "Error en la consulta.";
//                            return false; // Detiene el envío del formulario
                        }
                    }
                };

                // Configurar la solicitud AJAX
                xhr.open("POST", "controladorSesion", true);
                xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

                // Enviar los datos al servidor
                xhr.send("emailDocumento=" + correo + "&contrasena=" + contrasena);

                // Mostrar los datos en la consola (para depuración)
                console.log("Los datos son: ");
                console.log("Correo: " + correo);
                console.log("Contraseña: " + contrasena);

//              Detener el envío del formulario de forma predeterminada
//              return false;
        
         
    }
        

        



    </script>
</html>
