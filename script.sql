create extension if not exists "uuid-ossp";

create table pessoa(
id 					uuid primary key default uuid_generate_v4(),
usuario				varchar(200) not null,
senha				varchar(200) not null
)

create table fornecedor(
id                  uuid primary key default uuid_generate_v4(),
nome                varchar(200) not null,
status              boolean not null    
);

create table produto(
id                  uuid primary key default uuid_generate_v4(),
nome                varchar(200) not null,
quantidade          int not null,
idFornecedor        uuid not null,
status             boolean not null,
constraint produto_idFornecedor_fkey foreign key(idFornecedor) references fornecedor(id)
);