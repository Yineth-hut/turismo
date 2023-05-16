
use id20758455_turismoz;
create table usuario(
id_Usuario int not null primary key auto_increment,
nombre_Usuario varchar(50),
correo_Usuario varchar(50),
contraseña_Usuario varchar(200) 
 );
 
 create table CentrosReligiosos(
id_Centro int not null primary key auto_increment,
nombre_Centro varchar(100),
direccion_Centro varchar(100),
descipcion_Centro varchar(500),
nombreSacerdote_Centro varchar(100),
contacto_Centro numeric(11),
imagen_Centro blob,
horario_Centro blob,
usuario_Id int not null ,
CONSTRAINT fk_usuario FOREIGN KEY (usuario_Id) REFERENCES usuario(id_Usuario)
 );
 
 create table actividadesReprecentativas(
id_Centro int not null primary key auto_increment,
nombre_Actividad varchar(100),
lugar_Actividad varchar(100),
descipcion_Actividad varchar(500),
contacto_Actividad numeric(11),
imagen_Actividad blob,
programacion_Actividad blob,
usuario_Id int not null ,
CONSTRAINT fk_usuarios FOREIGN KEY (usuario_Id) REFERENCES usuario(id_Usuario)
 );
 
  create table hoteles(
id_hotel int not null primary key auto_increment,
nombre_hotel varchar(100),
direccion_hotel varchar(100),
descipcion_hotel varchar(500),
contacto_hotel numeric(11),
imagen_hotel blob,
horarios_hotel blob,
servicios_hotel blob,
usuario_Id int not null ,
CONSTRAINT fk_usuario1 FOREIGN KEY (usuario_Id) REFERENCES usuario(id_Usuario)
 );
 
 create table restaurantes(
id_restaurante int not null primary key auto_increment,
nombre_restaurante varchar(100),
direccion_restaurante varchar(100),
descipcion_restaurante varchar(500),
contacto_restaurante numeric(11),
imagen_restaurante blob,
horarios_restaurante blob,
cartaDesayuno_restaurante blob,
cartaAlmuerzo_restaurante blob,
cartaPostres_restaurante blob,
usuario_Id int not null ,
CONSTRAINT fk_usuario2 FOREIGN KEY (usuario_Id) REFERENCES usuario(id_Usuario)
 );
 
 create table sitiosTuristicos(
id_sitiosT int not null primary key auto_increment,
nombre_sitiosT varchar(100),
direccion_sitiosT varchar(100),
descipcion_sitiosT varchar(500),
contacto_sitiosT numeric(11),
imagen_sitiosT blob,
horarios_sitiosT blob,
planes_sitiosT blob,
usuario_Id int not null ,
CONSTRAINT fk_usuario3 FOREIGN KEY (usuario_Id) REFERENCES usuario(id_Usuario)
 );
 