-- Affiche toutes les données.
select * from school, students;

-- Affiche uniquement les prénoms.
select prenom from students;

-- Affiche les prénoms, les dates de naissance et l’école de chacun.
select prenom, datenaissance, school from students;

-- Affiche uniquement les élèves qui sont de sexe féminin.
select * from students where genre = "F";

-- Affiche uniquement les élèves qui font partie de l’école d'Addy.
select * from students inner join school on students.school = school.idschool where school.school = 'Addy';
select * from students where school = "1";

-- Affiche uniquement les prénoms des étudiants, par ordre inverse à l’alphabet (DESC). Ensuite, la même chose mais en limitant les résultats à 2.
select prenom from students order by prenom desc;    //    select prenom from students order by prenom desc limit 2;

-- Ajoute Ginette Dalor, née le 01/01/1930 et affecte-la à Bruxelles, toujours en SQL.
insert into students (idstudent, nom, prenom, datenaissance, genre, school) values ('31', 'Dalor', 'Ginette', '1930-01-01', 'F', '2');

-- Modifie Ginette (toujours en SQL) et change son sexe et son prénom en “Omer”.
update students set genre = 'Omer', prenom = 'Omer' where prenom = "Ginette";

-- Supprimer la personne dont l’ID est 3.
delete from students where idstudent = '3';


-- Modifier le contenu de la colonne School de sorte que "1" soit remplacé par "Liege" et "2" soit remplacé par "Gent". (attention au type de la colonne !)
-- inner join was previously made for the "Addy" query, thus not needed here. We can change the values right away --
-- also, not sure this is the expected answer since there are a few ways to interpret the question :D
update school set school = 'Liege' where idschool = 1;
update school set school = 'Gent' where idschool = 2;