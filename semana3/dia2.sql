USE Cursos;
CREATE TABLE IF NOT EXISTS alumno(
    id int(11) NOT NULL AUTO_INCREMENT,
    nombres varchar(100) NOT NULL,
    apellidos varchar(100) NOT NULL,
    email varchar(150) NOT NULL,
    pais varchar(100) DEFAULT 'Peru',
    nota int(11) DEFAULT '0',
    PRIMARY_KEY(id)
);

CREATE TABLE IF NOT EXISTS alumno_nota(
    id int(11) NOT NULL PRIMARY_KEY AUTO_INCREMENT,
    alumno_id int(11) NOT NULL,
    curso varchar(100) NOT NULL,
    nota int(11) DEFAULT 0,
    FOREIGN KEY (alumno_id) REFERENCES alumno(id)
);