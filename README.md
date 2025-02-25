# 💵 BillGuard

Bienvenido a **BillGuard**, una aplicación para gestionar tus suscripciones (Netflix, Spotify ...) para ayudarte a gestionar tu cartera y  tener en un mismo sitio donde te estas gastando al mes en servicios de suscripción. Esta guía te ayudará a entender cómo funciona la aplicación y cómo está estructurada la base de datos.

### 📚 Índice

1. 🌟 [Introducción](./#introduccion)
2. 🗺️ [Diagrama E-R](./#diagrama-e-r)
3. 📋 [Descripción de Tablas](./#descripcion-de-tablas)

### 🌟 Introducción

**BillGuard** es una aplicación desarrollada en Python utilizando PyQt6 para la interfaz gráfica y SQLite para la base de datos, a parte de Firebase para la autentificación de usuarios. La aplicación permite a los usuarios gestionar sus suscripciones de manera eficiente.



### 🗺️ Diagrama E-R

A continuación se muestra el diagrama E-R de la base de datos utilizada en **BillGuard**:

![Diagrama E-R](https://vscode-file/vscode-app/c:/Users/josem/Escritorio/DIN/PyQt6/BillGuard/path/to/your/er-diagram.png)

### 📋 Descripción de Tablas

#### Tabla `usuarios`

| Columna           | Tipo    | Descripción                       |
| ----------------- | ------- | --------------------------------- |
| `id`              | INTEGER | Identificador único del usuario   |
| `nombre`          | TEXT    | Nombre del usuario                |
| `email`           | TEXT    | Email del usuario                 |
| `contraseña_hash` | TEXT    | Hash de la contraseña del usuario |

#### Tabla `suscripciones`

| Columna            | Tipo    | Descripción                                           |
| ------------------ | ------- | ----------------------------------------------------- |
| `id`               | INTEGER | Identificador único de la suscripción                 |
| `usuario_id`       | INTEGER | Identificador del usuario                             |
| `nombre_servicio`  | TEXT    | Nombre del servicio                                   |
| `costo_mensual`    | REAL    | Costo mensual de la suscripción                       |
| `fecha_inicio`     | TEXT    | Fecha de inicio de la suscripción                     |
| `fecha_renovacion` | TEXT    | Fecha de renovación de la suscripción                 |
| `estado`           | TEXT    | Estado de la suscripción (Activo, Pausado, Cancelado) |
| `metodo_pago_id`   | INTEGER | Identificador del método de pago asociado             |

#### Tabla `metodos_pago`

| Columna             | Tipo    | Descripción                                                                      |
| ------------------- | ------- | -------------------------------------------------------------------------------- |
| `id`                | INTEGER | Identificador único del método de pago                                           |
| `usuario_id`        | INTEGER | Identificador del usuario                                                        |
| `nombre`            | TEXT    | Nombre del método de pago                                                        |
| `tipo`              | TEXT    | Tipo del método de pago (Cuenta Bancaria, Tarjeta de Débito, Tarjeta de Crédito) |
| `numero`            | TEXT    | Número del método de pago                                                        |
| `fecha_vencimiento` | TEXT    | Fecha de vencimiento del método de pago                                          |
