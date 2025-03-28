LOAD DATA INFILE '/caminho/para/Rol_de_Procedimentos.csv'
INTO TABLE procedimentos
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(codigo, descricao, tipo);
