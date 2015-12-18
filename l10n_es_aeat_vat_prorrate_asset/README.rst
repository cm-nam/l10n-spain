.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================================
AEAT - Prorrata de IVA - Extensión para activos
===============================================

Extensión de la prorrata de IVA cuando se lleva gestión de activos:

* Aumento del valor del activo según el porcentaje de prorrata cuando se crea
  desde la factura de compra.
* Regularización en la declaración del 303 del cuarto trimestre de la cantidad
  amortizada según el porcentaje definitivo de prorrata.

Configuración
=============

En la declaración del modelo 303 del último trimestre del ejercicio, hay que
introducir la cuenta contable a la que llevar la diferencia de la amortización
de los activos según el porcentaje de prorrata definitivo.

Uso
===

Al realizar una factura de proveedor y rellenar en una línea la categoría de
activo para auto-crear el activo, se habilita al lado una casilla
"Porc. prorrata", con valor por defecto 100, en la que debemos poner el
porcentaje de prorrata provisional que se esté utilizando ese año. De esa
forma, el activo tendrá un mayor valor bruto en base a ese porcentaje.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/189/8.0

Problemas conocidos / Hoja de ruta
==================================

* La prorrata especial de IVA no está contemplada.

Créditos
========

Contribudores
-------------

* Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>

Maintainer
----------

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
