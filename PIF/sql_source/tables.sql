Use FUTSTORE

CREATE TABLE USUARIO{
    Id_usuario INT AUTO_INCREMENT PRIMARY KEY, 
    Nombre_cliente VARCHAR(35) NOT NULL,
    Nombre_usuario VARCHAR(15)  NOT NULL,
    Correo VARCHAR(50) UNIQUE NOT NULL,
    Contraseña VARCHAR(15) NOT NULL, 
    Estado ENUM('Activo', 'Inactivo') NOT NULL DEFAULT 'Activo'
};

CREATE TABLE JERSEY{
    Id_Jersey INT AUTO_INCREMENT PRIMARY KEY,
    Modelo VARCHAR(100) NOT NULL,
    Marca VARCHAR(10) NOT NULL,
    Precio FLOAT NOT NULL,
    Talla VARCHAR(5) NOT NULL,
    Imagen VARCHAR(300) NOT NULL,
    Estado ENUM('Activo','Inactivo') NOT NULL DEFAULT 'Activo'
};

CREATE TABLE HISTORIAL_VENTAS{
    Id_venta INT AUTO_INCREMENT PRIMARY KEY,
    Id_usuario2 INT NOT NULL -- llave foranea del usuario
    Monto_total FLOAT NOT NULL,
    Tipo_pago VARCHAR(15) NOT NULL,
    Fecha_compra DATE NOT NULL,
    FOREIGN KEY (Id_usuario2) REFERENCES USUARIO(Id_usuario)
};

CREATE TABLE Envios{
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Id_venta2 INT NOT NULL, -- llave foranea de la compra
    Direccion VARCHAR(40) NOT NULL,
    Tipo_envio VARCHAR(20) NOT NULL,
    Fecha_envio DATE NOT NULL,
    FOREIGN KEY (Id_venta2) REFERENCES HISTORIAL_VENTAS(Id_venta)
};

CREATE TABLE VENTAS_JERSERY{
    Id_venta3 INT NOT NULL,
    Id_Jersey3 INT NOT NULL,
    PRIMARY KEY (Id_venta3, Id_Jersey3),
    FOREIGN KEY (Id_venta3) REFERENCES HISTORIAL_VENTAS(Id_venta),
    FOREIGN KEY (Id_Jersey3) REFERENCES HISTORIAL_VENTAS(Id_Jersey) 
};

