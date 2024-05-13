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



CREATE TABLE CARRITO{
        Id_carrito INT AUTO_INCREMENT PRIMARY KEY,
        Id_usuario_carrito INT,
        Id_producto INT, 
        Cantidad INT,
        FOREIGN KEY (Id_usuario_carr) REFERENCES USUARIO(Id_usuario),
        FOREIGN KEY (Id_producto) REFERENCES JERSEY(Id_Jersey)
    
};

CREATE TABLE HISTORIAL_VENTAS(
    Id_venta INT AUTO_INCREMENT PRIMARY KEY,
    Id_usuario2 INT NOT NULL, -- llave foranea del usuario
    Fecha_compra DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (Id_usuario2) REFERENCES USUARIO(Id_usuario)
);

CREATE TABLE ORDENES(
    Id_orden INT AUTO_INCREMENT PRIMARY KEY,
    Id_venta2 INT,
    Id_producto INT, 
    Cantidad INT,
    FOREIGN KEY (Id_venta2) REFERENCES HISTORIAL_VENTAS(Id_venta),
    FOREIGN KEY (Id_producto) REFERENCES JERSEY(Id_Jersey)
);

CREATE TABLE INVENTARIO (
    Id_inventario INT AUTO_INCREMENT PRIMARY KEY,
    Id_jersey INT NOT NULL,
    Talla VARCHAR(5) NOT NULL,
    Cantidad_disponible INT NOT NULL,
    FOREIGN KEY (Id_jersey) REFERENCES JERSEY(Id_Jersey)
);

