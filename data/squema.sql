create table usuarios (
ID SERIAL primary key,
username varchar(50) not null,
password_hash varchar(100),
foto_perfil varchar(255) default 'default_avatar.png'
);

create type status_jogo as enum ('iniciado', 'zerado','engavetado', 'abandonado');

create table jogos (
ID serial primary key,
usuario_ID int,
titulo varchar(100) not null,
plataforma varchar(50),
status status_jogo default 'engavetado',
data_inicio date,
data_fim date,
foreign key(usuario_ID) references usuarios(ID)
);
