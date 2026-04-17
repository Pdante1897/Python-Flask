drop database python

use sys

CREATE DATABASE python;

Use python

create table pelicula (
	id int AUTO_INCREMENT PRIMARY KEY,
	titulo varchar(100) not null,
	director varchar(100) not null,
	anio int not null,
	rating decimal(3,1) null,
	genero varchar(100), 
	imagen longtext
);


INSERT into pelicula(titulo, director, anio)
values ('Habia una vez en Holliwood', 'Quentin Tarantino', 2019);


INSERT into pelicula(titulo, director, anio)
values ('ScarFace', 'Brian De Palma', 1983);
INSERT into pelicula(titulo, director, anio)
values ('KillBill', 'Quentin Tarantino', 2003);



select * from pelicula p where anio = 2019 and p.director = 'Quentin Tarantino';

select * from pelicula p where p.director = 'Quentin Tarantino';
