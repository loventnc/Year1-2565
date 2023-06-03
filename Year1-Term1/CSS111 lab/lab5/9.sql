CREATE TABLE Foods (
ID integer PRIMARY KEY,
Name varchar(50) NOT NULL,
ServingSize varchar(50) NOT NULL,
Fiber float NOT NULL,
Type varchar(50) NOT NULL,
C float NOT NULL
);
INSERT into Foods values (1, 'Corn bran crude', '1cup', 79, 'Cereal Grains and Pasta', 0);
INSERT into Foods values (2, 'Spices cinnamon ground', '1tbsp', 54.3, 'Spices and Herbs', 28.5);
INSERT into Foods values (3, 'Cereals', '0.333cup', 43, 'Breakfast Cereals', 20);
INSERT into Foods values (4, 'Wheat bran crude', '1cup', 42.8, 'Cereal Grains and Pasta', 0);
INSERT into Foods values (5, 'Oregano dried', '1tsp ground', 42.8, 'Spices and Herbs', 50);
INSERT into Foods values (6, 'Coriander seed', '1tbsp', 41.9, 'Spices and Herbs', 21);
INSERT into Foods values (7, 'Basil dried', '1tbsp ground', 40.5, 'Spices and Herbs', 61.2);
INSERT into Foods values (8, 'Bean soup with bacon', '1cup', 30.8, 'Soups, Sauces and Gravies',
4);
INSERT into Foods values (10, 'Parsley dried', '1tbsp', 30.4, 'Spices and Herbs', 122);
INSERT into Foods values (11, 'Spearmint dried', '1tbsp', 29.8, 'Spices and Herbs', 0);

delete from Foods where C = '0' or Fiber < '40';
select * from Foods;