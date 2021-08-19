from flask import Flask, jsonify, abort, make_response, request
import xml.etree.ElementTree as et
from xml.dom import minidom
import psycopg2
import os
import lxml
from lxml import etree
import lxml

connection=psycopg2.connect(
    host='localhost',
    user='postgres',
    password='utn',
    database='postgres',
    )
cursor=connection.cursor()

def embellecedor(expXML):
    contenido = et.tostring(expXML, 'utf-8').decode('utf8')
    procesado = minidom.parseString(contenido)
    return procesado.toprettyxml(indent="  ")

app = Flask(__name__)

@app.route('/prueba2', methods=['POST'])



def addOne():
    
    if consulta(request.json['emisor']["id"]["numeroid"]):
            informacion = et.Element('FacturaElectronica')
            et.SubElement(informacion,'Clave').text = request.json['clave']
            et.SubElement(informacion,'CodigoActividad').text = request.json['codigoactividad']
            et.SubElement(informacion,'NumeroConsecutivo').text = request.json['numeroconsecutivo']
            et.SubElement(informacion,'FechaEmision').text = request.json['fechaemision']



            emisor = et.SubElement(informacion,'Emisor')
            et.SubElement(emisor,'Nombre').text = request.json['emisor']["nombre"]

            identificacion = et.SubElement(emisor,'Identificacion')
            et.SubElement(identificacion,'Tipo').text= request.json['emisor']["id"]["tipoid"]
            et.SubElement(identificacion,'Numero').text= request.json['emisor']["id"]["numeroid"]

            ubicacion = et.SubElement(emisor,'Ubicacion')
            et.SubElement(ubicacion,'Direccion').text= request.json['emisor']['ubicacion']["direccion"]

            telefono = et.SubElement(emisor,'Telefono')
            et.SubElement(telefono,'CodigoPais').text= request.json['emisor']["telefono"]["codigop"]
            et.SubElement(telefono,'Numero').text= request.json['emisor']["telefono"]["numero"]

            et.SubElement(emisor,'CorreoElectronico').text = request.json['emisor']["email"]

            receptor = et.SubElement(informacion,'Receptor')
            et.SubElement(receptor,'Nombre').text = request.json['receptor']['nombre']
            
            identificacion = et.SubElement(receptor,'Identificacion')
            et.SubElement(identificacion,'Tipo').text= request.json['receptor']['id']["tipoid"]
            et.SubElement(identificacion,'Numero').text= request.json['receptor']['id']["numeroid"]

            ubicacion = et.SubElement(receptor,'Ubicacion')
            et.SubElement(ubicacion,'Direccion').text= request.json['receptor']['ubicacion']["direccion"]

            telefono = et.SubElement(receptor,'Telefono')
            et.SubElement(telefono,'CodigoPais').text= request.json['receptor']['telefono']["codigop"]
            et.SubElement(telefono,'Numero').text= request.json['receptor']['telefono']["numero"]

            et.SubElement(receptor,'CorreoElectronico').text = request.json['receptor']['email']

            DetalleServicio = et.SubElement(informacion,'DetalleServicio')
        
            for i in request.json['detalleservicio']['lineadetalle']:
                LineaDetalle = et.SubElement(DetalleServicio,'LineaDetalle')
                et.SubElement(LineaDetalle,'NumeroLinea').text=i['numerolinea']
                et.SubElement(LineaDetalle,'Codigo').text=i['codproducto']
                et.SubElement(LineaDetalle,'Cantidad').text=i['cantidad']
                et.SubElement(LineaDetalle,'Detalle').text=i['detalleproducto']
                et.SubElement(LineaDetalle,'PrecioUnitario').text=i['preciouni']
                et.SubElement(LineaDetalle,'MontoTotal').text=i['montotal']
                et.SubElement(LineaDetalle,'Tarifa').text=i['tarifa']
                et.SubElement(LineaDetalle,'Impuesto').text=i['impuesto']
                et.SubElement(LineaDetalle,'MontoTotalLinea').text=i['montolinea']



            ResumenFactura = et.SubElement(informacion,'ResumenFactura')
            CodigoTipoMoneda = et.SubElement(ResumenFactura,'CodigoTipoMoneda')
            et.SubElement(CodigoTipoMoneda,'CodigoMoneda').text= request.json["resumenfactura"]["codtipomoneda"]['codmoneda']
            et.SubElement(ResumenFactura,'TotalVenta').text= request.json["resumenfactura"]['totalventa']
            et.SubElement(ResumenFactura,'TotalDescuentos').text= request.json["resumenfactura"]['descuentos']
            et.SubElement(ResumenFactura,'TotalVentaNeta').text= request.json["resumenfactura"]['totalventaneta']
            et.SubElement(ResumenFactura,'TotalImpuesto').text= request.json["resumenfactura"]['totalimpuesto']
            et.SubElement(ResumenFactura,'TotalComprobante').text= request.json["resumenfactura"]['total']

            Firma = et.SubElement(informacion,'FirmaDigital')
            et.SubElement(Firma,'FirmaDigital').text=request.json["firmadigital"]['firma']
            xml=embellecedor(informacion)
            if validate(xml, "factura.xsd"):
                return jsonify({'xml':embellecedor(informacion)})
            else:
                mensaje="Hay problemas con el xml"
                return mensaje   
    else:
        novalido="El cliente no existe"
        return (novalido) 

def consulta(id: int) -> bool:
    resultado=False
    cursor.execute("SELECT COUNT(1) FROM clientes WHERE idusuario =%s;", (id,))
    rows=cursor.fetchall()
    
    if (rows[0][0]==1):
        resultado=True
    
    return resultado

def validate(xml_path: str, xsd_path: str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml_file = lxml.etree.XML(xml_path)
    result = xmlschema.validate(xml_file)

    return result

if __name__ == '__main__':
    app.run(host='192.168.1.103', port=8080, debug=True)
