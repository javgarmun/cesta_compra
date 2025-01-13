# Módulo Cesta de la Compra

## Descripción

Este módulo permite crear y gestionar cestas de la compra dentro de Odoo. Cada cliente puede agregar productos o
servicios a sus cestas, gestionar las cantidades y precios. El módulo se encarga de calcular automáticamente los
subtotales de las líneas de la cesta y el total de la misma.

Además, ofrece una interfaz intuitiva para administrar tanto las cestas como los productos asociados, permitiendo a los
usuarios finales gestionar su compra de manera eficiente.

## Requisitos previos

- Odoo 13.0 o superior
- Entorno de Python configurado con sus correspondientes dependencias
- Acceso de administrador para instalar el módulo

## Pasos para instalar el módulo

1. **Clona el repositorio o descarga el módulo en formato ZIP:**

```bash
git clone https://github.com/javgarmun/cesta_compra.git
```

2. **Descomprime y coloca el módulo en la carpeta de `odoo-custom-addons`. Reinicia el servidor de Odoo
   para que el módulo sea detectado.**
   

3. **Instala el módulo desde la interfaz de Odoo (recuerda activar el modo desarrollador):**
   - Ve al menú de "Aplicaciones"
   - Busca el módulo "Cesta de la Compra" o simplemente filtra por "cesta"
   - Localiza el módulo y haz clic en "Instalar"
   
## Autor

Javier García Muñoz

GitHub: https://github.com/javgarmun/cesta_compra