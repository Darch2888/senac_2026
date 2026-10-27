-- apagando banco de dados caso exista
drop database if exists dbexercicio11;

-- criar base
create database dbexercicio11;

use dbexercicio11;

create table aluno(
	idaluno int not null auto_increment
    , nome varchar(45) not null
    , primary key (idaluno)
);

