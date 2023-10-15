<%-- 
    Document   : areaAdministracion
    Created on : 14/10/2023, 11:26:22 a. m.
    Author     : ADMON
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib  prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AreaAdministracion</title>
    <link rel="stylesheet" href="Public/Estilos/style.css">
    <link rel="stylesheet" href="PTSansNarrow-Regular.ttf">
    <!-- <script src="../Jquery/jquery-3.6.4.min.js"></script> -->
    <!-- <script src="../bootstrap/bootstrap-5.3.0-alpha1-dist/js/bootstrap.bundle.js"></script> -->
    <!-- <link rel="stylesheet" href="../bootstrap/bootstrap-5.3.0-alpha1-dist/css/bootstrap.css"> -->


</head>

<body>
    <main>
        <div id="bordeG">
            <div id="bordeP">
                <div id="divCa">
                    <picture id="aImg">
                        <img src="Public/imgs/logoQ1.png" alt="logo" width="40px" height="40px">
                    </picture>
                    <h1 class="hA">Farmacit</h1>
                    <h2 class="hA">Area de Administracion</h2>

                </div>
                <div id="bordeCG">
                    <div id="bordeCa">
                        <div id="bordeCS">
                            <div class="divButtonA">
                                <div class="SvgA">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                                        class="bi bi-building" viewBox="0 0 16 16">
                                        <path
                                            d="M4 2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1Zm3 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1Zm3.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1ZM4 5.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1ZM7.5 5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1Zm2.5.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1ZM4.5 8a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1Zm2.5.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1Zm3.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1Z" />
                                        <path
                                            d="M2 1a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V1Zm11 0H3v14h3v-2.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5V15h3V1Z" />
                                    </svg>
                                </div>
                                <div class="buttonAb">
                                    <div class="buttonAF">
                                        <a href="controladorDireccionamiento?opcion=datosFarmacia">
                                            <h3>Farmacias</h3>
                                        </a>
                                    </div>
                                </div>

                            </div>
                            <div class="divButtonA">
                                <div class="SvgA">

                                </div>
                                <div class="buttonAb">
                                    <div class="buttonAF">
                                        <a href="#">
                                            <h3>Auditoria</h3>
                                        </a>
                                    </div>
                                </div>

                            </div>
                            <div class="divButtonA">
                                <div class="SvgA">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                                        class="bi bi-person-vcard-fill" viewBox="0 0 16 16">
                                        <path
                                            d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm9 1.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 0-1h-4a.5.5 0 0 0-.5.5ZM9 8a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 0-1h-4A.5.5 0 0 0 9 8Zm1 2.5a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 0-1h-3a.5.5 0 0 0-.5.5Zm-1 2C9 10.567 7.21 9 5 9c-2.086 0-3.8 1.398-3.984 3.181A1 1 0 0 0 2 13h6.96c.026-.163.04-.33.04-.5ZM7 6a2 2 0 1 0-4 0 2 2 0 0 0 4 0Z" />
                                    </svg>
                                </div>
                                <div class="buttonAb">
                                    <div class="buttonAF">
                                        <a href="vistaDatosPersona.php">
                                            <h3>Personas</h3>
                                        </a>
                                    </div>
                                </div>
                            </div>
                            <div class="divButtonA">
                                <div class="SvgA">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor" class="bi bi-boxes" viewBox="0 0 16 16">
                                        <path d="M7.752.066a.5.5 0 0 1 .496 0l3.75 2.143a.5.5 0 0 1 .252.434v3.995l3.498 2A.5.5 0 0 1 16 9.07v4.286a.5.5 0 0 1-.252.434l-3.75 2.143a.5.5 0 0 1-.496 0l-3.502-2-3.502 2.001a.5.5 0 0 1-.496 0l-3.75-2.143A.5.5 0 0 1 0 13.357V9.071a.5.5 0 0 1 .252-.434L3.75 6.638V2.643a.5.5 0 0 1 .252-.434L7.752.066ZM4.25 7.504 1.508 9.071l2.742 1.567 2.742-1.567L4.25 7.504ZM7.5 9.933l-2.75 1.571v3.134l2.75-1.571V9.933Zm1 3.134 2.75 1.571v-3.134L8.5 9.933v3.134Zm.508-3.996 2.742 1.567 2.742-1.567-2.742-1.567-2.742 1.567Zm2.242-2.433V3.504L8.5 5.076V8.21l2.75-1.572ZM7.5 8.21V5.076L4.75 3.504v3.134L7.5 8.21ZM5.258 2.643 8 4.21l2.742-1.567L8 1.076 5.258 2.643ZM15 9.933l-2.75 1.571v3.134L15 13.067V9.933ZM3.75 14.638v-3.134L1 9.933v3.134l2.75 1.571Z"/>
                                    </svg>
                                </div>
                                <div class="buttonAb">
                                    <div class="buttonAF">
                                        <a href="vistaDatosProducto.php">
                                            <h3>Productos</h3>
                                        </a>
                                    </div>
                                </div>
                            </div>

                        </div>

                    </div>
                </div>

            </div>

        </div>
    </main>

</body>

</html>