<?php



//otro api

  //datos a enviar
  $data = array("id" => "1212");
  //url contra la que atacamos
  $ch2 = curl_init("http://10.90.29.159:5000/get_myKey");
  //a true, obtendremos una respuesta de la url, en otro caso, 
  //true si es correcto, false si no lo es
  curl_setopt($ch2, CURLOPT_RETURNTRANSFER, true);
  //establecemos el verbo http que queremos utilizar para la petición
  curl_setopt($ch2, CURLOPT_CUSTOMREQUEST, "PUT");
  //enviamos el array data
  curl_setopt($ch2, CURLOPT_POSTFIELDS,http_build_query($data));
  //obtenemos la respuesta
  $response = curl_exec($ch2);
  // Se cierra el recurso CURL y se liberan los recursos del sistema
  curl_close($ch2);


// fin api


$url = 'http://10.90.29.163:5000/prueba2';

// //create a new cURL resource
$ch = curl_init($url);

//setup request to send json via POST




    $datos= array(
        'clave' => '123456789',
        'codigoactividad' => '01',
        'numeroconsecutivo' => '1',
        'fechaemision' => date("Y-m-d"),
        'emisor' => array(
            'nombre' => utf8_decode('advicesolutions'),
            'id' => array(
                'tipoid' => '01',
                'numeroid' => '1'
            ),
            'ubicacion' => array(
                'direccion' => utf8_decode('Miramar, Puntarenas')
            ),
            'telefono' => array(
                'codigop' => '506',
                'numero' => '8888-8888'
            ),
            'email' => 'advicesolutions@gmail.com'
        ),
        'receptor' => array(
            'nombre' => ''.$tuple["first_name"].' '.$tuple["last_name"].'',
            'id' => array(
                'tipoid' => '02',
                'numeroid' => '2'
            ),
            'ubicacion' => array(
                'direccion' => utf8_decode('Barranca, Puntarenas')
            ),
            'telefono' => array(
                'codigop' => '506',
                'numero' => ''.$tuple["phone"].''
            ),
            'email' => ''.$tuple["email"].''
        ),
        'detalleservicio' => array(
            'lineadetalle' => 
                array(),  
            
        ),
        'resumenfactura' => array(
            'codtipomoneda' => array(
                'codmoneda' => 'CRC'
            ),
            'totalventa' => ''.$subtotal.'',
            'descuentos' => '0',
            'totalventaneta' => ''.$subtotal.'',
            'totalimpuesto' => ''.$impuesto.'',
            'total' => ''.$totalfinal.''
        ),
        'firmadigital' => array(
            'firma' => 'aqui va la firma digital'
        )
    );

    for($i=0; $i< count($_SESSION["qty"]); $i++){
        $suma=$_SESSION["price"][$i]*$_SESSION["qty"][$i];
        $taxes=$suma*0.13;
        $total= $taxes+$_SESSION["price"][$i];
        $numerolinea=$i+1;
        array_push($datos['detalleservicio']['lineadetalle'],array(
            'numerolinea'=>''.$numerolinea.'',
            'codproducto'=>$_SESSION['id_device'][$i],
            'cantidad'=>$_SESSION['qty'][$i],
            'detalleproducto'=>$_SESSION['model'][$i],
            'preciouni'=>$_SESSION['price'][$i],
            'montotal'=> ''.$suma.'',
            'tarifa'=>'0.13',
            'impuesto'=>''.$taxes.'',
            'montolinea'=>''.$total.''
        )); 
    }



$payload = json_encode($datos);



// //attach encoded JSON string to the POST fields
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);

// //set the content type to application/json
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));

// //return response instead of outputting
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// //execute the POST request
$result = curl_exec($ch);

$impr= json_decode($result);
print_r($impr);
// //close cURL resource
curl_close($ch);


?>
