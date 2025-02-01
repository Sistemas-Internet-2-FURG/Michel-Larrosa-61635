BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "equipe" (
	"matricula"	INTEGER,
	"nome"	TEXT NOT NULL UNIQUE,
	"senha"	TEXT NOT NULL,
	"cargo"	TEXT NOT NULL,
	PRIMARY KEY("matricula" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "turmas" (
	"identificador"	TEXT,
	"disciplina"	TEXT NOT NULL,
	"professor"	INTEGER NOT NULL,
	FOREIGN KEY("professor") REFERENCES "equipe"("matricula"),
	PRIMARY KEY("identificador")
);
CREATE TABLE IF NOT EXISTS "alunos" (
	"matricula"	INTEGER,
	"turma"	TEXT,
	"nome"	TEXT NOT NULL,
	"nota"	INTEGER NOT NULL,
	PRIMARY KEY("matricula"),
	FOREIGN KEY("turma") REFERENCES "turmas"("identificador")
);
INSERT INTO "equipe" ("matricula","nome","senha","cargo") VALUES (1,'Silvia','diretores','DIRETOR');
INSERT INTO "equipe" ("matricula","nome","senha","cargo") VALUES (2,'Rafael','coordenadores','COORDENADOR');
INSERT INTO "equipe" ("matricula","nome","senha","cargo") VALUES (3,'Fernanda','professores','PROFESSOR');
INSERT INTO "equipe" ("matricula","nome","senha","cargo") VALUES (4,'publico','publico_pass','PÚBLICO');
INSERT INTO "turmas" ("identificador","disciplina","professor") VALUES ('1101','prog',3);
INSERT INTO "alunos" ("matricula","turma","nome","nota") VALUES (1,'1101','Marielli',0);
INSERT INTO "alunos" ("matricula","turma","nome","nota") VALUES (3,'1101','Muriel',0);
INSERT INTO "alunos" ("matricula","turma","nome","nota") VALUES (123,'1101','Murilo Couro',0);
INSERT INTO "alunos" ("matricula","turma","nome","nota") VALUES (12346,'1101','Erica',5);
INSERT INTO "alunos" ("matricula","turma","nome","nota") VALUES (61000,'1101','Renan',5);
INSERT INTO "alunos" ("matricula","turma","nome","nota") VALUES (61001,'1101','Renata',5);
INSERT INTO "alunos" ("matricula","turma","nome","nota") VALUES (61002,'1101','Renata R',5);
INSERT INTO "alunos" ("matricula","turma","nome","nota") VALUES (61004,'1101','Renata Aluno',5);
COMMIT;
