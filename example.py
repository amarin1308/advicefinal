from flask import Flask, jsonify, abort, make_response, request
import xml.etree.ElementTree as et
from xml.dom import minidom
import psycopg2
from lxml import etree
import lxml

def embellecedor(expXML):
    contenido = et.tostring(expXML, 'utf-8').decode('utf8')
    procesado = minidom.parseString(contenido)
    return procesado.toprettyxml(indent="  ")


connection=psycopg2.connect(
    host='localhost',
    user='postgres',
    password='utn',
    database='postgres',
    )
cursor=connection.cursor()


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
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
     return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/factura', methods=['GET'])
def get_tasks():

    informacion = et.Element('FacturaElectronica')

    et.SubElement(informacion,'Clave').text = '0000000000000000000000000000000000000'
    et.SubElement(informacion,'CodigoActividad').text = '00000'
    et.SubElement(informacion,'NumeroConsecutivo').text = '00000000000000000000'
    et.SubElement(informacion,'FechaEmision').text = '24/07/2021 12:35:00'



    emisor = et.SubElement(informacion,'Emisor')
    et.SubElement(emisor,'Nombre').text = 'Datanet'

    identificacion = et.SubElement(emisor,'Identificacion')
    et.SubElement(identificacion,'Tipo').text= '01'
    et.SubElement(identificacion,'Numero').text= '310123456'

    ubicacion = et.SubElement(emisor,'Ubicacion')
    et.SubElement(ubicacion,'Direccion').text= 'Miramar, Puntarenas'

    telefono = et.SubElement(emisor,'Telefono')
    et.SubElement(telefono,'CodigoPais').text= '506'
    et.SubElement(telefono,'Numero').text= '26212122'

    et.SubElement(emisor,'CorreoElectronico').text = 'datanetinfo@gmail.com'

    receptor = et.SubElement(informacion,'Receptor')
    et.SubElement(receptor,'Nombre').text = 'Andrio Marin'
    
    identificacion = et.SubElement(receptor,'Identificacion')
    et.SubElement(identificacion,'Tipo').text= '02'
    et.SubElement(identificacion,'Numero').text= '123456789'

    ubicacion = et.SubElement(receptor,'Ubicacion')
    et.SubElement(ubicacion,'Direccion').text= 'Alajuelita, San Jose'

    telefono = et.SubElement(receptor,'Telefono')
    et.SubElement(telefono,'CodigoPais').text= '506'
    et.SubElement(telefono,'Numero').text= '83119850'

    et.SubElement(receptor,'CorreoElectronico').text = 'andrio13marin@gmail.com'

    DetalleServicio = et.SubElement(informacion,'DetalleServicio')
    LineaDetalle = et.SubElement(DetalleServicio,'LineaDetalle')
    et.SubElement(LineaDetalle,'NumeroLinea').text= '1'
    CodigoComercial = et.SubElement(LineaDetalle,'CodigoComercial')
    et.SubElement(CodigoComercial,'Codigo').text= 'PCD1070'
    et.SubElement(LineaDetalle,'Cantidad').text= '1'
    et.SubElement(LineaDetalle,'Detalle').text= 'msi modern b11mo-056 xsp'
    et.SubElement(LineaDetalle,'PrecioUnitario').text= '650.000'
    et.SubElement(LineaDetalle,'MontoTotal').text= '650.000'
    impuesto = et.SubElement(LineaDetalle,'Impuesto')
    et.SubElement(impuesto,'Tarifa').text= '13.00'
    et.SubElement(impuesto,'Tarifa').text= '84.500'
    et.SubElement(LineaDetalle,'MontoTotalLinea').text= '734.500'

    ResumenFactura = et.SubElement(informacion,'ResumenFactura')
    CodigoTipoMoneda = et.SubElement(ResumenFactura,'CodigoTipoMoneda')
    et.SubElement(CodigoTipoMoneda,'CodigoMoneda').text= 'CRC'
    et.SubElement(ResumenFactura,'TotalVenta').text= '734.500'
    et.SubElement(ResumenFactura,'TotalDescuentos').text= '0'
    et.SubElement(ResumenFactura,'TotalVentaNeta').text= '650.000'
    et.SubElement(ResumenFactura,'TotalImpuesto').text= '84.500'
    et.SubElement(ResumenFactura,'TotalComprobante').text= '734.500'

    return jsonify({'xml':embellecedor(informacion)})


if __name__ == '__main__':
    app.run(host='192.168.1.103', port=4000, debug=True)

