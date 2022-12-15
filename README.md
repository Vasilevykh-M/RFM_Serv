# RFM_Serv
в файле servers.json лежит список серваков к которым мы можем цепануться \n
в файле config.ini лежит мой ip:port + настройки подключения к бд \n
скрипт создания бд \n
create DATABASE servers;
create table table_name
(
id_folder uuid default gen_random_uuid() not null
constraint table_name1_pk
primary key,
id_server integer not null
);

alter table table_name
owner to postgres;
